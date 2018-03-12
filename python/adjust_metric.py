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
					#if not(isfile(join(runsPath, d, r, d)+"_filtered.log")): # recompute
						#shutil.copyfile(join(runsPath, d, r, d)+".log", join(runsPath, d, r, d)+".log.bak")
					gtLog = open(join(runsPath, d, r, d)+".log", "r")
					print join(runsPath, d, r, d)+".log"
					newContent = []
					prev_line = ["", "", "", ""]
					# if the robot hasn't moved between two poses, keep the latest 
					for line in reversed(gtLog.readlines()):
						words = line.split(' ')
						if words[0]!='\n':
							if not(words[1]==prev_line[1] and words[2]==prev_line[2] and words[3]==prev_line[3]):
								# something changed, store line
								newContent.append(str(float(words[0]))+" "+words[1]+" "+words[2]+" "+words[3])
							prev_line = words
					# overwrite GT log
					# NOTE: THIS DOESN'T OVERWRITE .BAG FILE ON PURPOSE, AS WE MAY NEED (FOR SOME REASON)
					# TO REVERT THESE CHANGES IN THE FUTURE! IT ONLY OVERWRITES THE LOG FILE, WHICH CAN BE
					# RECREATED! FOR THE SAME REASON, IT DOESN'T MODIFY THE SLAM OUTPUT!
					gtLog.close()
					gtLog = open(join(runsPath, d, r, d)+"_filtered.log", "w")
					writeContent = reversed(newContent)
					for item in writeContent:
  						gtLog.write("%s" % item)
  					gtLog.close()
  					# recompute all metricEvaluator errors with the updated logs: NEEDS TO BE UPDATED TO _filtered
  					generateAll(join(runsPath, d, r)+'/', skipGroundTruthConversion=True, skipOrderedRecomputation=True)

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='This tool filters, from each run, the redundant poses that occur whenever the robot stops in a position, either to "think" or because the exploration has ended, and recomputes the error metrics.')
	parser.add_argument('runs_output_folder',help='the path where the runs of each dataset are located')
	args = parser.parse_args()
	adjustMetric(args.runs_output_folder)
