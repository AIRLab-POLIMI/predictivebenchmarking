import argparse
from os import listdir
from os.path import join,exists, isdir,isfile
from analyzer import loadModels,processVoronoiGraph

def predictDatasets(predictFolder, models):
	for f in listdir(predictFolder):
		if isfile(join(predictFolder,f)) and f[-5:]=="world":
			datasetName = f[:-6]
			voronoi, voronoiCenter, voronoiDistance, voronoiTopVisits, voronoiRotation,voronoiStats = processVoronoiGraph(datasetName, join(predictFolder, "voronoi"), join(predictFolder, datasetName)+".world", join(predictFolder, datasetName)+".png")
			print datasetName
			print voronoiDistance
			print models["transError.mean.mean"][0].predict(voronoiDistance)

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
    #models = analyzeDatasets(args.runs_folder,args.layouts_folder,args.voronoi_folder,args.world_folder,args.plot_folder)
    #saveModels(models,args.models_folder)
    models = loadModels(args.models_folder)
    predictDatasets(args.datasets_to_predict_folder, models)