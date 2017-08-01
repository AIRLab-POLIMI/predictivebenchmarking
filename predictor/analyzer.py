import sys
from PIL import Image,ImageDraw,ImageFont
from os import listdir
from os.path import join,exists, isdir
from structures.run import Run
from structures.dataset import Dataset
from structures.statistics import Stats, ErrorStats, RunStats, PerfStats
from structures.geometry import Geometry
import numpy as np
import util.util_XML as xmlutil
import matplotlib.pyplot as plt
import math
from scipy.stats import pearsonr

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
		raise RuntimeError("Error while loading the dataset runs!")
	# if we are here, we successfully loaded the error stats from file
	myRun = Run(tstats,rstats,totalTime,totalLength)
	#print myRun
	return myRun

def loadDatasetRuns(runsFolder, datasetName):
	# loads all the runs of the specified dataset
	runs = []
	datasetPath = join(runsFolder,datasetName)
	for r in listdir(datasetPath):
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

def loadGeometry(myDataset, xmlFile):
	# load and parse the xml of the layout
	rooms, boundingPolygon, scalingFactor = xmlutil.loadXML(xmlFile)
	datasetGeometry = Geometry(rooms, boundingPolygon, scalingFactor)
	myDataset.geometry = datasetGeometry
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
	rooms, boundingPolygon, scalingFactor = xmlutil.loadXML(xmlFile)
	datasetGeometry = Geometry(rooms, boundingPolygon, scalingFactor)
	myDataset.geometry = datasetGeometry

def loadDataset(datasetName, runsFolder):
	# load the runs
	runs = loadDatasetRuns(runsFolder, datasetName)
	# compute the performance statistics
	perfStats = computePerformanceStats(runs)
	# create the dataset object
	myDataset = Dataset(datasetName, runs, perfStats)
	#print myDataset.perfStats
	return myDataset
	# compute geometry
	# compute topology
	# correlate

def prova2(dataset):
	errors = ["transError", "rotError"]
	attrs = ["mean", "std", "numSamples"]
	attrStats = ["mean", "std"]
	for e in errors:
		for a in attrs:
			for s in attrStats:
				print getattr(getattr(getattr(dataset.perfStats, e),a),s)

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
	predictors["area"] = (lambda dataset: (dataset.geometry.shape.area))
	predictors["perimeter"] = (lambda dataset: (dataset.geometry.shape.perimeter))
	predictors["wallRatio"] = (lambda dataset: (dataset.geometry.shape.wallRatio))
	predictors["numRooms"] = (lambda dataset: (len(dataset.geometry.rooms)))
	#predictors["totalTime"] = (lambda dataset: (dataset.perfStats.totalTime.mean))
	#predictors["totalLength"] = (lambda dataset : (dataset.perfStats.totalLength.mean))
	predictors["avgRoomArea"] = (lambda dataset: np.array([r.shape.area for r in dataset.geometry.rooms]).mean()**2)
	predictors["avgRoomPerimeter"] = (lambda dataset: np.array([r.shape.perimeter for r in dataset.geometry.rooms]).mean()**2)
	predictors["avgRoomWallRatio"] = (lambda dataset: np.array([r.shape.wallRatio for r in dataset.geometry.rooms]).mean()**2)
	return predictors

def getDummyLambdaStats():
	dummyLambda = dict()
	dummyLambda["dummy"] = (lambda x : x)
	return dummyLambda

def xFunctions():
	xFunctions = dict()
	xFunctions["none"] = (lambda x: x)
	xFunctions["sqrt"] = (lambda x : math.sqrt(x))
	xFunctions["log"] = (lambda x: math.log(x))
	return xFunctions

def yFunctions():
	yFunctions = dict()
	yFunctions["none"] = (lambda y: y)
	yFunctions["sqrt"] = (lambda y: math.sqrt(y))
	yFunctions["log"] = (lambda y: math.log(y))
	return yFunctions

def formatFunctionLabel(fun,label):
	if fun=="none":
		return label
	else:
		return fun+"("+label+")"

def plotAndSave(xs,ys,xLabel,yLabel,corrStats,plotFolder,name):
	fig = plt.figure()
	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	fit = np.polyfit(xs,ys,1)
	fit_fn = np.poly1d(fit)
	support_range = np.arange(min(xs), max(xs),0.1) 
	# fit_fn is now a function which takes in x and returns an estimate for y
	plt.plot(xs,ys, 'ro', support_range, fit_fn(support_range), '-')
	prs,pvalue = pearsonr(xs,ys)
	corrStats.append([xLabel,yLabel,prs,pvalue])
	if abs(prs) > 0.65:
		print name
		print prs, pvalue
		fig.savefig(join(plotFolder,"correlation",name)+".png", bbox_inches='tight')
		pattern = Image.open(join(plotFolder,"correlation",name)+".png", "r").convert('RGBA')
		size = width, height = pattern.size
		draw = ImageDraw.Draw(pattern,'RGBA')
		font = ImageFont.truetype("OpenSans-Regular.ttf", 16)
		draw.text((80,525), 'Pearson: ' + str(round(prs,3)), fill=(0, 0, 0, 255), font=font)
		draw.text((500,525), 'P-Value: '+ str(round(pvalue,5)), fill=(0, 0, 0, 255), font = font)
		pattern.save(join(plotFolder,"correlation",name)+".png")
	plt.close(fig)

def plotIterator(datasets,layoutFolder,plotFolder,corrStats,predictedStats,predictedStatsAttrs,isPredictedStatsAttrsDummy):
	attrStats = getAttrStats()
	predictors = getPredictors()
	# error stats
	for eName, eLambda in predictedStats.iteritems():
		for aName, aLambda in predictedStatsAttrs.iteritems():
			for sName, sLambda in attrStats.iteritems():
				for pName, pLambda in predictors.iteritems():
					for yFName, yFLambda in yFunctions().iteritems():
						for xFName, xFLambda in xFunctions().iteritems():
							xs = []
							ys = []
							for d in datasets:			
								if isdir(join(layoutFolder, d.name)) and d.name[-10:]!="furnitures":
									x = xFLambda(pLambda(d))
									y = yFLambda(sLambda(aLambda(eLambda(d))))
									#print d.name, x, y
									xs.append(x)
									ys.append(y)
							#plt.plot(xs,ys,'ro')
							xLabel = formatFunctionLabel(xFName,pName)
							if not isPredictedStatsAttrsDummy:
								yLabel = formatFunctionLabel(yFName,eName+"."+aName+"."+sName)
								name = xFName+"-"+pName+"-"+yFName+"-"+eName+"."+aName+"."+sName#,prs,pvalue
							else:
								yLabel = formatFunctionLabel(yFName,eName+"."+sName)
								name = xFName+"-"+pName+"-"+yFName+"-"+eName+"."+sName
							plotAndSave(xs,ys,xLabel,yLabel,corrStats,plotFolder,name)	

def plotGraphs(datasets,layoutFolder,plotFolder):
	corrStatsFile = open(join(plotFolder, "corrStats.csv"), "w")
	corrStatsFile.write("x, y, Pearson, P-Value\n")
	corrStats = []
	errorTypes = getErrorTypes()
	runStats = getRunStats()
	errorAttrs = getErrorAttrs()
	dummyErrorAttrs = getDummyLambdaStats()
	plotIterator(datasets,layoutFolder,plotFolder,corrStats,errorTypes,errorAttrs,isPredictedStatsAttrsDummy=False)
	#plotIterator(datasets,layoutFolder,plotFolder,corrStats,runStats,dummyErrorAttrs,isPredictedStatsAttrsDummy=True)
	corrStats.sort(key=lambda x:abs(x[2]), reverse=True)
	for elem in corrStats:
		corrStatsFile.write(elem[0]+','+elem[1]+','+str(elem[2])+','+str(elem[3])+'\n')
	corrStatsFile.close()

def analyzeDatasets(runsFolder, layoutFolder, plotFolder):
	datasets = []
	for f in listdir(runsFolder):
		if isdir(join(runsFolder, f)):# and "furnitures" not in f:
			datasets.append(loadDataset(f, runsFolder))
	for d in datasets:
		if isdir(join(layoutFolder, d.name)):
			print d.name
			loadGeometry(d, join(layoutFolder, d.name, d.name)+".xml")	
			print len(d.runs)
			#print d.geometry
	plotGraphs(datasets,layoutFolder,plotFolder)

def buildcsv(outputs):
	csv=open('errorscsv.csv','w')
	csv.write('DATASET, MEAN-T, STD-T, MIN-T, MAX-T, MEAN-R, STD-R, MIN-R, MAX-R, NUMMEASURES\n')

	for f in listdir(outputs):
		if isdir(join(outputs,f)):
			for r in listdir(join(outputs,f)):

				if exists(join(join(outputs,f),r+'/Errors/RE/T.errors')):
					file=open(join(join(outputs,f),r+'/Errors/RE/T.errors'),'r')
					first=True

					for line in file:
						words=line.split(', ')
						if first is True:
							first=False
						else:
							csv.write(f+', '+words[0]+', '+words[1]+', '+words[2]+', '+words[3])

					file.close()

				if exists(join(join(outputs,f),r+'/Errors/RE/R.errors')):
					file=open(join(join(outputs,f),r+'/Errors/RE/R.errors'),'r')
					first=True

					for line in file:
						if first is True:
							first=False
						else:
							csv.write(', '+line)

					file.close()

	csv.close()

if __name__ == '__main__':
	#buildcsv(sys.argv[1])
	analyzeDatasets(sys.argv[1], sys.argv[2], sys.argv[3])
