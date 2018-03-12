''' Filters the redundant data within each run when the robot is stuck somewhere "thinking" where to go,
or where the exploration has actually ended, to avoid misleading error values. '''

import sys, argparse
import shutil
from os import listdir
from os.path import basename,join, exists, isfile, isdir, dirname
from generateAll import generateAll

def adjustMetric(runsPath):
	# for each dataset found in the runsPath
	for d in listdir(runsPath):
		if isdir(join(runsPath, d)):
			# for each run
			for r in listdir(join(runsPath, d)):
				if isdir(join(runsPath, d, r)):
					if not isfile(join(runsPath, d, r, "Errors/Original/RE/T.errors")):
  						# recompute all metricEvaluator errors with the updated logs
  						generateAll(join(runsPath, d, r)+'/', skipGroundTruthConversion=True, skipOrderedRecomputation=False)

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='This tool filters, from each run, the redundant poses that occur whenever the robot stops in a position, either to "think" or because the exploration has ended, and recomputes the error metrics.')
	parser.add_argument('runs_output_folder',help='the path where the runs of each dataset are located')
	args = parser.parse_args()
	adjustMetric(args.runs_output_folder)
