'''
This script invokes the layout reconstruction process for each .png file in a specified
directory.
'''

import parameters as par
import time
from os import killpg, getpgid, setsid, makedirs, listdir, getcwd, remove
from os.path import basename,join, exists, isfile, dirname
from minibatch import extractLayout

def isWordInList(list, word):
	try:
		position = list.index(word)
		return True
	except ValueError:
		return False

def parseWorldFile(worldFile):
	file = open(worldFile, 'r')
	scale = 1
	image = ".png"
	for line in file:
		words = line.split(' ')
		if isWordInList(words, "resolution"):
			scale = float(words[-1])
		if isWordInList(words, "bitmap"):
			image = words[-1].replace("\"","")[:-1]
	file.close()
	return scale, image

def main():
	start = time.time()
	''' Initialize default parameters '''
	param_obj = par.Parameter_obj()
	path_obj = par.Path_obj()
	''' Loop through all maps defined in the input dataset folder '''
	for f in listdir(path_obj.datasetInputFolder):
		if isfile(join(path_obj.datasetInputFolder, f)):
			if f[-6:] == ".world": # valid world file
				worldFilePath = join(path_obj.datasetInputFolder, f) 
				param_obj.imageScale, path_obj.inputFileName = parseWorldFile(worldFilePath)
				path_obj.actualOutputFolder = join(path_obj.parentOutputFolder,f[:-6])
				path_obj.outputFileName = join(path_obj.actualOutputFolder,f[:-6])+".xml"
				if not exists(path_obj.actualOutputFolder):
					makedirs(path_obj.actualOutputFolder)
				path_obj.metricMap = join(path_obj.datasetInputFolder, path_obj.inputFileName)
				print path_obj.metricMap
				print len(path_obj.metricMap)
				extractLayout(param_obj, path_obj)
	fine = time.time()
	elapsed = fine-start
	print "Computation lasted %f seconds" % elapsed


if __name__ == '__main__':
	main()
