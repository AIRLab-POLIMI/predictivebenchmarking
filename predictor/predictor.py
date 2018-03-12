import argparse
from os import listdir
from os.path import join,exists, isdir,isfile
from analyzer import loadModels,processVoronoiGraph

def predictDatasets(predictFolder, models):
	print "transError.mean.mean = "+str(models["transError.mean.mean"]["voronoi_traversal_distance"].coef_[0])+"*X+"+str(models["transError.mean.mean"]["voronoi_traversal_distance"].intercept_[0])
	print "transError.mean.std = "+str(models["transError.mean.std"]["voronoi_traversal_distance"].coef_[0])+"*X+"+str(models["transError.mean.std"]["voronoi_traversal_distance"].intercept_[0])
	print "rotError.mean.mean = "+str(models["rotError.mean.mean"]["voronoi_traversal_distance"].coef_[0])+"*X+"+str(models["rotError.mean.mean"]["voronoi_traversal_distance"].intercept_[0])
	print "rotError.mean.std = "+str(models["rotError.mean.std"]["voronoi_traversal_distance"].coef_[0])+"*X+"+str(models["rotError.mean.std"]["voronoi_traversal_distance"].intercept_[0])
	for f in listdir(predictFolder):
		if isfile(join(predictFolder,f)) and f[-5:]=="world":
			datasetName = f[:-6]
			voronoi, voronoiCenter, voronoiDistance, voronoiTopVisits, voronoiRotation,voronoiStats = processVoronoiGraph(datasetName, join(predictFolder, "voronoi"), join(predictFolder, datasetName)+".world", join(predictFolder, datasetName)+".png")
			print datasetName
			print voronoiDistance
			print models["transError.mean.mean"]["voronoi_traversal_distance"].predict(voronoiDistance)
			print models["transError.mean.std"]["voronoi_traversal_distance"].predict(voronoiDistance)
			print models["rotError.mean.mean"]["voronoi_traversal_distance"].predict(voronoiDistance)
			print models["rotError.mean.std"]["voronoi_traversal_distance"].predict(voronoiDistance)

if __name__ == '__main__':
	#buildcsv(sys.argv[1])
    parser = argparse.ArgumentParser(description='This is the main tool of the RPPF. Its task is to analyze the error data of the different runs of the training datasets, correlate it with properties extracted from such datasets, build a prediction model and use it to predict the error data of the desired test datasets. Please refer to the wiki for extended documentation.')
    #parser.add_argument('layouts_folder',help='the folder in which the layout information of each training dataset, as extracted by the Layout Extractor, is stored')
    parser.add_argument('models_folder',help='the output folder in which the tool stores the trained models')
    parser.add_argument('datasets_to_predict_folder',help='the folder in which all the data related to the datasets of the test set for which the tool must perform predictions is stored')
    args = parser.parse_args()
    #models = analyzeDatasets(args.runs_folder,args.layouts_folder,args.voronoi_folder,args.world_folder,args.plot_folder)
    #saveModels(models,args.models_folder)
    models = loadModels(args.models_folder)
    predictDatasets(args.datasets_to_predict_folder, models)
