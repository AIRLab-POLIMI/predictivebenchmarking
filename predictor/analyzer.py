import sys
import cv2
from PIL import Image,ImageDraw,ImageFont
from os import listdir
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
from scipy.stats import pearsonr
from sklearn import linear_model
from sklearn.model_selection import KFold, cross_val_score
from shapely.geometry import Polygon, Point
from skimage.morphology import skeletonize
from skimage import img_as_ubyte

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
	myDataset.topology = G

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

def timestampedTraversal(voronoi, center):
	n1=dt.datetime.now()
	T = nx.dfs_tree(voronoi, center)
	n2=dt.datetime.now()
	delta = (n2-n1).microseconds 
	if delta < 500000:
		return delta
	else:
		return -1

def getPredictors():
	predictors = dict()
	#predictors["traversalTime"] = (lambda dataset: timestampedTraversal(dataset.voronoi, dataset.voronoiCenter))
	predictors["traversalTime"] = (lambda dataset: (dataset.voronoiTime))
	predictors["area"] = (lambda dataset: (dataset.geometry.shape.area))
	predictors["perimeter"] = (lambda dataset: (dataset.geometry.shape.perimeter))
	predictors["wallRatio"] = (lambda dataset: (dataset.geometry.shape.wallRatio))
	predictors["numRooms"] = (lambda dataset: (len(dataset.geometry.rooms)))
	predictors["totalTime"] = (lambda dataset: (dataset.perfStats.totalTime.mean))
	predictors["totalLength"] = (lambda dataset : (dataset.perfStats.totalLength.mean))
	predictors["avgRoomArea"] = (lambda dataset: np.array([r.shape.area for r in dataset.geometry.rooms]).mean()**2)
	predictors["avgRoomPerimeter"] = (lambda dataset: np.array([r.shape.perimeter for r in dataset.geometry.rooms]).mean()**2)
	predictors["avgRoomWallRatio"] = (lambda dataset: np.array([r.shape.wallRatio for r in dataset.geometry.rooms]).mean()**2)
	predictors["roomPerimeter"] = 	(lambda dataset: np.array([r.shape.perimeter for r in dataset.geometry.rooms]).sum())
	predictors["nodes"] = (lambda dataset: dataset.voronoiStats.nodes)
	predictors["edges"] = (lambda dataset: dataset.voronoiStats.edges)
	predictors["avg_shortest_path_length"] = (lambda dataset : dataset.voronoiStats.avg_shortest_path_length)
	predictors["density"] = (lambda dataset : dataset.voronoiStats.density)
	predictors["diameter"] = (lambda dataset: dataset.voronoiStats.diameter)
	predictors["radius"] = (lambda dataset: dataset.voronoiStats.radius)
	predictors["numBifurcationPoints"] = (lambda dataset: len(get_bifurcation_points(dataset.voronoi)))
	predictors["avg_betweenness_centrality"] = (lambda dataset: dataset.voronoiStats.betweenness_centrality.mean())
	predictors["avg_eigenvector_centrality"] = (lambda dataset: dataset.voronoiStats.eigenvector_centrality.mean())
	predictors["avg_katz_centrality"] = (lambda dataset: dataset.voronoiStats.katz_centrality.mean())
	predictors["avg_closeness_centrality"] = (lambda dataset: dataset.voronoiStats.closeness_centrality.mean())
	predictors["std_betweenness_centrality"] = (lambda dataset: dataset.voronoiStats.betweenness_centrality.std())
	predictors["std_eigenvector_centrality"] = (lambda dataset: dataset.voronoiStats.eigenvector_centrality.std())
	predictors["std_katz_centrality"] = (lambda dataset: dataset.voronoiStats.katz_centrality.std())
	predictors["std_closeness_centrality"] = (lambda dataset: dataset.voronoiStats.closeness_centrality.std())
	#TODO: provare con la somma dei lati di ogni stanza (quindi un "perimetro" generalizzato)
	return predictors

def getDummyLambdaStats():
	dummyLambda = dict()
	dummyLambda["dummy"] = (lambda x : x)
	return dummyLambda

def xFunctions():
	xFunctions = dict()
	xFunctions["none"] = (lambda x: x)
	#xFunctions["sqrt"] = (lambda x : math.sqrt(x))
	#xFunctions["log"] = (lambda x: math.log(x))
	return xFunctions

def yFunctions():
	yFunctions = dict()
	yFunctions["none"] = (lambda y: y)
	#yFunctions["sqrt"] = (lambda y: math.sqrt(y))
	#yFunctions["log"] = (lambda y: math.log(y))
	return yFunctions

def formatFunctionLabel(fun,label):
	if fun=="none":
		return label
	else:
		return fun+"("+label+")"

def multiCorrelate(datasets, layoutFolder):
	nsamples = len(datasets)
	xs = np.empty([nsamples,3])
	ys = np.empty([nsamples,1])
	for i in range(0,nsamples):
		d = datasets[i]			
		if isdir(join(layoutFolder, d.name)):# and d.name[-10:]!="furnitures":
			print d.name
			xs[i][0] = d.voronoiTime
			xs[i][1] = d.voronoiTopVisits 
			xs[i][2] = d.voronoiStats.edges#len(get_bifurcation_points(d.voronoi))
			ys[i][0] = d.perfStats.transError.mean.mean
	lm = linear_model.LinearRegression()
	print xs
	print ys
	model = lm.fit(xs,ys)
	strategy = KFold(n_splits=10,shuffle=True)
	rsquared = lm.score(xs,ys)
	print rsquared
	mses = np.sqrt(np.abs(cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='neg_mean_squared_error')))
	print mses
	print mses.mean()

def plotAndSave(xs,ys,xLabel,yLabel,corrStats,plotFolder,name):
	fig = plt.figure()
	plt.xlabel(xLabel)
	plt.ylabel(yLabel)
	fit = np.polyfit(xs,ys,1)
	fit_fn = np.poly1d(fit)
	support_range = np.arange(min(xs), max(xs),0.1) 
	# fit_fn is now a function which takes in x and returns an estimate for y
	plt.plot(xs,ys, 'ro', support_range, fit_fn(support_range), '-')
	lm = linear_model.LinearRegression()
	nsamples = len(xs)
	xs = np.array(xs).reshape(nsamples,1)
	ys = np.array(ys).reshape(nsamples,1)
	model = lm.fit(xs,ys)
	strategy = KFold(n_splits=10,shuffle=True)
	#prs,pvalue = pearsonr(xs,ys)
	rsquared = lm.score(xs,ys)
	corrStats.append([xLabel,yLabel,rsquared])
	#if abs(prs) > 0.5:
	print name
	print rsquared
	mses = np.sqrt(np.abs(cross_val_score(lm, xs, ys, cv=strategy, n_jobs = -1, scoring='neg_mean_squared_error')))
	print mses
	print mses.mean()
	fig.savefig(join(plotFolder,"correlation",name)+".png", bbox_inches='tight')
	pattern = Image.open(join(plotFolder,"correlation",name)+".png", "r").convert('RGBA')
	size = width, height = pattern.size
	draw = ImageDraw.Draw(pattern,'RGBA')
	font = ImageFont.truetype("OpenSans-Regular.ttf", 16)
	draw.text((80,525), 'rsquared: ' + str(round(rsquared,3)), fill=(0, 0, 0, 255), font=font)
	#draw.text((500,525), 'P-Value: '+ str(round(pvalue,5)), fill=(0, 0, 0, 255), font = font)
	pattern.save(join(plotFolder,"correlation",name)+".png")
	# we must also store the xs and ys in a table
	buildcsv(join(plotFolder,"correlation",name)+".csv",xLabel,yLabel,xs,ys)
	plt.close(fig)

def buildcsv(correlationFileName, xLabel, yLabel, xs, ys):
	csv=open(correlationFileName, 'w')
	csv.write(xLabel+','+yLabel+'\n')
	for r in range(0, len(xs)):
		csv.write(str(xs[r][0])+','+str(ys[r][0])+'\n')
	csv.close()

def plotIterator(datasets,layoutFolder,plotFolder,corrStats,predictedStats,predictedStatsAttrs,isPredictedStatsAttrsDummy):
	attrStats = getAttrStats()
	predictors = getPredictors()
	# error stats
	exclude_datasets = []
	for eName, eLambda in predictedStats.iteritems():
		for aName, aLambda in predictedStatsAttrs.iteritems():
			for sName, sLambda in attrStats.iteritems():
				for pName, pLambda in predictors.iteritems():
					for yFName, yFLambda in yFunctions().iteritems():
						for xFName, xFLambda in xFunctions().iteritems():
							xs = []
							ys = []
							for d in datasets:			
								if isdir(join(layoutFolder, d.name)) and not (d.name in exclude_datasets):# and d.name[-10:]!="furnitures":
									#print d.name
									x = xFLambda(pLambda(d))
									y = yFLambda(sLambda(aLambda(eLambda(d))))
									if y != -1:
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
	corrStatsFile.write("x, y, rsquared\n")
	corrStats = []
	errorTypes = getErrorTypes()
	runStats = getRunStats()
	errorAttrs = getErrorAttrs()
	dummyErrorAttrs = getDummyLambdaStats()
	plotIterator(datasets,layoutFolder,plotFolder,corrStats,errorTypes,errorAttrs,isPredictedStatsAttrsDummy=False)
	#plotIterator(datasets,layoutFolder,plotFolder,corrStats,runStats,dummyErrorAttrs,isPredictedStatsAttrsDummy=True)
	corrStats.sort(key=lambda x:abs(x[2]), reverse=True)
	for elem in corrStats:
		corrStatsFile.write(elem[0]+','+elem[1]+','+str(elem[2])+'\n')
	corrStatsFile.close()

''' Outline of the algorithm (TICK-TOCK mechanism):
# black == occupied, white == free
1) TICK phase: I "look around" the node where I'm currently standing with the find_nearest_node
function, looking for the nearest (euclidean distance) black pixel as that's the nearest frontier. Then, 
I apply the shortest_path algorithm to identify a set of nodes on the voronoi graph that lead me towards
the nearest frontier. 
2) TOCK phase: For each node on the shortest path, I apply a "line-of-sight-visiting-algorithm". That is, 
I look around them to retrieve all the black pixels that are within a certain (laser) distance; for each of
them, I ask whether it belongs to the same room (using the TG) of the "current" node on the shortest path
and if so I assume it's visible, so it gets marked as visited (i.e. colored white on the image).
Improvement: the line-of-sight mechanism is not very pretty, it doesn't take into account the direction 
that the robot is facing.'''

def mapPixelsToRooms(myDataset, image, height):
	pixelRoomMap = {}
	black_pixels = np.argwhere(image == 0)
	for p in black_pixels:
		# remember: pixels are in <y,x> format with y increasing as rows
		r = getRoomOfPixel(myDataset, p, height)
		pixelRoomMap[height-p[0],p[1]] = r
	return pixelRoomMap

def getRoomOfPixel(myDataset, currentPixel, height):
	idx = -1
	r = 0
	while r < len(myDataset.geometry.rooms) and idx==-1:
		if myDataset.geometry.rooms[r].boundingPolygon.polygon.contains(Point(currentPixel[0],height-currentPixel[1])):
			idx = r
		r+=1
	return idx 

def retrieveNearbyPixels(TG, image, currentPixel, previousPixel, laserLength):
	black_pixels = np.argwhere(image == 0)
	ref_angle = math.atan2(currentPixel[0]-previousPixel[0], currentPixel[1]-previousPixel[1])
	if ref_angle < 0:
		ref_angle += 2*np.pi
	distances = np.sqrt((black_pixels[:,0] - currentPixel[0]) ** 2 + (black_pixels[:,1] - currentPixel[1]) ** 2)
	angles = np.arctan2(black_pixels[:,0] - currentPixel[0], black_pixels[:,1]-currentPixel[1])
	angles = [a if a > 0 else a+2*np.pi for a in angles]
	lgt = len(distances)
	indices = [i for i in range(0, lgt) if distances[i] < laserLength and (np.pi - math.fabs(math.fabs(ref_angle - angles[i]) - np.pi))<3.0/4.0*np.pi]
	return black_pixels[indices]

def retrieveVisiblePixels(TG, image, gtImage, totalNodes, currentPixel, previousPixel, laserLength, pixelRoomMap):
	height, width = image.shape
	nearbyPixels = retrieveNearbyPixels(TG, image, currentPixel, previousPixel, laserLength)
	# but are these actually visible? we approximate this by checking whether they belong to the same room
	visiblePixels = []
	# the idea is the following: if the two pixels are visible from each other, when drawing a white 
	# line between the two the number of black points at the end should only decrease by two
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

def lineOfSight(VG, TG, image, gtImage, totalNodes, currentPixel, previousPixel, voronoiNodesMap, voronoiNodesReverseMap, laserLength, pixelRoomMap):
	height, width = image.shape
	visiblePixels = retrieveVisiblePixels(TG, image, gtImage, totalNodes, currentPixel, previousPixel, laserLength, pixelRoomMap)
	visibleNodes = pixelsToNodes(visiblePixels, voronoiNodesMap, height)
	markVisiblePixelsAsVisited(image, visiblePixels)
	nseen = markVisibleNodesAsVisited(VG, visibleNodes)
	return visibleNodes, nseen

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

def exploreVoronoiGraph(VG, TG, myDataset, image, gtImage, start, voronoiNodesMap, voronoiNodesReverseMap, laserLength, scale, speed):
	# initialize the correspondence between pixels of the voronoi graph and the room to which they belong
	height, width = image.shape
	pixelRoomMap = mapPixelsToRooms(myDataset, image, height)
	backtorgb = cv2.cvtColor(gtImage,cv2.COLOR_GRAY2RGB) 
	initNodeVisitedStatus(VG)
	totalNodes = len(VG.nodes())
	currentPixel = start
	numVisitedNodes = 0
	numSeenNodes = 0
	totalDistance = 0
	# line-of-sight: identify and mark as visited the pixels that are visible from the current location
	visibleNodes, nseen = lineOfSight(VG, TG, image, gtImage, totalNodes, currentPixel, (currentPixel[0]+1,currentPixel[1]), voronoiNodesMap, voronoiNodesReverseMap, laserLength, pixelRoomMap)
	numSeenNodes += nseen
	visitedPixels = []
	numStops = 0
	while numSeenNodes < totalNodes:
		# next frontier
		nearestPixel = retrieveNearestFrontier(image, currentPixel)
		nearestNode = voronoiNodesMap[height-nearestPixel[0], nearestPixel[1]]
		currentNode = voronoiNodesMap[height-currentPixel[0], currentPixel[1]]
		shortest_path = nx.shortest_path(VG, currentNode, nearestNode)
		numStops += 1
		for n in shortest_path:
			previousPixel = currentPixel
			previousNode = currentNode
			currentPixel = (height-voronoiNodesReverseMap[n][0],voronoiNodesReverseMap[n][1])
			currentNode = n
			visitedPixels.append(currentPixel)
			visibleNodes, nseen = lineOfSight(VG, TG, image, gtImage, totalNodes,currentPixel, previousPixel, voronoiNodesMap, voronoiNodesReverseMap, laserLength, pixelRoomMap)
			# add to the number of seen nodes the new ones we have actually seen in line of sight
			numSeenNodes += nseen
			# and increase the number of times this current node has been visited
			VG.node[n]['nvisits'] += 1
			numVisitedNodes += 1
			totalDistance += node_distance(VG,previousNode,currentNode)
		currentPixel = nearestPixel
		#gray_pixels = np.argwhere(image == 127)
		#backtorgb[currentPixel[0],currentPixel[1]] = (0,255,0)
		#for p in gray_pixels:
		#	backtorgb[p[0],p[1]] = (0,0,255)
		#for p in visitedPixels:
		#	backtorgb[p[0],p[1]] = (255,0,0)
		#cv2.imshow("test", backtorgb)
		#cv2.waitKey(0)
		# speed : pixel / s
	#totalTime = totalDistance / speed + numStops*2 # s	
	return totalDistance/scale, sum(getTopVisitedNodes(VG,40))#40 best

def createVoronoiGraphFromImage(myDataset, imagePath, worldPath):
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
	#cv2.imshow("test",image)
	#cv2.waitKey(0)
	robotX, robotY, scale = retrieveExplorationStartingPoint(worldPath, width, height)
	#print height
	#print width
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

def loadVoronoiGraph(myDataset, voronoiPath, worldPath):
	pickleFile = join(voronoiPath, "pickle",myDataset.name)+"_voronoi.pickle"
	imageFile = join(voronoiPath, "images",myDataset.name)+"_voronoi.png"
	if exists(pickleFile):
		Gc = nx.read_gpickle(pickleFile)
	else:
		Gc = createVoronoiGraphFromImage(myDataset, imageFile, worldPath)
		nx.write_gpickle(Gc, pickleFile)
	return Gc


def processVoronoiGraph(myDataset, voronoiPath, worldPath, gtImagePath):
	Gc = loadVoronoiGraph(myDataset, voronoiPath, worldPath)
	gtImage = cv2.imread(gtImagePath,cv2.IMREAD_GRAYSCALE)
	height, width = gtImage.shape
	robotX, robotY, scale = retrieveExplorationStartingPoint(worldPath, width, height)
	voronoiNodesReverseMap = {}
	voronoiNodesMap = {}
	img = np.full((height, width), 255, np.uint8)
	for n in Gc.nodes():
		voronoiNodesReverseMap[n] = Gc.node[n]['pos'][1], Gc.node[n]['pos'][0]
	for k,v in voronoiNodesReverseMap.iteritems():
		voronoiNodesMap[v] = k
		img[height-v[0],v[1]] = 0
	# we also need to figure out which node is the closest to the starting point of the exploration
	nearestPixel = find_nearest_node(img, robotX, robotY)
	nearestNode = voronoiNodesMap[height-nearestPixel[0],nearestPixel[1]]
	myDataset.voronoi = Gc
	myDataset.voronoiCenter = nearestNode
	#plt.clf()
	#plt.cla()
	#plt.close()
	#plt.axis('equal')
	#nx.draw_networkx_nodes(Gc,pos,node_color='b',node_size=1)
	#nx.draw_networkx_edges(Gc,pos,edge_color='r',width=1.0)
	#plt.show()
	speed = 0.85 # m/s
	totalTime, topVisits = exploreVoronoiGraph(Gc, myDataset.topology, myDataset, img, gtImage, nearestPixel, voronoiNodesMap, voronoiNodesReverseMap, 30*scale, scale, speed*scale)
	myDataset.voronoiTime = totalTime
	myDataset.voronoiTopVisits = topVisits
	myDataset.voronoiStats = GraphStats(Gc)
	print "Voronoi Time "+str(totalTime)

def node_distance(G,u,v): 
	return np.sqrt((G.node[u]['pos'][0]-G.node[v]['pos'][0])**2+(G.node[u]['pos'][1]-G.node[v]['pos'][1])**2)

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

def remove_flow_through(graph):
	for n in graph.nodes():
		neighbors = graph.neighbors(n)
		if len(neighbors) == 2:
			w1 = graph.get_edge_data(n,neighbors[0])['weight']
			w2 = graph.get_edge_data(n,neighbors[1])['weight']
			graph.remove_node(n)
			graph.add_edge(neighbors[0], neighbors[1],weight=w1+w2)

def analyzeDatasets(runsFolder, layoutFolder, voronoiFolder, worldFolder, plotFolder):
	datasets = []
	for f in listdir(runsFolder):
		if isdir(join(runsFolder, f)):# and "furnitures" not in f:
			datasets.append(loadDataset(f, runsFolder))
	for d in datasets:
		if isdir(join(layoutFolder, d.name)):
			print d.name
			loadGeometry(d, join(layoutFolder, d.name, d.name)+".xml")	
			#if isfile(join(voronoiFolder, d.name)+"_voronoi.png"):
			processVoronoiGraph(d, voronoiFolder, join(worldFolder, d.name)+".world", join(worldFolder, d.name)+".png")
			print len(d.runs)
			#print d.geometry
	#multiCorrelate(datasets, layoutFolder)
	plotGraphs(datasets,layoutFolder,plotFolder)

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
	analyzeDatasets(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
