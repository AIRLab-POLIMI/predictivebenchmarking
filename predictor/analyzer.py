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
from sklearn.model_selection import KFold, RepeatedKFold, RepeatedStratifiedKFold, cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.decomposition import PCA
from sklearn import preprocessing, feature_selection
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression, RFECV, RFE
from shapely.geometry import Polygon, Point
from skimage.morphology import skeletonize
from skimage import img_as_ubyte
from copy import deepcopy
from itertools import product

''' Dataset Analyzer 
This script essentially performs the following operations:
1) collect, for each dataset, the SLAM performances as computed by the metricEvaluator over all the runs
2) summarize them with several statistics (mean and std of mean, std, number of samples...)
3) load the corresponding layout reconstruction XML and extract relevant features for the analysis
4) compute the topological graph and extract relevant features for the analysis
5) correlate 
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
		print errorFile
		raise IOError('Error file '+errorFile+ ' not found.')

def extractTimestampedPose(words):
	pose = dict()
	pose["t"] = float(words[0])
	pose["x"] = float(words[1])
	pose["y"] = float(words[2])
	return pose

def extractRunStatsFromGTLog(gtLog):
	if exists(gtLog):
		file = open(gtLog,'r')
		first = True
		prevPose = extractTimestampedPose([0]*3)
		totalLength = 0
		for line in file:
			words = line.split(' ')
			if first is True:
				first = False
				prevPose = extractTimestampedPose(words)
			else:
				curPose = extractTimestampedPose(words)
				totalLength += math.sqrt(math.pow(curPose["x"]-prevPose["x"],2)+math.pow(curPose["y"]-prevPose["y"],2))
				prevPose = curPose
		totalTime = float(line.split(' ')[0])
		return totalTime, totalLength
	else:
		raise IOError('Ground Truth log '+gtLog+' not found.')

def loadDatasetRun(datasetRunPath,datasetName):
	# for the specified dataset, load the metricEvaluator errors of that run
	try:
		tstats = extractRunStatsFromErrorFile(join(datasetRunPath+'/Errors/RE/T.errors'))
		rstats = extractRunStatsFromErrorFile(join(datasetRunPath+'/Errors/RE/R.errors'))
		totalTime, totalLength = extractRunStatsFromGTLog(join(datasetRunPath,datasetName)+'.log')
	except IOError as err:
		raise RuntimeError("Error while loading the dataset runs! Trouble at "+join(datasetRunPath,datasetName))
	# if we are here, we successfully loaded the error stats from file
	myRun = Run(tstats,rstats,totalTime,totalLength)
	#print myRun
	return myRun

def loadDatasetRuns(runsFolder, datasetName):
	# loads all the runs of the specified dataset
	runs = []
	datasetPath = join(runsFolder,datasetName)
	for r in listdir(datasetPath):
		if r[:3]=="run":
			runs.append(loadDatasetRun(join(datasetPath,r),datasetName))
	return runs
		
def reject_outliers(data, m = 2.):
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return data[s<m]

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
	''' For each run, add the mean and standard deviation of the selected error type, and the number
	of samples, to a list '''
	for r in runs:
		totalTimesList.append(r.totalTime)
		totalLengthsList.append(r.totalLength)
	''' Convert the lists to numpy arrays '''
	totalTimesArray = np.array(totalTimesList)
	totalLengthsArray = np.array(totalLengthsList)
	''' For each of them compute mean and standard deviation '''
	totalTime = Stats(totalTimesArray.mean(), totalTimesArray.std())
	totalLength = Stats(totalLengthsArray.mean(), totalLengthsArray.std())
	# build an errorStats object and return it
	return totalTime, totalLength

def computePerformanceStats(runs):
	transErrorStats = computeErrorStats(runs, errorType="trans")
	rotErrorStats = computeErrorStats(runs, errorType="rot")
	totalTime, totalLength = computeRunStats(runs)
	return PerfStats(transErrorStats,rotErrorStats,totalTime,totalLength)

def loadGeometry(myDataset, xmlFile):
	# load and parse the xml of the layout
	rooms, connectedRooms, boundingPolygon, scalingFactor = xmlutil.loadXML(xmlFile)
	datasetGeometry = Geometry(rooms, boundingPolygon, scalingFactor)
	myDataset.geometry = datasetGeometry
	# create the topological graph
	G=nx.Graph()
	#for i,s in enumerate(rooms):
	#	G.add_node(i)
	G.add_edges_from(connectedRooms)
	Gc = max(nx.connected_component_subgraphs(G), key=len)
	myDataset.topology = Gc
	myDataset.topologyStats = GraphStats(Gc)

def loadDataset(datasetName, runsFolder):
	# load the runs
	print "Loading runs of "+datasetName
	runs = loadDatasetRuns(runsFolder, datasetName)
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

def getPredictors():
	predictors = dict()
	#predictors["totalTime"] = (lambda dataset: (dataset.perfStats.totalTime.mean))
	#predictors["totalLength"] = (lambda dataset : (dataset.perfStats.totalLength.mean))
	predictors["area"] = (lambda dataset: (dataset.geometry.shape.area))
	predictors["perimeter"] = (lambda dataset: (dataset.geometry.shape.perimeter))
	predictors["wallRatio"] = (lambda dataset: (dataset.geometry.shape.wallRatio))
	predictors["numRooms"] = (lambda dataset: (len(dataset.geometry.rooms)))
	predictors["avgRoomArea"] = (lambda dataset: np.array([r.shape.area for r in dataset.geometry.rooms]).mean()**2)
	predictors["avgRoomPerimeter"] = (lambda dataset: np.array([r.shape.perimeter for r in dataset.geometry.rooms]).mean()**2)
	predictors["avgRoomWallRatio"] = (lambda dataset: np.array([r.shape.wallRatio for r in dataset.geometry.rooms]).mean()**2)
	predictors["roomPerimeter"] = 	(lambda dataset: np.array([r.shape.perimeter for r in dataset.geometry.rooms]).sum())
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
	predictors["entropy"] = (lambda dataset: dataset.entropy)
	return predictors

def getDummyLambdaStats():
	dummyLambda = dict()
	dummyLambda["dummy"] = (lambda x : x)
	return dummyLambda

def multiCorrelate(datasets, layoutFolder):
	nsamples = len(datasets)
	xs = np.empty([nsamples,3])
	ys = np.empty([nsamples,1])
	for i in range(0,nsamples):
		d = datasets[i]			
		if isdir(join(layoutFolder, d.name)):# and d.name[-10:]!="furnitures":
			print d.name
			xs[i][0] = d.voronoiDistance
			xs[i][1] = d.voronoiTopVisits 
			xs[i][2] = d.voronoiStats.edges#len(get_bifurcation_points(d.voronoi))
			ys[i][0] = d.perfStats.transError.mean.mean
	lm = linear_model.LinearRegression()
	print xs
	print ys
	model = lm.fit(xs,ys)
	strategy = KFold(n_splits=5,shuffle=True)
	rsquared = lm.score(xs,ys)
	print rsquared
	mses = np.sqrt(np.abs(cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='neg_mean_squared_error')))
	print mses
	print mses.mean()
	rsquareds = cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='r2')
	print rsquareds
	print rsquareds.mean()


def plotAndSave(xs,ys,xLabel,yLabel,corrStats,plotFolder,name,numFolds,allxs,allys):
	#cs = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100]
	#gammas = [0.0000000001,0.000000001,0.00000001,0.0000001, 0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1]
	#degrees = [1, 2, 3, 4, 5]
	#cs = [1]
	#gammas = [1]
	cs = [1]
	gammas = [1]
	degrees = [1]
	origxs = xs
	origys = ys
	for c in cs:
		for g in gammas:
			for d in degrees:
				print "c = "+str(c)+", g = "+str(g)+", d = "+str(d)
				#lm = svm.SVR(kernel='rbf',max_iter=10000, degree = d, C=c, gamma=g)
				lm = linear_model.LinearRegression()
				nsamples = len(origxs)
				xs = np.array(origxs).reshape(nsamples,1)
				ys = np.array(origys).reshape(nsamples,1)
				model = lm.fit(xs,ys)
				strategy = KFold(n_splits=numFolds,shuffle=True)
				#prs,pvalue = pearsonr(xs,ys)
				#if abs(prs) > 0.5:
				try:
					rsquared = lm.score(xs,ys)
					mses = np.sqrt(np.abs(cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='neg_mean_squared_error')))
					rsquareds = cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='r2')
					print name
					print 'r^2: '+str(rsquared)
					print 'Avg RMSE: '+str(mses.mean())
					print 'Avg r^2: '+str(rsquareds.mean())
					corrStats.append([xLabel,yLabel,rsquared,mses.mean(),rsquareds.mean()])
					fig = plt.figure()
					plt.xlabel(xLabel)
					plt.ylabel(yLabel)
					fit = np.polyfit(origxs,origys,1)
					fit_fn = np.poly1d(fit)
					support_range = np.arange(min(origxs), max(origxs),0.1) 
					# fit_fn is now a function which takes in x and returns an estimate for y
					plt.plot(origxs,origys, 'ro', support_range, fit_fn(support_range), '-')
					fig.savefig(join(plotFolder,"correlation",name)+".png", bbox_inches='tight')
					pattern = Image.open(join(plotFolder,"correlation",name)+".png", "r").convert('RGBA')
					size = width, height = pattern.size
					draw = ImageDraw.Draw(pattern,'RGBA')
					font = ImageFont.truetype("OpenSans-Regular.ttf", 16)
					draw.text((80,525), 'rsquared: ' + str(round(rsquared,3)), fill=(0, 0, 0, 255), font=font)
					#draw.text((500,525), 'P-Value: '+ str(round(pvalue,5)), fill=(0, 0, 0, 255), font = font)
					pattern.save(join(plotFolder,"correlation",name)+".png")
					# we must also store the xs and ys in a table
					buildcsv(join(plotFolder,"correlation",name)+".csv",xLabel,yLabel,xs,ys,mses,rsquareds)
					plt.close(fig)
					fig = plt.figure()
					plt.xlabel(xLabel)
					plt.ylabel(yLabel)
					plt.plot(xs,ys, 'ro', support_range, fit_fn(support_range), '-')
					plt.plot(allxs,allys,'gx')
					fig.savefig(join(plotFolder,"correlation",name)+"_allpoints.png", bbox_inches='tight')
					plt.close(fig)
				except ValueError:
					pass
	return model

def fitLinearModel(xs,ys,xLabel,yLabel,corrStats,plotFolder,name,numFolds,allxs,allys):
	lm = linear_model.LinearRegression()
	nsamples = len(xs)
	orig_xs = xs
	orig_ys = ys
	xs = np.array(xs).reshape(nsamples,1)
	ys = np.array(ys).reshape(nsamples,1)
	model = deepcopy(lm.fit(xs,ys))
	strategy = KFold(n_splits=numFolds,shuffle=True)
	rsquared = lm.score(xs,ys)
	mses = np.sqrt(np.abs(cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='neg_mean_squared_error')))
	rsquareds = cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='r2')
	print name
	print 'r^2: '+str(rsquared)
	print 'Avg RMSE: '+str(mses.mean())
	print 'Avg r^2: '+str(rsquareds.mean())
	corrStats.append([xLabel,yLabel,rsquared,mses.mean(),rsquareds.mean()])
	fig = plt.figure()
	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	fit = np.polyfit(orig_xs,orig_ys,1)
	fit_fn = np.poly1d(fit)
	support_range = np.arange(min(orig_xs), max(orig_xs),0.1) 
	# fit_fn is now a function which takes in x and returns an estimate for y
	plt.plot(orig_xs,orig_ys, 'ro', support_range, fit_fn(support_range), '-')
	fig.savefig(join(plotFolder,"correlation",name)+".png", bbox_inches='tight')
	pattern = Image.open(join(plotFolder,"correlation",name)+".png", "r").convert('RGBA')
	size = width, height = pattern.size
	draw = ImageDraw.Draw(pattern,'RGBA')
	font = ImageFont.truetype("OpenSans-Regular.ttf", 16)
	draw.text((80,525), 'rsquared: ' + str(round(rsquared,3)), fill=(0, 0, 0, 255), font=font)
	#draw.text((500,525), 'P-Value: '+ str(round(pvalue,5)), fill=(0, 0, 0, 255), font = font)
	pattern.save(join(plotFolder,"correlation",name)+".png")
	# we must also store the xs and ys in a table
	buildcsv(join(plotFolder,"correlation",name)+".csv",xLabel,yLabel,xs,ys,mses,rsquareds)
	plt.close(fig)
	fig = plt.figure()
	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	plt.plot(orig_xs,orig_ys, 'ro', support_range, fit_fn(support_range), '-')
	plt.plot(allxs,allys,'gx')
	fig.savefig(join(plotFolder,"correlation",name)+"_allpoints.png", bbox_inches='tight')
	plt.close(fig)
	return model, mses.mean()

def fitModel(lm,xs,ys,numFolds):
	nsamples = len(xs)
	orig_xs = xs
	orig_ys = ys
	xs = np.array(xs).reshape(nsamples,1)
	ys = np.array(ys).reshape(nsamples,1)
	model = deepcopy(lm.fit(xs,ys))
	strategy = KFold(n_splits=numFolds,shuffle=True)
	rsquared = lm.score(xs,ys)
	mses = np.sqrt(np.abs(cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='neg_mean_squared_error')))
	rsquareds = cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='r2')
	return model, mses.mean(), rsquareds.mean()

def buildcsv(correlationFileName, xLabel, yLabel, xs, ys, mses, rsquareds):
	csv=open(correlationFileName, 'w')
	csv.write(xLabel+','+yLabel+'\n')
	for r in range(0, len(xs)):
		csv.write(str(xs[r][0])+','+str(ys[r][0])+'\n')
	csv.write('\n')
	csv.write(str(len(mses))+"-Fold RMSE:,")
	for r in range(0, len(mses)-1):
		csv.write(str(mses[r])+',')
	csv.write(str(mses[r])+'\n')
	csv.write('Average '+str(len(mses))+'-Fold RMSE:,'+str(mses.mean())+'\n')
	csv.write('\n')
	csv.write(str(len(rsquareds))+'-Fold rsquared:,')
	for r in range(0,len(rsquareds)-1):
		csv.write(str(rsquareds[r])+',')
	csv.write(str(rsquareds[r])+'\n')
	csv.write('Average '+str(len(rsquareds))+'-Fold rsquared:,'+str(rsquareds.mean())+'\n')
	csv.close()

def selectModelClass(modelClass):
	if modelClass=='LinearRegression':
		lm = linear_model.LinearRegression()
	elif modelClass=='ElasticNet':
		lm = linear_model.ElasticNet()
	return lm

def loadFeaturesFromFile(featureString):
	predictors = getPredictors()
	usedPredictors = {}
	featureFile = open(featureString,'r')
	for l in featureFile.readlines():
		line = l.strip()
		tokens = line.split('=')
		if tokens[0] in predictors and tokens[1]=='True':
			usedPredictors[tokens[0]] = predictors[tokens[0]]
	return usedPredictors

def selectFeaturesToUse(featureString):
	# fetch all possible predictors
	allPredictors = getPredictors()
	usedPredictors = {}
	if featureString=='overrideAll':
		# we have to load all possible features
		usedPredictors = allPredictors
	elif featureString in allPredictors:
		# select a single feature from the dictionary
		usedPredictors[featureString] = allPredictors[featureString]
	else:
		# try to interpret the feature string as a configuration file
		try:
			usedPredictors = loadFeaturesFromFile(featureString)
		except IOError:
			print "The feature string you specified is neither an override option, nor a valid string, nor a configuration file. Exiting."
			exit()
	return usedPredictors
	# in the end, we have to build a dictionary of features 

def rmse_cv(model,xs,ys,kf):
    rmse= np.sqrt(-cross_val_score(model, xs, ys, scoring="neg_mean_squared_error", cv = kf))
    return(rmse)

def ElasticNetTraining(xs, ys, featuresArray, numFolds, fsFolder, predictedFeature):
	#kf = KFold(n_splits=numFolds, shuffle=True)
	kf = RepeatedKFold(n_splits=numFolds, n_repeats=10)
	l1_ratios = [.1, .5, .7, .9, .95, .99, 1]
	alphas = [0.0001, 0.0003, 0.0005, 0.001, 0.01, 0.03, 0.05, 0.1, 0.3, 0.5, 1, 3, 5, 10, 30, 50, 100]
	# First we identify the best l1 ratio and alpha with cross validation (hyperparameters tuning)
	cv_elastic = [rmse_cv(linear_model.ElasticNet(alpha = alpha, l1_ratio=l1_ratio),xs,ys,kf).mean() 
            for (alpha, l1_ratio) in product(alphas, l1_ratios)]
	idx = list(product(alphas, l1_ratios))
	best_idx = np.argmin(cv_elastic)
	best_pair = idx[best_idx]
	best_alpha = best_pair[0]
	best_l1_ratio = best_pair[1]
	#estimator = linear_model.ElasticNetCV(l1_ratio=l1_ratios,alphas=alphas,cv=kf)
	#estimator.fit(xs,ys)
	print predictedFeature
	print "Best l1 ratio found is " + str(best_l1_ratio)
	print "Best alpha found is " + str(best_alpha)
	# Then we fit the estimator with the hyperparameters identified by cross validation
	estimator = linear_model.ElasticNet(l1_ratio=best_l1_ratio,alpha=best_alpha)
	model = deepcopy(estimator.fit(xs,ys))
	usedFeaturesIdx = [idx for idx,value in enumerate(estimator.coef_) if value > 0]
	usedFeatures = [feature for idx,feature in enumerate(featuresArray) if idx in usedFeaturesIdx]
	# Finally, we validate keeping l1_ratio and alpha fixed (model validation)
	strategy = KFold(n_splits=numFolds,shuffle=True)
	mses = np.sqrt(np.abs(cross_val_score(estimator, xs, ys, cv=strategy, n_jobs = -1, scoring='neg_mean_squared_error')))
	rsquareds = cross_val_score(estimator, xs, ys, cv=strategy, n_jobs = -1, scoring='r2')
	return model, usedFeatures, mses.mean(), rsquareds.mean()	

def KBestFeatureSelection(xs, ys, featuresArray, numFolds, n_features):
	estimator = LinearRegression()
	n_repeats = 100
	# in order to properly perform feature selection, we must perform cross validation as the outer loop 
	selected_features_per_fold = np.empty([n_repeats*numFolds,len(featuresArray)])
	kf = KFold(n_splits=numFolds, shuffle=True)
	i = 0
	for r in range(0,n_repeats):
		for train, test in kf.split(xs):
			x_train = xs[train]
			y_train = ys[train]
			x_test = xs[test]
			y_test = ys[test]
			# perform feature selection
			fs = SelectKBest(f_regression, k=n_features).fit(x_train, y_train)
			# take note of which features have been selected
			support = [1 if v else 0 for v in fs.get_support()]
			np.copyto(selected_features_per_fold[i], support)
			i+=1
	# now, we have to get the most voted k features
	selected_features_total = np.sum(selected_features_per_fold,axis=0)
	usedFeaturesIdx = np.argpartition(selected_features_total, -n_features)[-n_features:]
	usedFeatures = [feature for idx,feature in enumerate(featuresArray) if idx in usedFeaturesIdx]
	# now we can train the final model and get a cv estimate of its performance
	xr = xs[:,usedFeaturesIdx]
	model = deepcopy(estimator.fit(xr,ys))
	# validate
	strategy = KFold(n_splits=numFolds,shuffle=True)
	mses = np.sqrt(np.abs(cross_val_score(estimator, xr, ys, cv=strategy, n_jobs = -1, scoring='neg_mean_squared_error')))
	rsquareds = cross_val_score(estimator, xr, ys, cv=strategy, n_jobs = -1, scoring='r2')
	return model, usedFeatures, mses.mean(), rsquareds.mean()

def ParametrizedKBestFeatureSelection(xs, ys, featuresArray, numFolds, fsFolder, predictedFeature):
	# I want to explore how the cross-validated RMSE varies when increasing the number of top k features
	n_features = len(featuresArray)
	models = []
	xp = np.arange(start=1,stop=n_features+1,step=1)
	yp = np.empty(n_features)
	for k in xp:
		model, usedFeatures, rmse, r2 = KBestFeatureSelection(xs, ys, featuresArray, numFolds, k)
		models.append((model, usedFeatures, rmse, r2))
		yp[k-1] = rmse
	fig = plt.figure()
	plt.xlabel("Number of features, in order of decreasing relevance")
	plt.ylabel("RMSE")
	plt.plot(xp,yp, 'b-')
	fig.savefig(join(fsFolder,predictedFeature,"krmse.png"))
	plt.close(fig)
	saveCVKFoldFile(join(fsFolder,predictedFeature),models, numFolds)
	return getBestIndividualModel(models)

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
				#model, selectedFeatures, mse, r2 = ParametrizedKBestFeatureSelection(estimator, xs, ys, featuresArray, numFolds, fsFolder, predictedFeature)
				models[predictedFeature] = (model, selectedFeatures, mse, r2)
	return models	

def performIndividualFeatureTraining(datasets,layoutFolder,predictedStats,predictedStatsAttrs,numFolds,estimator,predictors):
	attrStats = getAttrStats()
	# error stats
	models = {}
	for eName, eLambda in predictedStats.iteritems():
		for aName, aLambda in predictedStatsAttrs.iteritems():
			for sName, sLambda in attrStats.iteritems():
				models[eName+"."+aName+"."+sName] = []
				for pName, pLambda in predictors.iteritems():
					xs,ys = [], []
					for d in datasets:			
						if isdir(join(layoutFolder, d.name)):
							xs.append(pLambda(d))
							ys.append(sLambda(aLambda(eLambda(d))))
					model, rmse, r2 = fitModel(estimator,xs,ys,numFolds)
					models[eName+"."+aName+"."+sName].append((model, pName, rmse, r2))
	return models

def plotIterator(datasets,layoutFolder,plotFolder,corrStats,predictedStats,predictedStatsAttrs,numFolds,meanPerfStats):
	attrStats = getAttrStats()
	predictors = getPredictors()
	meanErrorTypes = dict()
	meanErrorTypes["transError"] = (lambda meanPerfStats: meanPerfStats.transError)
	meanErrorTypes["rotError"] = (lambda meanPerfStats: meanPerfStats.rotError)
	runErrorTypes = dict()
	runErrorTypes["transError"] = (lambda run: run.transStats)
	runErrorTypes["rotError"] = (lambda run: run.rotStats)
	# error stats
	models = {}
	for eName, eLambda in predictedStats.iteritems():
		for aName, aLambda in predictedStatsAttrs.iteritems():
			for sName, sLambda in attrStats.iteritems():
				bestModel = None
				bestRMSE = float('inf')
				for pName, pLambda in predictors.iteritems():
					xs,ys,yc = [], [], []
					allxs = np.asarray([])
					allys = np.asarray([])
					for d in datasets:			
						if isdir(join(layoutFolder, d.name)):
							xs.append(pLambda(d))
							ys.append(sLambda(aLambda(eLambda(d))))
							yc.append(sLambda(aLambda(meanErrorTypes[eName](meanPerfStats))))
							runxs, runys = [], []
							for r in d.runs:
								runxs.append(pLambda(d))
								runys.append(aLambda(runErrorTypes[eName](r)))
							runxs = np.asarray(runxs)
							runys = np.asarray(runys)
							#m = 0.8
							#d = np.abs(runys - np.median(runys))
							#mdev = np.median(d)
							#s = d/mdev if mdev else 0.
							#runxs = runxs[s>m]
							#runys = runys[s>m]
							allxs = np.append(allxs,runxs)
							allys = np.append(allys,runys)
					xLabel = pName
					yLabel = eName+"."+aName+"."+sName
					name = pName+"-"+eName+"."+aName+"."+sName
					model,avg_rmse = fitLinearModel(xs,ys,xLabel,yLabel,corrStats,plotFolder,name,numFolds,allxs,allys)
					print "Constant baseline RMSE: "+str(np.sqrt(mean_squared_error(ys,yc)))
					print "Avg 5-fold RMSE of this model: "+str(avg_rmse)
					if avg_rmse < bestRMSE:
						bestModel = model
						bestRMSE = avg_rmse
					#yp = model.predict(xs)
					#print "Model RMSE: "+str(np.sqrt(mean_squared_error(ys,yp)))
				models[eName+"."+aName+"."+sName] = (bestModel, bestRMSE)
	return models


def PCAAnalyzer(datasets,layoutFolder,plotFolder,corrStats,predictedStats,predictedStatsAttrs,numFolds,meanPerfStats):
	attrStats = getAttrStats()
	predictors = getPredictors()
	meanErrorTypes = dict()
	meanErrorTypes["transError"] = (lambda meanPerfStats: meanPerfStats.transError)
	meanErrorTypes["rotError"] = (lambda meanPerfStats: meanPerfStats.rotError)
	runErrorTypes = dict()
	runErrorTypes["transError"] = (lambda run: run.transStats)
	runErrorTypes["rotError"] = (lambda run: run.rotStats)
	# error stats
	nsamples = len(datasets)
	X = []	
	ys = np.empty([nsamples,1])
	for pName, pLambda in predictors.iteritems():
		print pName
		xp = []
		for i in range(0, nsamples):
			d = datasets[i]
			xp.append(pLambda(d))
			ys[i][0] = d.perfStats.transError.mean.mean
		xp = preprocessing.scale(xp)
		X.append(xp)
	X = np.transpose(np.array(X))
	pca = PCA(n_components=5)
	X_pca = pca.fit_transform(X)
	print "PCA:"
	print pca.explained_variance_ratio_ 
	fs = SelectKBest(f_regression, k=3)
	X_new = fs.fit_transform(X, ys)
	print zip(fs.get_support(),predictors.iteritems())
	# now we try to predict
	cs = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100]
	gammas = [0.0000000001,0.000000001,0.00000001,0.0000001, 0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1]
	#degrees = [1, 2, 3, 4, 5]
	degrees = [1]
	#for al in range(1,11):
	#	alpha = al*0.01
		#print "Alpha: "+str(float(alpha))
	for c in cs:
		for g in gammas:
			for d in degrees:
				print "c = "+str(c)+", g = "+str(g)+", d = "+str(d)
				#lm = linear_model.LinearRegression()#linear_model.Lasso(alpha=alpha)#LinearRegression()
				lm = svm.SVR(kernel='rbf',max_iter=10000, degree = d, C=c, gamma=g)#linear_model.LinearRegression()
				model = lm.fit(X_new,ys)
				strategy = KFold(n_splits=5,shuffle=True)
				rsquared = lm.score(X_new,ys)
				print rsquared
				all_mses = []
				all_rsquareds = []
				for i in range(0, 20):
					mses = np.sqrt(np.abs(cross_val_score(lm, X_new, ys, cv=strategy, n_jobs = -1, scoring='neg_mean_squared_error')))
					rsquareds = cross_val_score(lm, X_new, ys, cv=strategy, n_jobs = -1, scoring='r2')
					all_mses += mses.tolist()
					all_rsquareds += rsquareds.tolist()
				print "Final average:"
				print np.asarray(all_mses).mean()
				print np.asarray(all_rsquareds).mean()
	#print "Additional test:"
 	#F, pval = feature_selection.f_regression(X, ys, center=False)
 	#print F
 	#print pval

def plotGraphs(datasets,layoutFolder,plotFolder,meanPerfStats,numFolds):
	corrStatsFile = open(join(plotFolder, "corrStats.csv"), "w")
	corrStatsFile.write("x, y, r^2, avg "+str(numFolds)+"-fold RMSE, avg "+str(numFolds)+"-fold r^2 \n")
	corrStats = []
	errorTypes = getErrorTypes()
	runStats = getRunStats()
	errorAttrs = getErrorAttrs()
	models = plotIterator(datasets,layoutFolder,plotFolder,corrStats,errorTypes,errorAttrs,numFolds,meanPerfStats)
	corrStats.sort(key=lambda x:x[2], reverse=True)
	for elem in corrStats:
		corrStatsFile.write(elem[0]+','+elem[1]+','+str(elem[2])+','+str(elem[3])+','+str(elem[4])+'\n')
	corrStatsFile.close()
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
def retrieveNearbyPixels(image, currentPixel, previousPixel, laserLength):
	# Retrieve all black pixels (black = occupied)
	black_pixels = np.argwhere(image == 0)
	# Compute the orientation of the robot
	ref_angle = correct_angle(math.atan2(currentPixel[0]-previousPixel[0], currentPixel[1]-previousPixel[1]))
	# Compute the distance between the current pixel and every other black pixel
	distances = np.sqrt((black_pixels[:,0] - currentPixel[0]) ** 2 + (black_pixels[:,1] - currentPixel[1]) ** 2)
	# Compute the relative orientation 
	angles = np.arctan2(black_pixels[:,0] - currentPixel[0], black_pixels[:,1]-currentPixel[1])
	angles = [correct_angle(a) for a in angles]
	lgt = len(distances)
	# Return only those pixels that are within the laser range and field of view
	indices = [i for i in range(0, lgt) if distances[i] < laserLength and (np.pi - math.fabs(math.fabs(ref_angle - angles[i]) - np.pi))<=3.0/4.0*np.pi] 
	return black_pixels[indices]

''' Retrieves all pixels that are visible from the current robot location and orientation.
A pixel is considered to be visible if three conditions hold:
- it is within the laser range
- it is within the laser field of view
- there are no other black pixels on the line connecting it to the current robot location '''
def retrieveVisiblePixels(image, gtImage, totalNodes, currentPixel, previousPixel, laserLength):
	height, width = image.shape
	# Retrieve candidate pixels 
	nearbyPixels = retrieveNearbyPixels(image, currentPixel, previousPixel, laserLength)
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
def lineOfSight(VG, image, gtImage, totalNodes, currentPixel, previousPixel, voronoiNodesMap, voronoiNodesReverseMap, laserLength):
	height, width = image.shape
	visiblePixels = retrieveVisiblePixels(image, gtImage, totalNodes, currentPixel, previousPixel, laserLength)
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

def getTopVisitedNodes(G,num):
	return sorted([G.node[n]['nvisits'] for n in G.nodes()],reverse=True)[:num]

''' Explore the voronoi graph; return the total amount of travelled distance and the sum of the visits
of the top N visited nodes.''' 
def exploreVoronoiGraph(VG, image, gtImage, start, voronoiNodesMap, voronoiNodesReverseMap, laserLength, scale, speed, topNVisitedNodes):
	# set every node as 'not seen' and with zero visits
	initNodeVisitedStatus(VG)
	# initialize counting variables
	height, width = image.shape
	totalNodes = len(VG.nodes())
	currentPixel = start
	previousPixel = (currentPixel[0]+1,currentPixel[1])
	numVisitedNodes, numSeenNodes, totalDistance, totalAngle = 0, 0, 0, 0
	# line-of-sight: identify and mark as 'seen' the pixels that are visible from the current location
	visibleNodes, nseen = lineOfSight(VG, image, gtImage, totalNodes, currentPixel, previousPixel, voronoiNodesMap, voronoiNodesReverseMap, laserLength)
	numSeenNodes += nseen
	# we proceed until we've seen every single node of the graph 
	while numSeenNodes < totalNodes:
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
			totalAngle += node_angle(previousPixel, currentPixel, newPixel)
			previousPixel = currentPixel
			previousNode = currentNode
			currentPixel = newPixel
			currentNode = newNode
			visibleNodes, nseen = lineOfSight(VG, image, gtImage, totalNodes,currentPixel, previousPixel, voronoiNodesMap, voronoiNodesReverseMap, laserLength)
			# add to the number of seen nodes the new ones we have actually seen in line of sight
			numSeenNodes += nseen
			# and increase the number of times this current node has been visited
			VG.node[n]['nvisits'] += 1
			numVisitedNodes += 1
			# finally, increase the total travelled distance by the amount joining two consecutive nodes on the path
			totalDistance += node_distance(VG,previousNode,currentNode)
		currentPixel = nearestPixel
	return totalDistance/scale, sum(getTopVisitedNodes(VG,topNVisitedNodes)), totalAngle

def createVoronoiGraphFromImage(imagePath, worldPath):
	print imagePath
	image = cv2.imread(imagePath,cv2.IMREAD_GRAYSCALE)
	height, width = image.shape
	# Invert
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
	# Simplify graph by removing all 'passthrough' nodes
	print len(G.nodes())
	remove_flow_through(G)
	print "After removal: "+str(len(G.nodes()))	
	# Further simplify by aggregating together those nodes that are very very close to each other
	close_nodes = lambda G,u,v: (u in G[v] and v in G[u] and node_distance(G,u,v)<scale*0.2)
	updated = True
	Gcred = G.copy()
	while updated:
		updated = False
		for u in Gcred.nodes():
			for v in Gcred.nodes():
				if close_nodes(Gcred, u,v):
					Gcred = nx.contracted_nodes(Gcred, u, v, self_loops=False)
					updated = True
					break
			if updated:
				break
	G = Gcred
	print "After further removal: "+str(len(G.nodes()))	
	# necessary to filter out unreachable rooms
	Gc = max(nx.connected_component_subgraphs(G), key=len)
	return Gc

def loadVoronoiGraph(datasetName, voronoiPath, worldPath):
	pickleFile = join(voronoiPath, "pickle",datasetName)+"_voronoi.pickle"
	imageFile = join(voronoiPath, "images",datasetName)+"_voronoi.png"
	if exists(pickleFile):
		Gc = nx.read_gpickle(pickleFile)
	else:
		Gc = createVoronoiGraphFromImage(imageFile, worldPath)
		nx.write_gpickle(Gc, pickleFile)
	return Gc

def processVoronoiGraph(datasetName, voronoiPath, worldPath, gtImagePath):
	VG = loadVoronoiGraph(datasetName, voronoiPath, worldPath)
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
	speed = 0.85 # m/s
	topNVisitedNodes = 40
	laserRangeInMeters = 30
	totalDistance, topVisits, totalAngle = exploreVoronoiGraph(VG, img, gtImage, nearestPixel, voronoiNodesMap, voronoiNodesReverseMap, laserRangeInMeters*scale, scale, speed*scale, topNVisitedNodes)
	print "Voronoi Distance "+str(totalDistance)
	print "Voronoi Angle "+str(totalAngle)
	return VG, voronoiCenter, totalDistance, topVisits,totalAngle, GraphStats(VG)

def computeDatasetEntropy(myDataset, gtImagePath):
	gtImage = cv2.imread(gtImagePath,cv2.IMREAD_GRAYSCALE)
	height, width = gtImage.shape
	# Black is obstacle, white is free space
	_,thresh = cv2.threshold(gtImage,127,255,cv2.THRESH_BINARY)
	# Convert to zeros and ones
	gtImage[gtImage == 255] = 1
	# Apply kernel
	densities = {}
	total = 0
	for r in range(0,height-1):
		for c in range(0, width-1):
			occupancy = (gtImage[r,c]+gtImage[r+1,c]+gtImage[r+1,c+1]+gtImage[r,c+1])/4
			if not (occupancy in densities):
				densities[occupancy] = 0
			densities[occupancy] += 1
			total += 1
	entropy = 0
	for occupancy, numTimes in densities.iteritems():
		frequency = float(numTimes) / total
		entropy += -frequency * np.log(frequency)
	myDataset.entropy = entropy

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

def remove_flow_through(graph):
	for n in graph.nodes():
		neighbors = graph.neighbors(n)
		if len(neighbors) == 2:
			w1 = graph.get_edge_data(n,neighbors[0])['weight']
			w2 = graph.get_edge_data(n,neighbors[1])['weight']
			graph.remove_node(n)
			graph.add_edge(neighbors[0], neighbors[1],weight=w1+w2)

def setVoronoiProperties(myDataset, voronoi, voronoiCenter, voronoiDistance, voronoiTopVisits, voronoiRotation, voronoiStats):
	myDataset.voronoi = voronoi
	myDataset.voronoiCenter = voronoiCenter
	myDataset.voronoiDistance = voronoiDistance
	myDataset.voronoiTopVisits = voronoiTopVisits
	myDataset.voronoiRotation = voronoiRotation
	myDataset.voronoiStats = voronoiStats	

def analyzeDatasetsOld(runsFolder, layoutFolder, voronoiFolder, worldFolder, plotFolder):
	datasets = []
	runs = []
	for f in listdir(runsFolder):
		if isdir(join(runsFolder, f)):# and "furnitures" not in f:
			datasets.append(loadDataset(f, runsFolder))
	for d in datasets:
		if isdir(join(layoutFolder, d.name)):
			print d.name
			runs += d.runs
			loadGeometry(d, join(layoutFolder, d.name, d.name)+".xml")	
			#if isfile(join(voronoiFolder, d.name)+"_voronoi.png"):
			voronoi, voronoiCenter, voronoiDistance, voronoiTopVisits, voronoiRotation, voronoiStats = processVoronoiGraph(d.name, voronoiFolder, join(worldFolder, d.name)+".world", join(worldFolder, d.name)+".png")
			setVoronoiProperties(d, voronoi, voronoiCenter, voronoiDistance, voronoiTopVisits, voronoiRotation, voronoiStats)
			computeDatasetEntropy(d, join(worldFolder, d.name)+".png")
			print len(d.runs)
			#print d.geometry
	meanPerfStats = computePerformanceStats(runs)
	#multiCorrelate(datasets, layoutFolder)
	models = plotGraphs(datasets,layoutFolder,plotFolder,meanPerfStats,numFolds=5)
	return models

# bisogna distinguere due modi d'uso: singola feature o multiple features (feature selection)
# se singola feature, posso scegliere di far calcolare:
# a) un modello per ogni feature individuale
# b) un modello solo per alcune features (abilitate da sezioni True / False)
# c) solo un modello (default)
# in questo caso l'output e' dato da tanti modelli quanti se ne sono selezionati
# se multiple features, allora viene fatta feature selection e in output salviamo UN solo modello
# in cui indichiamo anche quali features sono state mantenute

# tre scelte da fare:
# 1) modello da usare (LinearRegression / ElasticNet / ...)
# 2) singola feature / multiple features
# 3) SE singola feature, posso scegliere se calcolare un default, un overrideAll, oppure un selectFromFile
# 3) SE multiple features, posso scegliere se fare recursive feature elimination o specificare un goal
# 4) per alcuni modelli e' possibile specificare parametri addizionali (es. elastic net vuole i parametri di penalty)

def setupFeatureSelection(datasets,layoutFolder,fsFolder,numFolds,predictors):
	errorTypes = getErrorTypes()
	runStats = getRunStats()
	errorAttrs = getErrorAttrs()
	function = (lambda paramList: ParametrizedKBestFeatureSelection(*paramList))
	models = performFeatureSelection(datasets,layoutFolder,fsFolder,errorTypes,errorAttrs,numFolds,predictors,function)
	return models

def setupIndividualFeatureTraining(datasets,layoutFolder,numFolds,estimator,predictors):
	errorTypes = getErrorTypes()
	runStats = getRunStats()
	errorAttrs = getErrorAttrs()
	models = performIndividualFeatureTraining(datasets,layoutFolder,errorTypes,errorAttrs,numFolds,estimator,predictors)
	bestModels = getBestModels(models)
	return models, bestModels

def setupElasticNetTraining(datasets,layoutFolder,fsFolder,numFolds,predictors):
	errorTypes = getErrorTypes()
	runStats = getRunStats()
	errorAttrs = getErrorAttrs()
	function = (lambda paramList: ElasticNetTraining(*paramList))
	models = performFeatureSelection(datasets,layoutFolder,fsFolder,errorTypes,errorAttrs,numFolds,predictors,function)
	return models

def getBestModels(models):
	bestModels = {}
	for predictedFeature, availableModels in models.iteritems():
		bestModel, bestName, bestRMSE, bestR2 = getBestIndividualModel(availableModels)
		bestModels[predictedFeature] = (bestModel, bestName, bestRMSE, bestR2)
	return bestModels

def getBestIndividualModel(models):
	bestModel = None
	bestName = ''
	bestRMSE = float('inf')
	bestR2 = float('-inf')
	for model, name, rmse, r2 in models:
		if rmse < bestRMSE:
			bestModel = model
			bestName = name
			bestRMSE = rmse
			bestR2 = r2
	return bestModel, bestName, bestRMSE, bestR2

def analyzeDatasets(runsFolder, layoutFolder, voronoiFolder, worldFolder, plotFolder, modelsFolder, modelClass, useMode, featureString):
	datasets = []
	runs = []
	for f in listdir(runsFolder):
		if isdir(join(runsFolder, f)):# and "furnitures" not in f:
			datasets.append(loadDataset(f, runsFolder))
	for d in datasets:
		if isdir(join(layoutFolder, d.name)):
			print d.name
			runs += d.runs
			loadGeometry(d, join(layoutFolder, d.name, d.name)+".xml")	
			#if isfile(join(voronoiFolder, d.name)+"_voronoi.png"):
			voronoi, voronoiCenter, voronoiDistance, voronoiTopVisits, voronoiRotation, voronoiStats = processVoronoiGraph(d.name, voronoiFolder, join(worldFolder, d.name)+".world", join(worldFolder, d.name)+".png")
			setVoronoiProperties(d, voronoi, voronoiCenter, voronoiDistance, voronoiTopVisits, voronoiRotation, voronoiStats)
			computeDatasetEntropy(d, join(worldFolder, d.name)+".png")
			print len(d.runs)
			#print d.geometry
	meanPerfStats = computePerformanceStats(runs)
	# select which model class should be used (LinearRegression, ElasticNet, ...)
	estimator = selectModelClass(modelClass)
	# select whether we should perform feature selection or use single features 
	if useMode=='feature_selection':
		# in this mode, we first identify, for each subset of k features, which are the k features that correlate
		# best with our data; then we identify the best number of features k 
		fsFolder = join(modelsFolder,modelClass,'models','fs')
		models = setupFeatureSelection(datasets,layoutFolder,fsFolder,5,getPredictors())
		saveFSModels(models,fsFolder,5)
	elif useMode=='linear_regression':
		# in this mode, we directly fit a simple non-penalized linear regression model on the given features
		usedPredictors = selectFeaturesToUse(featureString)
		models,bestModels = setupIndividualFeatureTraining(datasets,layoutFolder,5,estimator,usedPredictors)
		saveIndividualModels(models, join(modelsFolder,modelClass,'models','individual'), 5)
		saveBestModels(bestModels,join(modelsFolder,modelClass,'models','best_individual'), 5)
	elif useMode=='elastic_net':
		# in this mode, we use cross validation to find the best hyperparameters of an elastic net model
		fsFolder = join(modelsFolder,'ElasticNet','models','fs')
		models = setupElasticNetTraining(datasets,layoutFolder,fsFolder,5,getPredictors())
		saveFSModels(models,fsFolder,5)	


	#multiCorrelate(datasets, layoutFolder)
	
	#models = plotGraphs(datasets,layoutFolder,plotFolder,meanPerfStats,numFolds=5)

def saveSummaryFile(path, corrStats, numFolds):
	summaryFile = open(join(path, "summary.csv"), "w")
	summaryFile.write("predictedFeature, predictor, avg "+str(numFolds)+"-fold RMSE, avg "+str(numFolds)+"-fold r^2 \n")
	corrStats.sort(key=lambda x:x[0], reverse=False)
	for elem in corrStats:
		summaryFile.write(elem[0]+','+elem[1]+','+str(elem[2])+','+str(elem[3])+'\n')
	summaryFile.close()

def saveBestModels(models, path, numFolds):
	corrStats = []
	for predictedFeature, (model, name, rmse, r2) in models.iteritems():
		if not exists(join(path,predictedFeature)):
			makedirs(join(path,predictedFeature))
		joblib.dump(model, join(path,predictedFeature,name)+'.mdl')
		corrStats.append((predictedFeature,name,rmse,r2))
	saveSummaryFile(path,corrStats, numFolds)
		# save somewhere name, rmse, r2

def saveIndividualModels(models,path, numFolds):
	corrStats = []
	for predictedFeature, modelList in models.iteritems():
		if not exists(join(path,predictedFeature)):
			makedirs(join(path,predictedFeature))
		for model, name, rmse, r2 in modelList:
			joblib.dump(model, join(path,predictedFeature,name)+'.mdl')
			corrStats.append((predictedFeature,name,rmse,r2))
			# save somewhere names, rmse, r2
	saveSummaryFile(path,corrStats, numFolds)

def saveFSModels(models, path, numFolds):
	corrStats = []
	for predictedFeature, (model, featuresArray, rmse, r2) in models.iteritems():
		if not exists(join(path,predictedFeature)):
			makedirs(join(path,predictedFeature))
		joblib.dump(model, join(path,predictedFeature,'model')+'.mdl')
		corrStats.append((predictedFeature,';'.join(featuresArray),rmse,r2))
		# save somewhere in a text file the featuresArray and also rmse, r2
	saveSummaryFile(path,corrStats, numFolds)

def loadModels(path):
	models = {}
	for f in listdir(path):
		if isfile(join(path,f)) and f[-3:]=="mdl":
			predictedFeature = f[:-4]
			models[predictedFeature]=joblib.load(join(path,f))
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
	#buildcsv(sys.argv[1])
    parser = argparse.ArgumentParser(description='This is the main tool of the RPPF. Its task is to analyze the error data of the different runs of the training datasets, correlate it with properties extracted from such datasets, build a prediction model and use it to predict the error data of the desired test datasets. Please refer to the wiki for extended documentation.')
    parser.add_argument('runs_folder',help='the folder in which all the training datasets and their respective runs are stored')
    parser.add_argument('layouts_folder',help='the folder in which the layout information of each training dataset, as extracted by the Layout Extractor, is stored')
    parser.add_argument('voronoi_folder',help='the folder in which the data related to the voronoi graph of each training dataset, as extracted by the Voronoi Extractor, is stored')
    parser.add_argument('world_folder',help='the folder in which the Stage data of each training dataset, as used to perform the Stage simulations, is stored')
    parser.add_argument('models_folder',help='the output folder in which the tool stores the trained models')
    parser.add_argument('plot_folder',help='the output folder in which the tool stores the results of the correlation analyses performed on the training dataset')
    parser.add_argument('datasets_to_predict_folder',help='the folder in which all the data related to the datasets of the test set for which the tool must perform predictions is stored')
    args = parser.parse_args()
    analyzeDatasets(args.runs_folder,args.layouts_folder,args.voronoi_folder,args.world_folder,args.plot_folder,args.models_folder,'LinearRegression', 'elastic_net', 'overrideAll')
    