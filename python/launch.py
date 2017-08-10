import sys
import select
import signal
import time
from os import killpg, getpgid, setsid, makedirs, listdir, getcwd, remove
from os.path import basename,join, exists, isfile, dirname
from subprocess import Popen, PIPE, check_call
from threading import Timer, Thread
from generateAll import generateAll
from compare_images import compare_images
from PIL import Image

minutes=0
first_time=True
seconds_mapsave=600
maxmapsave=18
count=0
threshold=5
num_runs=5
global project_path


def killProcess(p,folder):
	'''
	Kills the process of the launchNavigation and calls generateAll to generate relations,errors and trajectories
	'''
	killpg(getpgid(p.pid),signal.SIGTERM)


def getMap(dataset_name,p,folder):
	'''
	Saves the map and checks if the exploration is complete. 
	This is done by comparing the last two saved images.
	If this functions has been called more than maxmapsave then the exploration is killed.
	Otherwise it calls itself again to be triggerd after seconds_mapsave 
	'''
	global minutes
	global first_time
	global maxmapsave
	global count
	count+=1

	print 'COUNT '+str(count)

	if not exists(join(folder,"Maps/")):
		makedirs(join(folder,"Maps/"))

	getmapString="rosrun map_server map_saver -f "+folder+"Maps/"+str(minutes)+"Map"
	print 'PRIMA DI POPEN'
	process=check_call(getmapString, shell=True, preexec_fn=setsid)
	#process.wait()
	try:
		Image.open(folder+"Maps/"+str(minutes)+"Map.pgm").save(folder+"Maps/"+str(minutes)+"Map.png")
		remove(folder+"Maps/"+str(minutes)+"Map.pgm")
	except IOError:
		print("cannot convert", infile)


	
	if first_time:
		minutes+=seconds_mapsave/60
		first_time=False
		Timer(seconds_mapsave,getMap,[dataset_name,p,folder]).start()
	else:
		print 'INSIDE ELSE'
		print 'MAXMAPSAVE ' + str(maxmapsave)
		diff=threshold

		try:
			diff = compare_images(folder+"Maps/"+str(minutes)+"Map.png",folder+"Maps/"+str(minutes-seconds_mapsave/60)+"Map.png")
			print 'DIFFERENCE VALUE: '+ str(diff)
		except ValueError:
			print 'Compare images error'

		if diff < threshold or maxmapsave < count or exists(join(folder,"explorer/robot_0/exploration.log")):
			print 'KILL PROCESS'
			getmapString="rosrun map_server map_saver -f "+folder+"Maps/"+str(minutes)+"Map"
			process=check_call(getmapString, shell=True, preexec_fn=setsid)
			#process.wait()
			try:
				Image.open(folder+"Maps/"+str(minutes)+"Map.pgm").save(folder+"Maps/"+str(minutes)+"Map.png")
				remove(folder+"Maps/"+str(minutes)+"Map.pgm")
			except IOError:
				print("cannot convert", infile)
			killProcess(p,folder)
			return
		else:
			minutes+=seconds_mapsave/60
			Timer(seconds_mapsave,getMap,[dataset_name,p,folder]).start()



		

def launchNavigation(world,folder):
	'''
	Calls the launch file and starts the exploration, waits until the process is done
	'''
	try:
		worldfile=basename(world)
		launchString="roslaunch "+project_path+"/launch/exploreambient.launch worldfile:="+world+" \
			outputfile:="+folder+worldfile[:-6]+"Out.log \
			bag:="+folder+worldfile[:-6]+".bag \
			log_path:="+folder+""

		p=Popen(launchString, shell=True, preexec_fn=setsid)
		Timer(seconds_mapsave,getMap,[folder,p,folder]).start()
		p.wait()
		time.sleep(20)
		generateAll(folder)
		return
	except KeyboardInterrupt:
		print 'KILL PROCESS'
		killProcess(p,folder)
		time.sleep(20)
		generateAll(folder)
		return
	

def fiveRuns(world,folder):
	'''
	Given a world and a folder runs 5 explorations of that environment
	'''
	global minutes
	global first_time
	global count
	maxrun=0

	for f in listdir(folder):
		if int(f[3:]) >= maxrun:
			maxrun=int(f[3:])
	
	for i in range(maxrun+1,maxrun+1+num_runs):
		minutes=seconds_mapsave/60
		first_time=True
		count=0
		if not exists(join(folder,"run"+str(i)+"/")):
			makedirs(join(folder,"run"+str(i)+"/"))
		print 'START'
		launchNavigation(world,join(folder,"run"+str(i)+"/"))
		print 'END'

def exploreWorlds(worlds):
	'''
	Given a folder with worlds file it runs 5 times each environment exploration
	'''
	wheretosaveoutputs=project_path+"/runs/outputs/"
	for f in listdir(worlds):
		if isfile(join(worlds, f)):
			if f[-6:] == ".world":
				if not exists(join(wheretosaveoutputs,f[:-6])):
					makedirs(join(wheretosaveoutputs,f[:-6]))

				fiveRuns(join(worlds, f),join(wheretosaveoutputs,f[:-6]))

if __name__ == '__main__':
    # retrieve current path
	global project_path
	project_path = dirname(getcwd())
	exploreWorlds(sys.argv[1])
