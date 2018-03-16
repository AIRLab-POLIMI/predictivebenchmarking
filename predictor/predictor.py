import argparse, sys
from os import listdir
from os.path import join, exists, isdir, isfile
from analyzer import loadModels, processVoronoiGraph, checkPredictors, getGeometricalPredictors, getTopologicalPredictors, getVoronoiGraphPredictors, getVoronoiTraversalPredictors, getPredictors, createVoronoiGraphFromImage, loadGeometry
from structures.dataset import Dataset
from structures.statistics import GraphStats
from structures.geometry import Geometry
import numpy as np
import networkx as nx

def loadVoronoiGraph(datasetName, voronoiPath, worldPath):
	pickleFile = join(voronoiPath, datasetName)+"_voronoi.pickle"
	imageFile = join(voronoiPath, datasetName)+"_voronoi.png"
	if exists(pickleFile):
		print "Loading Voronoi graph... [DONE]"
		Gc = nx.read_gpickle(pickleFile)
	else:
		if exists(imageFile):
			Gc = createVoronoiGraphFromImage(imageFile, worldPath)
			nx.write_gpickle(Gc, pickleFile)
		else:
			raise IOError("Missing bitmap Voronoi graph for "+datasetName+", did you run the Voronoi extractor?")
	return Gc

def setupPrediction(predictFolder, modelsFolder):
	component = selectComponentToPredict()
	manualOrAutomatic = selectManualOrAutomaticPrediction()
	if manualOrAutomatic == 1: # automatic
		approach = findBestRMSEPredictor(modelsFolder, component)
	else: # manual:
		approach = selectPredictionApproach()
	if approach == 1: # individual linear regression
		predictor, model = selectPredictor(modelsFolder, component)
		print "Computing predictions with Linear Regression model."
		predictDatasetsWithSingleRegressor(predictFolder, [predictor], component, model)
	elif approach == 2: # f-regression multiple feature regressions
		predictors, model = predictDatasetsWithFRegression(predictFolder, modelsFolder, component)
		print "Computing predictions with F-regression model."
		predictDatasetsWithSingleRegressor(predictFolder, predictors, component, model)
	elif approach == 3: # ElasticNet
		predictors, model = predictDatasetsWithElasticNet(predictFolder, modelsFolder, component)
		print "Computing predictions with ElasticNet model."
		predictDatasetsWithSingleRegressor(predictFolder, predictors, component, model)

def getFeatureListTerminator(tokens):
	try:
		idxOfFirstEmptyItem, _ = next((idx, obj) for idx, obj in enumerate(tokens) if obj == '')
	except StopIteration:
		idxOfFirstEmptyItem = len(tokens)
	return idxOfFirstEmptyItem - 2

def predictDatasetsWithFRegression(predictFolder, modelsFolder, component):
	# we first need to identify which features are used by the FRegressor
	summaryFile = open(join(modelsFolder,'LinearRegression','models','fs', "summary.csv"), "r")
	lines = summaryFile.readlines()
	modelsFeatures = {}
	for line in lines[1:]:
		tokens = line.split(',')
		modelsFeatures[tokens[0]] = tokens[1].split(';')
	usedFeatures = modelsFeatures[component]
	models = loadModels(join(modelsFolder,'LinearRegression','models','fs'))
	return usedFeatures, models[component]['model']

def predictDatasetsWithElasticNet(predictFolder, modelsFolder, component):
	# we first need to identify which features are used by the ElasticNet
	summaryFile = open(join(modelsFolder,'ElasticNet','models','fs', "summary.csv"), "r")
	lines = summaryFile.readlines()
	modelsFeatures = {}
	for line in lines[1:]:
		tokens = line.split(',')
		modelsFeatures[tokens[0]] = tokens[1].split(';')
	usedFeatures = modelsFeatures['allFeatures']
	models = loadModels(join(modelsFolder,'ElasticNet','models','fs'))
	return usedFeatures, models[component]['model']

def selectComponentToPredict():
	modeArray = ["transError.mean.mean", "transError.mean.std", "rotError.mean.mean", "rotError.mean.std"]
	mode = 0
	while mode <= 0 or mode >= 6:
		print "Which component of the localization error you are interested in predicting?"
		print "1) translational localization error mean"
		print "2) translational localization error st.dev."
		print "3) rotational localization error mean"
		print "4) rotational localization error st.dev."
		print "5) exit"
		try:
			mode = int(raw_input("Your choice:"))
			if mode == 5:
				exit()
		except ValueError:
			print "Invalid option!"
			mode = 0
	return modeArray[mode-1]

def selectPredictionApproach():
	mode = 0
	while mode <= 0 or mode >= 5:
		print "Which model type would you like to use?"
		print "1) individual linear regression"
		print "2) F-regression multiple features model"
		print "3) regularized ElasticNet model"
		print "4) exit"
		try:
			mode = int(raw_input("Your choice:"))
			if mode == 4:
				exit()
		except ValueError:
			print "Invalid option!"
			mode = 0
	return mode

def selectManualOrAutomaticPrediction():
	mode = 0
	while mode <= 0 or mode >= 4:
		print "Which prediction approach would you like to use?"
		print "1) automatic (find model with lowest RMSE)"
		print "2) manual (select desired model)"
		print "3) exit"
		try:
			mode = int(raw_input("Your choice:"))
			if mode == 3:
				exit()
		except ValueError:
			print "Invalid option!"
			mode = 0
	return mode

def retrieveRMSEOfModelClass(summaryPath, component):
	summaryFile = open(summaryPath, "r")
	lines = summaryFile.readlines()
	modelsRMSE = {}
	for line in lines[1:]:
		tokens = line.split(',')
		modelsRMSE[tokens[0]] = float(tokens[2]) if tokens[2]!='' else float('inf')
	return modelsRMSE[component]

def findBestRMSEPredictor(modelsFolder, component):
	# three possibilities: it may be an individual linear regression model, an F-regression model, or an ElasticNet model
	bestRMSE = np.zeros(3)
	# linear model performance
	bestRMSE[0] = retrieveRMSEOfModelClass(join(modelsFolder,'LinearRegression','models','best_individual', "summary.csv"), component)
	# f-regression performance
	bestRMSE[1] = retrieveRMSEOfModelClass(join(modelsFolder,'LinearRegression','models','fs', "summary.csv"), component)
	# ElasticNet performance
	bestRMSE[2] = retrieveRMSEOfModelClass(join(modelsFolder,'ElasticNet','models','fs', "summary.csv"), component)
	return np.argmin(bestRMSE)+1

def selectPredictor(modelsFolder, component):
	models = loadModels(join(modelsFolder,'LinearRegression','models','individual'))
	idxMap = []
	idx = 0
	for key, elem in models[component].iteritems():
		idxMap.append(key)
		idx += 1
	mode = 0
	while mode <= 0 or mode >= len(idxMap)+2:
		print "Which model would you like to use?"
		for idx in range(0, len(idxMap)):
			print str(idx+1)+") "+idxMap[idx]
		print str(len(idxMap)+1)+") use model with lowest RMSE"
		print str(len(idxMap)+2)+") exit"
		try:
			mode = int(raw_input("Your choice:"))
			if mode == len(idxMap)+1:
				# look for model with minimum RMSE
				pass
			elif mode == len(idxMap)+2:
				exit()
		except ValueError:
			print "Invalid option!"
			mode = 0
	return idxMap[mode-1],models[component][idxMap[mode-1]]	

def predictDatasetsWithSingleRegressor(predictFolder, predictors, component, model):
	allPredictors = getPredictors(0) # debug mode disabled
	for f in listdir(predictFolder):
		if isfile(join(predictFolder,f)) and f[-5:]=="world":
			d = Dataset(f[:-6], None, None)
			print "Predicting "+component+" for "+d.name+"."
			# we need to be sure we have the necessary data to compute the prediction
			if checkPredictors(predictors, getGeometricalPredictors()) or checkPredictors(predictors, getTopologicalPredictors()):
				if exists(join(predictFolder, d.name)+".xml"):
					print "Computing geometrical and topological features...",
					sys.stdout.flush()
					d.geometry, d.topology, d.topologyStats = loadGeometry(join(predictFolder, d.name)+".xml")
					print "[DONE]"
				else:
					print "Layout file for "+d.name+" not found, did you run the Layout extractor?"
					print "Skipping "+d.name+" due to missing data."
			if checkPredictors(predictors, getVoronoiGraphPredictors()) or checkPredictors(predictors, getVoronoiTraversalPredictors()):
				worldFile = join(predictFolder, d.name)+".world"
				gtImageFile = join(predictFolder, d.name)+".png"
				try:
					d.voronoi = loadVoronoiGraph(d.name, predictFolder, worldFile)
					if checkPredictors(predictors, getVoronoiTraversalPredictors()):
						# rirordarsi di inserire o chiedere range, FOV, rot. distance, anche se sarebbe molto meglio salvarli nel modello
						d.voronoiCenter, d.voronoiDistance, d.voronoiRotation = processVoronoiGraph(d.voronoi, worldFile, gtImageFile, 30, 270*3.14/180, 0.5)
					if checkPredictors(predictors, getVoronoiGraphPredictors()):
						print "Computing Voronoi graph stats...",
						sys.stdout.flush()
						d.voronoiStats = GraphStats(d.voronoi)
						print "[DONE]"
				except IOError, e:
					print str(e)
					print "Skipping "+d.name+" due to missing data."
			# predict
			evaluatedFeatures = [[p(d) for p in [allPredictors.get(key) for key in predictors]]]
			print "Predicted "+component+" for "+d.name+": "+ str(model.predict(evaluatedFeatures))

if __name__ == '__main__':
	#buildcsv(sys.argv[1])
    parser = argparse.ArgumentParser(description='This is the main tool of the RPPF. Its task is to analyze the error data of the different runs of the training datasets, correlate it with properties extracted from such datasets, build a prediction model and use it to predict the error data of the desired test datasets. Please refer to the wiki for extended documentation.')
    #parser.add_argument('layouts_folder',help='the folder in which the layout information of each training dataset, as extracted by the Layout Extractor, is stored')
    parser.add_argument('models_folder',help='the input folder from which the tool loads the trained models')
    parser.add_argument('datasets_to_predict_folder',help='the folder in which all the data related to the datasets of the test set for which the tool must perform predictions is stored')
    args = parser.parse_args()
    setupPrediction(args.datasets_to_predict_folder, args.models_folder)
