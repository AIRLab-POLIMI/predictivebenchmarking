from __future__ import division
import numpy as np
import util.layout as lay
import util.GrafoTopologico as gtop
import util.transitional_kernels as tk

from util import pickle_util as pk
import parameters as params
import pickle
import datetime as dt
import os
import shutil
import glob
from structures import room

def main():
	# retrieve the necessary settings
	path_par = params.Path_obj()
	par = params.Parameter_obj()
	# identifies the directory where we're going to save the processed images
	our_time = str(dt.datetime.now())[:-10].replace(' ','@')
	SAVE_FOLDER = os.path.join('./log', our_time)
	if not os.path.exists(SAVE_FOLDER):
		os.mkdir(SAVE_FOLDER)
	# name of the file we're going to process
	metricMap = "./office_h.png"

	# initialize data structure containing features of all rooms
	rooms_features = []

	#----------------------------ROOM LAYOUT IDENTIFICATION-----------------------------------
	# retrieve rooms, clusters...
	(rooms, cellClusters, extremes, colors, spaces) = lay.get_layout(metricMap, par.minVal, par.maxVal, par.rho, par.theta, par.thresholdHough, par.minLineLength, par.maxLineGap, par.eps, par.minPts, par.h, par.minOffset, par.minLateralSeparation,par.apertureSize, par.t, par.m, SAVE_FOLDER)

	# for each room, compute and store its relevant features

	for r in rooms:
		room_feature = room.Room(r,par.scaling_factor)
		rooms_features.append(room_feature)
		room_feature.printFeatures()



if __name__ == '__main__':
	main()
