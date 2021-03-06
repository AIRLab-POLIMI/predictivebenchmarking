''' Filters the redundant data within each run when the robot is stuck somewhere "thinking" where to go,
or where the exploration has actually ended, to avoid misleading error values. '''

import sys,argparse
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
					print join(runsPath, d, r, d)+"Out.log"
					outLog = open(join(runsPath, d, r, d)+"Out.log", "r")
					lines = outLog.readlines()
					outLog.close()
					last_line = len(lines)
					words = lines[-1].split(" ")
					try:
						test = words[8]
					except IndexError:
						last_line -= 1
					outLog = open(join(runsPath, d, r, d)+"Out.log", "w")
					for i in range(0,last_line):  
						outLog.write(lines[i])
					outLog.close()

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='This tool removes the last line of the SLAM output log file from each run in <runs_outputs_folder>, in order to avoid parsing errors due to untimely termination of the exploration process.')
	parser.add_argument('runs_output_folder',help='the path where the runs of each dataset are located')
	args = parser.parse_args()
	adjustMetric(args.runs_output_folder)
