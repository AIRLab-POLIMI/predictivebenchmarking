import sys,argparse
import cv2
from PIL import Image,ImageDraw,ImageFont
from os import listdir,makedirs
from os.path import join,exists, isdir,isfile
from structures.run import Run
from structures.dataset import Dataset
from structures.statistics import Stats, ErrorStats, RunStats, PerfStats, GraphStats
from structures.geometry import Geometry
import numpy as np
import util.util_XML as xmlutil
import matplotlib.pyplot as plt
import math
import networkx as nx
import datetime as dt
from sklearn.externals import joblib
from scipy.stats import pearsonr
from sklearn import linear_model, svm
from sklearn.model_selection import KFold, RepeatedKFold, RepeatedStratifiedKFold, cross_val_score, train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.decomposition import PCA
from sklearn import preprocessing, feature_selection
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression, RFECV, RFE
from shapely.geometry import Polygon, Point
from skimage.morphology import skeletonize
from skimage import img_as_ubyte
from copy import deepcopy
from itertools import product

''' Dataset Analyzer 
This script performs the following operations:
1) collects, for each environment, the SLAM performances as computed by the metricEvaluator over all the runs
2) computes the sample localization error
3) loads the corresponding layout reconstruction XML and bitmap Voronoi graph
4) computes the topological and Voronoi graphs
5) extracts relevant features for the analysis
6) correlates the extracted features with the localization error 
'''

def extractRunStatsFromErrorFile(errorFile):
	if exists(errorFile):
		runStats = None
		file = open(errorFile, 'r')
		first = True
		for line in file:
			words = line.split(', ')
			# skip the very first line, which just contains the name of the fields
			if first is True:
				first = False
			else:
				runStats = RunStats(float(words[0]),float(words[1]),float(words[2]),float(words[3]),int(words[4]))
		file.close()
		return runStats
	else:
		raise IOError('Error file '+errorFile+ ' not found.')

def extractTimestampedPose(words):
	pose = dict()
	pose["t"] = float(words[0])
	pose["x"] = float(words[1])
	pose["y"] = float(words[2])
	pose["theta"] = float(words[3])
	return pose

def extractRunStatsFromGTLog(gtLog):
	if exists(gtLog):
		file = open(gtLog,'r')
		first = True
		prevPose = extractTimestampedPose([0]*4)
		totalLength = 0
		totalRot = 0
		for line in file:
			words = line.split(' ')
			if first is True:
				first = False
				prevPose = extractTimestampedPose(words)
			else:
				curPose = extractTimestampedPose(words)
				totalLength += math.sqrt(math.pow(curPose["x"]-prevPose["x"],2)+math.pow(curPose["y"]-prevPose["y"],2))
				totalRot += (np.pi - math.fabs(math.fabs(correct_angle(curPose["theta"]) - correct_angle(prevPose["theta"])) - np.pi))
				prevPose = curPose
		totalTime = float(line.split(' ')[0])
		return totalTime, totalLength, totalRot
	else:
		raise IOError('Ground Truth log '+gtLog+' not found.')

def loadDatasetRun(datasetRunPath,datasetName):
	# for the specified dataset, load the metricEvaluator errors of that run
	try:
		tstats = extractRunStatsFromErrorFile(join(datasetRunPath+'/Errors/Original/RE/T.errors'))
		rstats = extractRunStatsFromErrorFile(join(datasetRunPath+'/Errors/Original/RE/R.errors'))
		totalTime, totalLength, totalRot = extractRunStatsFromGTLog(join(datasetRunPath,datasetName)+'.log')
	except IOError as err:
		raise RuntimeError("Error while loading the dataset runs! Trouble at "+join(datasetRunPath,datasetName))
	# if we are here, we successfully loaded the error stats from file
	myRun = Run(tstats,rstats,totalTime,totalLength,totalRot)
	return myRun

def loadDatasetRuns(runsFolder, datasetName):
	# loads all the runs of the specified dataset
	runs = []
	datasetPath = join(runsFolder,datasetName)
	for r in listdir(datasetPath):
		if r[:3]=="run":
			runs.append(loadDatasetRun(join(datasetPath,r),datasetName))
	return runs

def computeErrorStats(runs, errorType):
	meansList = []
	stdsList = []
	numSamplesList = []
	''' For each run, add the mean and standard deviation of the selected error type, and the number
	of samples, to a list '''
	for r in runs:
		runStats = r.transStats if (errorType=="trans") else r.rotStats
		meansList.append(runStats.mean)
		stdsList.append(runStats.std)
		numSamplesList.append(runStats.numSamples)
	''' Convert the lists to numpy arrays '''
	meansArray = np.array(meansList)
	stdsArray = np.array(stdsList)
	numSamplesArray = np.array(numSamplesList)
	''' For each of them compute mean and standard deviation '''
	mean = Stats(meansArray.mean(),meansArray.std())
	std = Stats(stdsArray.mean(), stdsArray.std())	
	numSamples = Stats(numSamplesArray.mean(), numSamplesArray.std())
	# build an errorStats object and return it
	return ErrorStats(mean, std, numSamples)

def computeRunStats(runs):
	totalTimesList = []
	totalLengthsList = []
	totalRotsList = []
	''' For each run, add the mean and standard deviation of the selected error type, and the number
	of samples, to a list '''
	for r in runs:
		totalTimesList.append(r.totalTime)
		totalLengthsList.append(r.totalLength)
		totalRotsList.append(r.totalRot)
	''' Convert the lists to numpy arrays '''
	totalTimesArray = np.array(totalTimesList)
	totalLengthsArray = np.array(totalLengthsList)
	totalRotsArray = np.array(totalRotsList)
	''' For each of them compute mean and standard deviation '''
	totalTime = Stats(totalTimesArray.mean(), totalTimesArray.std())
	totalLength = Stats(totalLengthsArray.mean(), totalLengthsArray.std())
	totalRot = Stats(totalRotsArray.mean(), totalRotsArray.std())
	# build an errorStats object and return it
	return totalTime, totalLength, totalRot

def computePerformanceStats(runs):
	transErrorStats = computeErrorStats(runs, errorType="trans")
	rotErrorStats = computeErrorStats(runs, errorType="rot")
	totalTime, totalLength, totalRot = computeRunStats(runs)
	return PerfStats(transErrorStats,rotErrorStats,totalTime,totalLength,totalRot)

def loadGeometry(xmlFile):
	# load and parse the xml of the layout
	rooms, connectedRooms, boundingPolygon, scalingFactor = xmlutil.loadXML(xmlFile)
	datasetGeometry = Geometry(rooms, boundingPolygon, scalingFactor)
	#myDataset.geometry = datasetGeometry
	# create the topological graph
	G=nx.Graph()
	G.add_edges_from(connectedRooms)
	Gc = max(nx.connected_component_subgraphs(G), key=len)
	#myDataset.topology = Gc
	#myDataset.topologyStats = GraphStats(Gc)
	return datasetGeometry, Gc, GraphStats(Gc)

def loadDataset(datasetName, runsFolder):
	# load the runs
	print "Loading runs of "+datasetName+"...",
	sys.stdout.flush()
	runs = loadDatasetRuns(runsFolder, datasetName)
	print "[DONE, "+str(len(runs))+" runs loaded]"
	# compute the performance statistics
	perfStats = computePerformanceStats(runs)
	# create the dataset object
	myDataset = Dataset(datasetName, runs, perfStats)
	return myDataset

def getRunStats():
	runStats = dict()
	runStats["totalTime"] = (lambda dataset: dataset.perfStats.totalTime)
	runStats["totalLength"] = (lambda dataset: dataset.perfStats.totalLength)
	return runStats

def getErrorTypes():
	errorTypes = dict()
	errorTypes["transError"] = (lambda dataset: dataset.perfStats.transError)
	errorTypes["rotError"] = (lambda dataset: dataset.perfStats.rotError)
	return errorTypes

def getErrorAttrs():
	errorAttrs = dict()
	errorAttrs["mean"] = (lambda error: error.mean)
	errorAttrs["std"] = (lambda error: error.std)
	errorAttrs["numSamples"] = (lambda error: error.numSamples)
	return errorAttrs

def getAttrStats():
	attrStats = dict()
	attrStats["mean"] = (lambda attr: attr.mean)
	attrStats["std"] = (lambda attr: attr.std)
	return attrStats

def addGeometricalPredictors(predictors):
	predictors["area"] = (lambda dataset: (dataset.geometry.shape.area))
	predictors["perimeter"] = (lambda dataset: (dataset.geometry.shape.perimeter))
	predictors["wallRatio"] = (lambda dataset: (dataset.geometry.shape.wallRatio))
	predictors["numRooms"] = (lambda dataset: (len(dataset.geometry.rooms)))
	predictors["avgRoomArea"] = (lambda dataset: np.array([r.shape.area for r in dataset.geometry.rooms]).mean()**2)
	predictors["avgRoomPerimeter"] = (lambda dataset: np.array([r.shape.perimeter for r in dataset.geometry.rooms]).mean()**2)
	predictors["avgRoomWallRatio"] = (lambda dataset: np.array([r.shape.wallRatio for r in dataset.geometry.rooms]).mean()**2)
	predictors["roomPerimeter"] = 	(lambda dataset: np.array([r.shape.perimeter for r in dataset.geometry.rooms]).sum())
	return predictors

def getGeometricalPredictors():
	return addGeometricalPredictors({}).keys()

def addTopologicalPredictors(predictors):
	predictors["topology_nodes"] = (lambda dataset: dataset.topologyStats.nodes)
	predictors["topology_edges"] = (lambda dataset: dataset.topologyStats.edges)
	predictors["topology_avg_shortest_path_length"] = (lambda dataset : dataset.topologyStats.avg_shortest_path_length)
	predictors["topology_density"] = (lambda dataset : dataset.topologyStats.density)
	predictors["topology_diameter"] = (lambda dataset: dataset.topologyStats.diameter)
	predictors["topology_radius"] = (lambda dataset: dataset.topologyStats.radius)
	predictors["topology_numBifurcationPoints"] = (lambda dataset: len(get_bifurcation_points(dataset.topology)))
	predictors["topology_avg_betweenness_centrality"] = (lambda dataset: dataset.topologyStats.betweenness_centrality.mean())
	predictors["topology_avg_eigenvector_centrality"] = (lambda dataset: dataset.topologyStats.eigenvector_centrality.mean())
	predictors["topology_avg_katz_centrality"] = (lambda dataset: dataset.topologyStats.katz_centrality.mean())
	predictors["topology_avg_closeness_centrality"] = (lambda dataset: dataset.topologyStats.closeness_centrality.mean())
	predictors["topology_std_betweenness_centrality"] = (lambda dataset: dataset.topologyStats.betweenness_centrality.std())
	predictors["topology_std_eigenvector_centrality"] = (lambda dataset: dataset.topologyStats.eigenvector_centrality.std())
	predictors["topology_std_katz_centrality"] = (lambda dataset: dataset.topologyStats.katz_centrality.std())
	predictors["topology_std_closeness_centrality"] = (lambda dataset: dataset.topologyStats.closeness_centrality.std())
	return predictors

def getTopologicalPredictors():
	return addTopologicalPredictors({}).keys()

def addVoronoiGraphPredictors(predictors):
	predictors["voronoi_traversal_distance"] = (lambda dataset: (dataset.voronoiDistance))
	predictors["voronoi_traversal_rotation"] = (lambda dataset: (dataset.voronoiRotation))
	predictors["voronoi_nodes"] = (lambda dataset: dataset.voronoiStats.nodes)
	predictors["voronoi_edges"] = (lambda dataset: dataset.voronoiStats.edges)
	predictors["voronoi_avg_shortest_path_length"] = (lambda dataset : dataset.voronoiStats.avg_shortest_path_length)
	predictors["voronoi_density"] = (lambda dataset : dataset.voronoiStats.density)
	predictors["voronoi_diameter"] = (lambda dataset: dataset.voronoiStats.diameter)
	predictors["voronoi_radius"] = (lambda dataset: dataset.voronoiStats.radius)
	predictors["voronoi_numBifurcationPoints"] = (lambda dataset: len(get_bifurcation_points(dataset.voronoi)))
	predictors["voronoi_numTerminalPoints"] = (lambda dataset: len(get_terminal_points(dataset.voronoi)))
	predictors["voronoi_avg_betweenness_centrality"] = (lambda dataset: dataset.voronoiStats.betweenness_centrality.mean())
	predictors["voronoi_avg_eigenvector_centrality"] = (lambda dataset: dataset.voronoiStats.eigenvector_centrality.mean())
	predictors["voronoi_avg_katz_centrality"] = (lambda dataset: dataset.voronoiStats.katz_centrality.mean())
	predictors["voronoi_avg_closeness_centrality"] = (lambda dataset: dataset.voronoiStats.closeness_centrality.mean())
	predictors["voronoi_std_betweenness_centrality"] = (lambda dataset: dataset.voronoiStats.betweenness_centrality.std())
	predictors["voronoi_std_eigenvector_centrality"] = (lambda dataset: dataset.voronoiStats.eigenvector_centrality.std())
	predictors["voronoi_std_katz_centrality"] = (lambda dataset: dataset.voronoiStats.katz_centrality.std())
	predictors["voronoi_std_closeness_centrality"] = (lambda dataset: dataset.voronoiStats.closeness_centrality.std())
	return predictors

def getVoronoiGraphPredictors():
	return addVoronoiGraphPredictors({}).keys()

def addVoronoiTraversalPredictors(predictors):
	predictors["voronoi_traversal_distance"] = (lambda dataset: (dataset.voronoiDistance))
	predictors["voronoi_traversal_rotation"] = (lambda dataset: (dataset.voronoiRotation))
	return predictors

def getVoronoiTraversalPredictors():
	return addVoronoiTraversalPredictors({}).keys()

def getPredictors(debugMode):
	predictors = dict()
	if debugMode > 0:
		predictors["totalLength"] = (lambda dataset : (dataset.perfStats.totalLength.mean))
		predictors["totalRot"] = (lambda dataset : (dataset.perfStats.totalRot.mean))
	if debugMode < 2:
		predictors = addGeometricalPredictors(predictors)
		predictors = addTopologicalPredictors(predictors)
		predictors = addVoronoiGraphPredictors(predictors)
		predictors = addVoronoiTraversalPredictors(predictors)
	return predictors

def fitModel(lm,xs,ys,numFolds):
	nsamples = len(xs)
	orig_xs = xs
	orig_ys = ys
	xs = np.array(xs).reshape(nsamples,1)
	ys = np.array(ys).reshape(nsamples,1)
	model = deepcopy(lm.fit(xs,ys))
	strategy = KFold(n_splits=numFolds,shuffle=True)
	rsquared = lm.score(xs,ys)
	mses = np.abs(cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='neg_mean_squared_error'))
	rsquareds = cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='r2')
	#plot
	y_pred = model.predict(xs)
	fig = plt.figure()
	plt.scatter(orig_xs, orig_ys,  color='black')
	plt.plot(orig_xs, y_pred, color='blue', linewidth=3)
	return model, np.sqrt(mses.sum()/numFolds), rsquareds.mean(), fig

def selectFeaturesToUse(featureString, debugMode):
	# fetch all possible predictors
	allPredictors = getPredictors(debugMode)
	usedPredictors = {}
	if featureString=='overrideAll':
		# we have to load all possible features
		usedPredictors = allPredictors
	elif featureString in allPredictors:
		# select a single feature from the dictionary
		usedPredictors[featureString] = allPredictors[featureString]
	else:
		print "The feature string you specified is neither an override option nor a valid predictor. Exiting."
		exit()
	return usedPredictors
	# in the end, we have to build a dictionary of features 

def rmse_cv(model,xs,ys,kf):
    rmse= np.sqrt(-cross_val_score(model, xs, ys, scoring="neg_mean_squared_error", cv = kf))
    return(rmse)

def ElasticNetTraining(xs, ys, featuresArray, numFolds, fsFolder, predictedFeature):
	print "Computing ElasticNet model for "+predictedFeature+"...",
	sys.stdout.flush()
	kf = RepeatedKFold(n_splits=numFolds, n_repeats=10)
	# first split training from testing
	x_train, x_test, y_train, y_test = train_test_split(xs,ys,test_size=0.2)
	# perform hyperparameter selection
	l1_ratios = [.1, .5, .7, .9, .95, .99, 1]
	alphas = [0.0001, 0.0003, 0.0005, 0.001, 0.003, 0.005, 0.01, 0.03, 0.05, 0.1, 0.3, 0.5, 1, 3, 5, 10, 30, 50, 100]
	# First we identify the best l1 ratio and alpha with cross validation (hyperparameters tuning)
	cv_elastic = [rmse_cv(linear_model.ElasticNet(alpha = alpha, l1_ratio=l1_ratio),x_train,y_train,kf).mean() 
            for (alpha, l1_ratio) in product(alphas, l1_ratios)]
	idx = list(product(alphas, l1_ratios))
	best_idx = np.argmin(cv_elastic)
	best_pair = idx[best_idx]
	best_alpha = best_pair[0]
	best_l1_ratio = best_pair[1]
	print "[DONE]"
	print "Best l1 ratio found is " + str(best_l1_ratio)
	print "Best alpha found is " + str(best_alpha)
	# Then we create the estimator with the hyperparameters identified by cross validation
	estimator = linear_model.ElasticNet(l1_ratio=best_l1_ratio,alpha=best_alpha)
	# We fit the final model on all data
	model = deepcopy(estimator.fit(xs,ys))
	# We retrieve the actually used features; however, the actual model uses all of them
	usedFeaturesIdx = [idx for idx,value in enumerate(estimator.coef_) if value != 0]
	usedFeatures = [feature for idx,feature in enumerate(featuresArray) if idx in usedFeaturesIdx]
	# We validate on the test set
	estimator.fit(x_train,y_train)
	y_test_pred = estimator.predict(x_test)
	mse = mean_squared_error(y_test,y_test_pred)
	rsquared = r2_score(y_test,y_test_pred)
	return model, usedFeatures, mse, rsquared	

def KBestFeatureSelection(xs, ys, featuresArray, numFolds, n_features, predictedFeature):
	print "Computing F-regression feature selection model for "+predictedFeature+" with "+str(n_features)+" features...",
	sys.stdout.flush()
	estimator = linear_model.LinearRegression()
	n_repeats = 100
	# first split training from testing
	x_train, x_test, y_train, y_test = train_test_split(xs,ys,test_size=0.2)
	# in order to properly perform feature selection, we must perform cross validation as the outer loop 
	selected_features_per_fold = np.empty([n_repeats*numFolds,len(featuresArray)])
	kf = KFold(n_splits=numFolds, shuffle=True)
	i = 0
	for r in range(0,n_repeats):
		for train_smaller, validation in kf.split(xs):
			x_train_smaller = xs[train_smaller]
			y_train_smaller = ys[train_smaller]
			x_validation = xs[validation]
			y_validation = ys[validation]
			# perform feature selection
			fs = SelectKBest(f_regression, k=n_features).fit(x_train_smaller, y_train_smaller)
			# take note of which features have been selected
			support = [1 if v else 0 for v in fs.get_support()]
			np.copyto(selected_features_per_fold[i], support)
			i+=1
	print "[DONE]"
	# now, we have to get the most voted k features
	selected_features_total = np.sum(selected_features_per_fold,axis=0)
	usedFeaturesIdx = np.sort(np.argpartition(selected_features_total, -n_features)[-n_features:])
	usedFeatures = [feature for idx,feature in enumerate(featuresArray) if idx in usedFeaturesIdx]
	# now we can train the final model and get a cv estimate of its performance
	xr = xs[:,usedFeaturesIdx]
	x_train = x_train[:,usedFeaturesIdx]
	x_test = x_test[:,usedFeaturesIdx]
	# We validate on the test set
	estimator.fit(x_train,y_train)
	y_test_pred = estimator.predict(x_test)
	mse = mean_squared_error(y_test,y_test_pred)
	rsquared = r2_score(y_test,y_test_pred)
	# Finally, we fit the final model on all data
	model = deepcopy(estimator.fit(xr,ys))
	return model, usedFeatures, mse, rsquared

def ParametrizedKBestFeatureSelection(xs, ys, featuresArray, numFolds, fsFolder, predictedFeature):
	# I want to explore how the cross-validated RMSE varies when increasing the number of top k features
	n_features = len(featuresArray)
	models = []
	xp = np.arange(start=1,stop=n_features+1,step=1)
	yp = np.empty(n_features)
	for k in xp:
		model, usedFeatures, rmse, r2 = KBestFeatureSelection(xs, ys, featuresArray, numFolds, k, predictedFeature)
		models.append((model, usedFeatures, rmse, r2))
		yp[k-1] = rmse
	fig = plt.figure()
	plt.xlabel("Number of features, in order of decreasing relevance")
	plt.ylabel("RMSE")
	plt.plot(xp,yp, 'b-')
	if not exists(join(fsFolder,predictedFeature)):
		makedirs(join(fsFolder,predictedFeature))
	fig.savefig(join(fsFolder,predictedFeature,"krmse.png"))
	plt.close(fig)
	saveCVKFoldFile(join(fsFolder,predictedFeature),models, numFolds)
	return getBestIndividualModel(models,hasFig=False)

def saveCVKFoldFile(path, models, numFolds):
	summaryFile = open(join(path, "summary.csv"), "w")
	summaryFile.write("n. features, avg "+str(numFolds)+"-fold RMSE, avg "+str(numFolds)+"-fold r^2, usedFeatures \n")
	models.sort(key=lambda x:x[2], reverse=False)
	for (model,usedFeatures,rmse,r2) in models:
		summaryFile.write(str(len(usedFeatures))+','+str(rmse)+','+str(r2)+','+'-'.join(usedFeatures)+'\n')
	summaryFile.close()

def performFeatureSelection(datasets,layoutFolder,fsFolder,predictedStats,predictedStatsAttrs,numFolds,predictors,function):
	attrStats = getAttrStats()
	# error stats
	models = {}
	nsamples = len(datasets)
	featuresArray = list(predictors.keys())
	xs = np.empty([nsamples,len(featuresArray)])
	ys = np.empty([nsamples,1])
	for eName, eLambda in predictedStats.iteritems():
		for aName, aLambda in predictedStatsAttrs.iteritems():
			for sName, sLambda in attrStats.iteritems():
				bestModel = None
				bestRMSE = float('inf')
				for i in range(0,nsamples):
					d = datasets[i]			
					ys[i][0] = sLambda(aLambda(eLambda(d)))
					for k in range(0,len(featuresArray)):
						pName = featuresArray[k]
						pLambda = predictors[featuresArray[k]]
						xs[i][k] = pLambda(d)
				predictedFeature = eName+"."+aName+"."+sName
				model, selectedFeatures, mse, r2 = function([xs, ys, featuresArray, numFolds, fsFolder, predictedFeature])
				models[predictedFeature] = (model, selectedFeatures, mse, r2)
	return models, featuresArray	

def performIndividualFeatureTraining(datasets,layoutFolder,predictedStats,predictedStatsAttrs,numFolds,estimator,predictors):
	attrStats = getAttrStats()
	totalPredictors = len(predictors.keys())
	# error stats
	models = {}
	for eName, eLambda in predictedStats.iteritems():
		for aName, aLambda in predictedStatsAttrs.iteritems():
			for sName, sLambda in attrStats.iteritems():
				print "Computing predictors for "+eName+"."+aName+"."+sName+"...",
				sys.stdout.flush()
				idx = 0
				models[eName+"."+aName+"."+sName] = []
				for pName, pLambda in predictors.iteritems():
					print str(round(idx/totalPredictors*100))+"%...",
					sys.stdout.flush()
					xs,ys = [], []
					for d in datasets:			
						if isdir(join(layoutFolder, d.name)):
							xs.append(pLambda(d))
							ys.append(sLambda(aLambda(eLambda(d))))
					model, rmse, r2, fig = fitModel(estimator,xs,ys,numFolds)
					models[eName+"."+aName+"."+sName].append((model, pName, rmse, r2, fig))
					idx += 1
				print "[DONE]"
	return models

''' Outline of the algorithm (TICK-TOCK mechanism):
# black == occupied, white == free
1) TICK phase: I "look around" the node where I'm currently standing with the find_nearest_node
function, looking for the nearest (euclidean distance) black pixel as that's the nearest frontier. Then, 
I apply the shortest_path algorithm to identify a set of nodes on the voronoi graph that lead me towards
the nearest frontier. 
2) TOCK phase: For each node on the shortest path, I apply a "line-of-sight-visiting-algorithm". That is, 
I look around them to retrieve all the black pixels that are within a certain (laser) distance and that
satisfy the constraints on the laser sensor field of view; for each of the identified black points, I ask
whether there are no other black pixels (obstacles) on the line joining it with the current
node on the shortest path, and if so it gets marked as 'seen' (i.e. colored white on the image).'''

''' Correction for negative angles '''
def correct_angle(angle):
	if angle < 0:
		angle += 2*np.pi
	return angle

''' Retrieves all pixels that are within a certain range from the current pixel and that
are within the simulated field of view of the laser scanner. '''
def retrieveNearbyPixels(image, currentPixel, previousPixel, laserLength, laserFOV):
	# Retrieve all black pixels (black = occupied)
	black_pixels = np.argwhere(image == 0)
	# Compute the orientation of the robot
	ref_angle = math.atan2(currentPixel[0]-previousPixel[0], currentPixel[1]-previousPixel[1])
	# Compute the distance between the current pixel and every other black pixel
	distances = np.sqrt((black_pixels[:,0] - currentPixel[0]) ** 2 + (black_pixels[:,1] - currentPixel[1]) ** 2)
	# Compute the relative orientation 
	angles = np.arctan2(black_pixels[:,0] - currentPixel[0], black_pixels[:,1]-currentPixel[1])
	lgt = len(distances)
	# Return only those pixels that are within the laser range and field of view
	indices = [i for i in range(0, lgt) if distances[i] < laserLength and math.fabs(math.atan2(math.sin(angles[i]-ref_angle),math.cos(angles[i]-ref_angle)))<=laserFOV/2] 
	return black_pixels[indices]

''' Retrieves all pixels that are visible from the current robot location and orientation.
A pixel is considered to be visible if three conditions hold:
- it is within the laser range
- it is within the laser field of view
- there are no other black pixels on the line connecting it to the current robot location '''
def retrieveVisiblePixels(image, gtImage, totalNodes, currentPixel, previousPixel, laserLength, laserFOV):
	height, width = image.shape
	# Retrieve candidate pixels 
	nearbyPixels = retrieveNearbyPixels(image, currentPixel, previousPixel, laserLength, laserFOV)
	visiblePixels = []
	# If two black pixels are visible from each other, it means no other obstacle (black pixel) stands
	# between them
	for p in nearbyPixels:
		pixelsAlongLine = createLineIterator([currentPixel[1],currentPixel[0]],[p[1],p[0]],gtImage)
		black_pixels = np.argwhere(pixelsAlongLine == 0)
		if len(black_pixels)==0:
			visiblePixels.append(p)
	return visiblePixels

def markVisiblePixelsAsVisited(image, visiblePixels):
	for p in visiblePixels:
		image[p[0],p[1]] = 127

def markVisibleNodesAsVisited(VG, visibleNodes):
	nseen = 0 
	for n in visibleNodes:
		if VG.node[n]['seen'] == False:
			VG.node[n]['seen'] = True
			nseen+=1
	return nseen

def pixelsToNodes(pixels, voronoiNodesMap, height):
	nodes = []
	for p in pixels:
		nodes.append(voronoiNodesMap[height-p[0],p[1]])
	return nodes

''' Retrieve pixels that are visible in line-of-sight given the current robot location and orientation;
then, set them to gray, set the corresponding nodes as seen and return them.'''
def lineOfSight(VG, image, gtImage, totalNodes, currentPixel, previousPixel, voronoiNodesMap, voronoiNodesReverseMap, laserLength, laserFOV):
	height, width = image.shape
	visiblePixels = retrieveVisiblePixels(image, gtImage, totalNodes, currentPixel, previousPixel, laserLength, laserFOV)
	visibleNodes = pixelsToNodes(visiblePixels, voronoiNodesMap, height)
	markVisiblePixelsAsVisited(image, visiblePixels)
	nseen = markVisibleNodesAsVisited(VG, visibleNodes)
	return visibleNodes, nseen

''' Return the nearest frontier, in euclidean distance, from the current robot location.''' 
def retrieveNearestFrontier(img, currentPixel):
    black_pixels = np.argwhere(img == 0)
    distances = np.sqrt((black_pixels[:,0] - currentPixel[0]) ** 2 + (black_pixels[:,1] - currentPixel[1]) ** 2)
    nearest_index = np.argmin(distances)
    return black_pixels[nearest_index]

def initNodeVisitedStatus(VG):
	for n in VG.nodes():
		VG.node[n]['seen'] = False
		VG.node[n]['nvisits'] = 0

''' Explore the voronoi graph; return the total amount of travelled distance and the sum of the visits
of the top N visited nodes.''' 
def exploreVoronoiGraph(VG, image, gtImage, start, voronoiNodesMap, voronoiNodesReverseMap, laserLength, laserFOV, minRotDistance, scale):
	laserLength *= scale
	minRotDistance *= scale
	# set every node as 'not seen' and with zero visits
	initNodeVisitedStatus(VG)
	# initialize counting variables
	height, width = image.shape
	totalNodes = len(VG.nodes())
	currentPixel = start
	currentAnglePixel = currentPixel
	previousPixel = (currentPixel[0]+1,currentPixel[1])
	numSeenNodes, partialDistance, totalDistance, partialAngle, totalAngle, robotAngle = 0, 0, 0, 0, 0, 0
	# line-of-sight: identify and mark as 'seen' the pixels that are visible from the current location
	visibleNodes, nseen = lineOfSight(VG, image, gtImage, totalNodes, currentPixel, previousPixel, voronoiNodesMap, voronoiNodesReverseMap, laserLength, laserFOV)
	numSeenNodes += nseen
	# we proceed until we've seen every single node of the graph 
	while numSeenNodes < totalNodes:
		print str(round(float(numSeenNodes)/totalNodes*100))+"%...",
		sys.stdout.flush()
		# and until then, we keep looking for the next frontier (shortest euclidean distance from current location)
		nearestPixel = retrieveNearestFrontier(image, currentPixel)
		nearestNode = voronoiNodesMap[height-nearestPixel[0], nearestPixel[1]]
		currentNode = voronoiNodesMap[height-currentPixel[0], currentPixel[1]]
		# then, we follow the shortest path that connects our current location to the identified frontier
		shortest_path = nx.shortest_path(VG, currentNode, nearestNode)
		for n in shortest_path:
			# each node of the path gets visited and its neighboring nodes in line-of-sight are marked as 'seen'
			newPixel = (height-voronoiNodesReverseMap[n][0],voronoiNodesReverseMap[n][1])
			newNode = n 
			# increase the total travelled distance by the amount joining two consecutive nodes on the path
			travelledDistance = node_distance(VG,currentNode,newNode)
			partialDistance += travelledDistance
			totalDistance += travelledDistance
			if partialDistance > minRotDistance:
				partialAngle = math.atan2(newPixel[0]-currentAnglePixel[0], newPixel[1]-currentAnglePixel[1])
				totalAngle += math.fabs(math.atan2(math.sin(partialAngle-robotAngle),math.cos(partialAngle-robotAngle)))
				robotAngle = partialAngle
				currentAnglePixel = newPixel
				partialDistance = 0
			previousPixel = currentPixel
			previousNode = currentNode
			currentPixel = newPixel
			currentNode = newNode
			visibleNodes, nseen = lineOfSight(VG, image, gtImage, totalNodes,currentPixel, previousPixel, voronoiNodesMap, voronoiNodesReverseMap, laserLength, laserFOV)
			# add to the number of seen nodes the new ones we have actually seen in line of sight
			numSeenNodes += nseen
			# and increase the number of times this current node has been visited (currently unused)
			VG.node[n]['nvisits'] += 1
		currentPixel = nearestPixel
	return totalDistance/scale, totalAngle

def createVoronoiGraphFromImage(imagePath, worldPath):
	print "Computing Voronoi graph...",
	sys.stdout.flush()
	image = cv2.imread(imagePath,cv2.IMREAD_GRAYSCALE)
	height, width = image.shape
	_,thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
	# Dilate
	kernel = np.ones((5,5),np.uint8)
	dilation = cv2.dilate(thresh,kernel,iterations = 1)
	# Convert to skimage
	dilation[dilation == 255] = 1
	# Skeletonize
	skel = skeletonize(dilation)
	# Convert back to CV2
	skel[skel == 1] = 255
	skel[skel < 1] = 0
	skel = img_as_ubyte(skel)
	# Invert again
	_,image = cv2.threshold(skel,127,255,cv2.THRESH_BINARY_INV)
	robotX, robotY, scale = retrieveExplorationStartingPoint(worldPath, width, height)
	voronoiNodesMap = {}
	voronoiNodesReverseMap = {}
	idx = 0
	neighboringNodes = []
	for y in range(0, height):
		for x in range(0, width):
			if image[y,x]==0: # we found a cell of the voronoi graph
				voronoiNodesMap[(height-y,x)] = idx
				voronoiNodesReverseMap[idx] = (height-y,x)
				idx += 1
	for k,v in voronoiNodesMap.iteritems():
		for r in range(max(0,height-k[0]-1),min(height,height-k[0]+1)+1):
			for c in range(max(0,k[1]-1),min(width,k[1]+1)+1):
				if not(r==height-k[0] and c==k[1]) and image[r,c]==0: # it's a neighbor!
					neighboringNodes.append((voronoiNodesMap[k],voronoiNodesMap[(height-r,c)]))
	# create the graph
	G=nx.Graph()
	for i in range(0, idx):
		G.add_node(i)
	G.add_edges_from(neighboringNodes,weight=1)
	# create a dictionary containing the nodes positions (i.e. their representative points)
	pos = {}
	for i in range(0, idx):
		pos[i] = (voronoiNodesReverseMap[i][1],voronoiNodesReverseMap[i][0])
	# set the nodes positions
	for n, p in pos.iteritems():
		G.node[n]['pos'] = p
	print "[DONE]"
	# Simplify graph by removing all 'passthrough' nodes
	print "Nodes before pass-through removal: "+str(len(G.nodes()))
	removeFlowThroughNodes(G, image)
	print "Nodes after pass-through removal: "+str(len(G.nodes()))	
	# necessary to filter out unreachable rooms
	Gc = max(nx.connected_component_subgraphs(G), key=len)
	return Gc

def loadVoronoiGraph(datasetName, voronoiPath, worldPath):
	pickleFile = join(voronoiPath, "pickle",datasetName)+"_voronoi.pickle"
	imageFile = join(voronoiPath, "images",datasetName)+"_voronoi.png"
	if exists(pickleFile):
		print "Loading Voronoi graph... [DONE]"
		Gc = nx.read_gpickle(pickleFile)
	else:
		Gc = createVoronoiGraphFromImage(imageFile, worldPath)
		nx.write_gpickle(Gc, pickleFile)
	return Gc

def processVoronoiGraph(VG, worldPath, gtImagePath, laserRange, laserFOV, minRotDistance):
	print "Processing...",
	sys.stdout.flush()
	gtImage = cv2.imread(gtImagePath,cv2.IMREAD_GRAYSCALE)
	height, width = gtImage.shape
	robotX, robotY, scale = retrieveExplorationStartingPoint(worldPath, width, height)
	voronoiNodesReverseMap = {}
	voronoiNodesMap = {}
	img = np.full((height, width), 255, np.uint8)
	for n in VG.nodes():
		voronoiNodesReverseMap[n] = VG.node[n]['pos'][1], VG.node[n]['pos'][0]
	for k,v in voronoiNodesReverseMap.iteritems():
		voronoiNodesMap[v] = k
		img[height-v[0],v[1]] = 0
	# we also need to figure out which node is the closest to the starting point of the exploration
	nearestPixel = find_nearest_node(img, robotX, robotY)
	voronoiCenter = voronoiNodesMap[height-nearestPixel[0],nearestPixel[1]]
	totalDistance, totalAngle = exploreVoronoiGraph(VG, img, gtImage, nearestPixel, voronoiNodesMap, voronoiNodesReverseMap, laserRange, laserFOV, minRotDistance, scale)
	print "[DONE]"
	print "Voronoi traversal distance: "+str(totalDistance)
	print "Voronoi traversal rotation: "+str(totalAngle)
	return voronoiCenter, totalDistance ,totalAngle

def node_distance(G,u,v): 
	return np.sqrt((G.node[u]['pos'][0]-G.node[v]['pos'][0])**2+(G.node[u]['pos'][1]-G.node[v]['pos'][1])**2)

def node_angle(previousPixel, currentPixel, newPixel):
	# Compute the orientation of the robot
	ref_angle = correct_angle(math.atan2(currentPixel[0]-previousPixel[0], currentPixel[1]-previousPixel[1]))
	# Compute the absolute orientation between the new pixel and the current pixel
	angle = correct_angle(math.atan2(newPixel[0]-currentPixel[0], newPixel[1]-currentPixel[1]))
	# Compute the relative orientation between the new pixel and the current pixel, accounting for 
	# the initial orientation of the robot (between 0 and pi, always assume smallest rotation)
	angle = (np.pi - math.fabs(math.fabs(ref_angle - angle) - np.pi))	
	return angle

def find_nearest_node(img, robotX, robotY):
    black_pixels = np.argwhere(img == 0)
    distances = np.sqrt((black_pixels[:,0] - robotY) ** 2 + (black_pixels[:,1] - robotX) ** 2)
    nearest_index = np.argmin(distances)
    return black_pixels[nearest_index]

def retrieveExplorationStartingPoint(worldPath, width, height):
	worldFile = open(worldPath,'r')
	outputContent = []
	lines = worldFile.readlines()
	# at the 17th we have the world dimension, at the 18th the robot position
	worldSizeLine = 16
	robotPoseLine = 24
	# retrieve world size in meters
	worldSize = lines[worldSizeLine].split(' ')
	worldWidth = float(worldSize[3][1:])
	worldHeight = float(worldSize[4])
	# retrieve robot pose in meters
	robotPose = lines[robotPoseLine].split(' ')
	robotXinMeters = float(robotPose[3][1:])
	robotYinMeters = float(robotPose[4])
	# perform conversion to pixels
	robotX = int((robotXinMeters+worldWidth/2) * width / worldWidth)
	robotY = int((worldHeight/2-robotYinMeters) * height / worldHeight)
	scale = width / worldWidth # pixels per meter
	worldFile.close()
	return robotX, robotY, scale

def get_bifurcation_points(graph):
	bif = []
	for n in graph.nodes():
		if len(graph.neighbors(n))>2:
			bif.append(n)
	return bif

def get_terminal_points(graph):
	term = []
	for n in graph.nodes():
		if len(graph.neighbors(n))==1:
			term.append(n)
	return term

def lineBroken(p,delta,image):
	height, width = image.shape
	empty = True
	x = p[0]-delta
	while (x <= p[0]+delta) and empty:
		y = p[1]-delta
		while (y <= p[1]+delta) and empty:
			if image[height-int(y),int(x)]==0:
				empty = False
			y+=1
		x+=1
	return empty

def removeFlowThroughNodes(G, image):
	for n in G.nodes():
		neighbors = G.neighbors(n)
		if len(neighbors) == 2:
			# let's also check the angle before removing
			n1 = neighbors[0]
			n2 = neighbors[1]
			angle = correct_angle(math.atan2(G.node[n2]['pos'][1]-G.node[n1]['pos'][1], G.node[n2]['pos'][0]-G.node[n1]['pos'][0]))
			nextp = [G.node[n2]['pos'][0]+5*math.cos(angle),G.node[n2]['pos'][1]+5*math.sin(angle)]
			prevp = [G.node[n1]['pos'][0]-5*math.cos(angle),G.node[n1]['pos'][1]-5*math.sin(angle)]
			if not lineBroken(nextp,1,image) and not lineBroken(prevp,1,image):
				w1 = G.get_edge_data(n,n1)['weight']
				w2 = G.get_edge_data(n,n2)['weight']
				G.remove_node(n)
				G.add_edge(n1, n2,weight=w1+w2)

def setVoronoiTraversalProperties(myDataset, voronoiCenter, voronoiDistance, voronoiRotation):
	myDataset.voronoiCenter = voronoiCenter
	myDataset.voronoiDistance = voronoiDistance
	myDataset.voronoiRotation = voronoiRotation
	myDataset.voronoiStats = voronoiStats	

def setupFeatureSelection(datasets,layoutFolder,fsFolder,numFolds,predictors):
	errorTypes = getErrorTypes()
	runStats = getRunStats()
	errorAttrs = getErrorAttrs()
	function = (lambda paramList: ParametrizedKBestFeatureSelection(*paramList))
	models, _ = performFeatureSelection(datasets,layoutFolder,fsFolder,errorTypes,errorAttrs,numFolds,predictors,function)
	return models

def setupIndividualFeatureTraining(datasets,layoutFolder,numFolds,predictors):
	errorTypes = getErrorTypes()
	runStats = getRunStats()
	errorAttrs = getErrorAttrs()
	estimator = linear_model.LinearRegression()
	models = performIndividualFeatureTraining(datasets,layoutFolder,errorTypes,errorAttrs,numFolds,estimator,predictors)
	bestModels = getBestModels(models)
	return models, bestModels

def setupElasticNetTraining(datasets,layoutFolder,fsFolder,numFolds,predictors):
	errorTypes = getErrorTypes()
	runStats = getRunStats()
	errorAttrs = getErrorAttrs()
	function = (lambda paramList: ElasticNetTraining(*paramList))
	models, featuresArray = performFeatureSelection(datasets,layoutFolder,fsFolder,errorTypes,errorAttrs,numFolds,predictors,function)
	return models, featuresArray

def getBestModels(models):
	bestModels = {}
	for predictedFeature, availableModels in models.iteritems():
		bestModel, bestName, bestRMSE, bestR2, fig = getBestIndividualModel(availableModels, hasFig=True)
		bestModels[predictedFeature] = (bestModel, bestName, bestRMSE, bestR2, fig)
	return bestModels

def getBestIndividualModel(models, hasFig=False):
	bestModel = None
	bestName = ''
	bestRMSE = float('inf')
	bestR2 = float('-inf')
	bestFig = None
	if hasFig:
		for model, name, rmse, r2, fig in models:
			if rmse < bestRMSE:
				bestModel = model
				bestName = name
				bestRMSE = rmse
				bestR2 = r2
				bestFig = fig
		return bestModel, bestName, bestRMSE, bestR2, bestFig
	else:
		for model, name, rmse, r2 in models:
			if rmse < bestRMSE:
				bestModel = model
				bestName = name
				bestRMSE = rmse
				bestR2 = r2
		return bestModel, bestName, bestRMSE, bestR2

def saveVoronoiCSV(path, datasets):
	if not exists(path):
			makedirs(path)
	summaryFile = open(join(path, "stats.csv"), "w")
	summaryFile.write("dataset, Voronoi distance, Voronoi rotation, totalLen, totalRot, transError.mean.mean, transError.mean.std, rotError.mean.mean, rotError.mean.std\n")
	for d in datasets:
		summaryFile.write(d.name+','+str(d.voronoiDistance)+','+str(d.voronoiRotation)+','+str(d.perfStats.totalLength.mean)+','+str(d.perfStats.totalRot.mean)+','+str(d.perfStats.transError.mean.mean)+','+str(d.perfStats.transError.mean.std)+','+str(d.perfStats.rotError.mean.mean)+','+str(d.perfStats.rotError.mean.std)+'\n')
	summaryFile.close()

def checkPredictors(predictorsList, usedPredictors):
 	isUsed = False
 	for predictor in predictorsList:
 	 	if predictor in usedPredictors:
 	 	 	isUsed = True
 	return isUsed

def getUsedPredictors(useMode,debugMode,featureString):
	# select regressors to be used
	if useMode=='linear_regression':
		usedPredictors = selectFeaturesToUse(featureString, debugMode)
	else:
		usedPredictors = getPredictors(debugMode)
	return usedPredictors

def analyzeDatasets(runsFolder, layoutFolder, voronoiFolder, worldFolder, modelsFolder, useMode, featureString, numFolds, laserRange, laserFOV, minRotDistance, debugMode):
	datasets = []
	usedPredictors = getUsedPredictors(useMode,debugMode,featureString)
	# load dataset runs
	for f in listdir(runsFolder):
		if isdir(join(runsFolder, f)):
			datasets.append(loadDataset(f, runsFolder))
	# load dataset properties (layout, voronoi graph...)
	for d in datasets:
		if checkPredictors(getGeometricalPredictors(), usedPredictors.keys()) or checkPredictors(getTopologicalPredictors(), usedPredictors.keys()):
			print "Computing geometrical and topological features...",
			sys.stdout.flush()
			d.geometry, d.topology, d.topologyStats = loadGeometry(join(layoutFolder, d.name, d.name)+".xml")	
			print "[DONE]"
		if checkPredictors(getVoronoiGraphPredictors(), usedPredictors.keys()) or checkPredictors(getVoronoiTraversalPredictors(), usedPredictors.keys()):
			print "Processing Voronoi graph of "+d.name+"."
			worldFile = join(worldFolder, d.name)+".world"
			gtImageFile = join(worldFolder, d.name)+".png"
			d.voronoi = loadVoronoiGraph(d.name, voronoiFolder, worldFile)
			if checkPredictors(getVoronoiTraversalPredictors(), usedPredictors.keys()):
				d.voronoiCenter, d.voronoiDistance, d.voronoiRotation = processVoronoiGraph(d.voronoi, worldFile, gtImageFile, laserRange, laserFOV, minRotDistance)
			if checkPredictors(getVoronoiGraphPredictors(), usedPredictors.keys()):
				print "Computing Voronoi graph stats...",
				sys.stdout.flush()
				d.voronoiStats = GraphStats(d.voronoi)
				print "[DONE]"
	# select whether we should perform feature selection or use single features 	
	if useMode=='feature_selection':
		# in this mode, we first identify, for each subset of k features, which are the k features that correlate
		# best with our data; then we identify the best number of features k 
		fsFolder = join(modelsFolder,'LinearRegression','models','fs')
		models = setupFeatureSelection(datasets,layoutFolder,fsFolder,numFolds,getPredictors(debugMode))
		saveFSModels(models,fsFolder,numFolds)
	elif useMode=='linear_regression':
		# in this mode, we directly fit a simple non-penalized linear regression model on the given features
		models,bestModels = setupIndividualFeatureTraining(datasets,layoutFolder,numFolds,usedPredictors)
		saveVoronoiCSV(join(modelsFolder,'LinearRegression','models','individual'), datasets)
		saveIndividualModels(models, join(modelsFolder,'LinearRegression','models','individual'), numFolds)
		saveBestModels(bestModels,join(modelsFolder,'LinearRegression','models','best_individual'), numFolds)
	elif useMode=='elastic_net':
		# in this mode, we use cross validation to find the best hyperparameters of an elastic net model
		fsFolder = join(modelsFolder,'ElasticNet','models','fs')
		models, featuresArray = setupElasticNetTraining(datasets,layoutFolder,fsFolder,numFolds,getPredictors(debugMode))
		saveElasticNetModels(models,fsFolder,numFolds, featuresArray)	

def saveSummaryFile(path, corrStats, numFolds):
	summaryFile = open(join(path, "summary.csv"), "w")
	summaryFile.write("predictedFeature, predictor, avg "+str(numFolds)+"-fold RMSE, avg "+str(numFolds)+"-fold r^2 \n")
	corrStats.sort(key=lambda x:x[0], reverse=False)
	for elem in corrStats:
		summaryFile.write(elem[0]+','+elem[1]+','+str(elem[2])+','+str(elem[3])+'\n')
	summaryFile.close()

def saveBestModels(models, path, numFolds):
	corrStats = []
	for predictedFeature, (model, name, rmse, r2, fig) in models.iteritems():
		if not exists(join(path,predictedFeature)):
			makedirs(join(path,predictedFeature))
		joblib.dump(model, join(path,predictedFeature,name)+'.mdl')
		corrStats.append((predictedFeature,name,rmse,r2))
		fig.savefig(join(path,predictedFeature,name)+".pdf", bbox_inches='tight')
	saveSummaryFile(path,corrStats, numFolds)

def saveIndividualModels(models,path, numFolds):
	corrStats = []
	for predictedFeature, modelList in models.iteritems():
		if not exists(join(path,predictedFeature)):
			makedirs(join(path,predictedFeature))
		for model, name, rmse, r2, fig in modelList:
			joblib.dump(model, join(path,predictedFeature,name)+'.mdl')
			corrStats.append((predictedFeature,name,rmse,r2))
			fig.savefig(join(path,predictedFeature,name)+".pdf", bbox_inches='tight')
	saveSummaryFile(path,corrStats, numFolds)

def saveFSModels(models, path, numFolds):
	corrStats = []
	for predictedFeature, (model, usedFeatures, rmse, r2) in models.iteritems():
		if not exists(join(path,predictedFeature)):
			makedirs(join(path,predictedFeature))
		joblib.dump(model, join(path,predictedFeature,'model')+'.mdl')
		corrStats.append((predictedFeature,';'.join(usedFeatures),rmse,r2))
	saveSummaryFile(path,corrStats, numFolds)

def saveElasticNetModels(models, path, numFolds, allFeatures):
	corrStats = []
	for predictedFeature, (model, usedFeatures, rmse, r2) in models.iteritems():
		if not exists(join(path,predictedFeature)):
			makedirs(join(path,predictedFeature))
		joblib.dump(model, join(path,predictedFeature,'model')+'.mdl')
		corrStats.append((predictedFeature,';'.join(usedFeatures),rmse,r2))
	corrStats.append(('allFeatures',';'.join(allFeatures),'',''))
	saveSummaryFile(path,corrStats, numFolds)


def loadModels(path):
	models = {}
	for predictedFeature in listdir(path):
		if isdir(join(path,predictedFeature)):
			models[predictedFeature] = {}
			for f in listdir(join(path,predictedFeature)):
				if isfile(join(path,predictedFeature,f)) and f[-3:]=="mdl":
					modelName = f[:-4]
					models[predictedFeature][modelName]=joblib.load(join(path,predictedFeature,f))
	return models	

def createLineIterator(P1, P2, img):
	"""
	Produces and array that consists of the coordinates and intensities of each pixel in a line between two points

	Parameters:
	-10-P1: a numpy array that consists of the coordinate of the first point (x,y)
	-10-P2: a numpy array that consists of the coordinate of the second point (x,y)
	-10-img: the image being processed

    Returns:
	-10-it: a numpy array that consists of the coordinates and intensities of each pixel in the radii (shape: [numPixels, 3], row = [x,y,intensity])     
	"""
	#define local variables for readability
	imageH = img.shape[0]
	imageW = img.shape[1]
	P1X = P1[0]
	P1Y = P1[1]
	P2X = P2[0]
	P2Y = P2[1]

	#difference and absolute difference between points
	#used to calculate slope and relative location between points
	dX = P2X - P1X
	dY = P2Y - P1Y
	dXa = np.abs(dX)
	dYa = np.abs(dY)

	#predefine numpy array for output based on distance between points
	itbuffer = np.empty(shape=(np.maximum(dYa,dXa),3),dtype=np.float32)
	itbuffer.fill(np.nan)

	#Obtain coordinates along the line using a form of Bresenham's algorithm
	negY = P1Y > P2Y
	negX = P1X > P2X
	if P1X == P2X: #vertical line segment
		itbuffer[:,0] = P1X
		if negY:
			itbuffer[:,1] = np.arange(P1Y - 1,P1Y - dYa - 1,-1)
		else:
			itbuffer[:,1] = np.arange(P1Y+1,P1Y+dYa+1)              
	elif P1Y == P2Y: #horizontal line segment
		itbuffer[:,1] = P1Y
		if negX:
			itbuffer[:,0] = np.arange(P1X-1,P1X-dXa-1,-1)
		else:
			itbuffer[:,0] = np.arange(P1X+1,P1X+dXa+1)
	else: #diagonal line segment
		steepSlope = dYa > dXa
		if steepSlope:
			slope = dX.astype(np.float32)/dY.astype(np.float32)
			if negY:
				itbuffer[:,1] = np.arange(P1Y-1,P1Y-dYa-1,-1)
			else:
				itbuffer[:,1] = np.arange(P1Y+1,P1Y+dYa+1)
			itbuffer[:,0] = (slope*(itbuffer[:,1]-P1Y)).astype(np.int) + P1X
		else:
			slope = dY.astype(np.float32)/dX.astype(np.float32)
			if negX:
				itbuffer[:,0] = np.arange(P1X-1,P1X-dXa-1,-1)
			else:
				itbuffer[:,0] = np.arange(P1X+1,P1X+dXa+1)
			itbuffer[:,1] = (slope*(itbuffer[:,0]-P1X)).astype(np.int) + P1Y

	#Remove points outside of image
	colX = itbuffer[:,0]
	colY = itbuffer[:,1]
	itbuffer = itbuffer[(colX >= 0) & (colY >=0) & (colX<imageW) & (colY<imageH)]

	#Get intensities from img ndarray
	itbuffer[:,2] = img[itbuffer[:,1].astype(np.uint),itbuffer[:,0].astype(np.uint)]

	return itbuffer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is the main tool of the RPPF. Its task is to analyze the error data of the different runs of the training datasets, correlate it with properties extracted from such datasets, build a prediction model and use it to predict the error data of the desired test datasets. Please refer to the wiki for extended documentation.')
    parser.add_argument('runs_folder',help='the folder in which all the training datasets and their respective runs are stored')
    parser.add_argument('layouts_folder',help='the folder in which the layout information of each training dataset, as extracted by the Layout Extractor, is stored')
    parser.add_argument('voronoi_folder',help='the folder in which the data related to the voronoi graph of each training dataset, as extracted by the Voronoi Extractor, is stored')
    parser.add_argument('world_folder',help='the folder in which the Stage data of each training dataset, as used to perform the Stage simulations, is stored')
    parser.add_argument('models_folder',help='the output folder in which the tool stores the trained models')
    parser.add_argument('--n_folds', action='store', default=5, help='specifies the k number of folds of k-fold cross validation; default is 5')
    parser.add_argument('--laser_range', action='store', default=30, help='specifies the maximum range in meters of the virtual laser; default is 30')
    parser.add_argument('--laser_fov', action='store', default=270, help='specifies the field of view in degrees of the virtual laser; default is 270')
    parser.add_argument('--min_rotation_distance', action='store', default=0.5, help='specifies the minimum distance between two nodes for the computation of the travelled rotation; default is 0.5')
    parser.add_argument('--linear_regression', dest='regression_technique',action='store_const',const='linear_regression', help='uses the linear regression technique for learning')
    parser.add_argument('--feature_selection', dest='regression_technique',action='store_const',const='feature_selection', help='uses the feature selection technique for learning')
    parser.add_argument('--elastic_net', dest='regression_technique',action='store_const',const='elastic_net', help='uses the ElasticNet regularized regression technique for learning; this is the default behavior')
    parser.add_argument('--predictor',action='store',default='overrideAll', help='specifies the predictor to be used with the linear regression machine learning technique; default is "overrideAll", which trains all possible predictors')
    parser.add_argument('--debug_mode',action='store',default=0,help='specifies whether the true trajectory length and true trajectory rotation features should be used. 0 disables them, 1 enables them in addition to the other features, 2 enables them with all other features disabled (default is 0)')
    args = parser.parse_args()
    regression_technique = args.regression_technique
    if regression_technique is None:
        print 'You must specify a regression technique via --linear_regression, --feature_selection or --elastic_net. Exiting.'
    else:
        analyzeDatasets(args.runs_folder,args.layouts_folder,args.voronoi_folder,args.world_folder,args.models_folder, args.regression_technique, args.predictor, int(args.n_folds), args.laser_range, args.laser_fov*np.pi/180, args.min_rotation_distance, args.debug_mode)
    
