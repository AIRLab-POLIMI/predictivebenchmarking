import sys,argparse
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from pylab import savefig
import random
import rosbag
from geometry_msgs.msg import Vector3, Quaternion
from nav_msgs.msg import Odometry
import rospy
import roslib
import tf
import math
import numpy as np
from subprocess import Popen, check_call
from scipy.stats import t
from os import listdir, makedirs, getcwd
from os.path import isfile, join, exists, dirname
from writeTextonImage import writeText


def writeGroundTruth(data,outputFile):
	'''
	Given a bag file writes out a .log file with the euclidean poses 
	'''

	groundtruth=open(outputFile+".log","w")

	firstrun=True
	displacementx=0
	displacementy=0

	for topic,msg,t in rosbag.Bag(data).read_messages():
		if topic=="/base_pose_ground_truth":
			position=msg.pose.pose.position
			quaternion=Quaternion()
			quaternion=(msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
			rot=tf.transformations.euler_from_quaternion(quaternion)

			if firstrun:
				displacementx=-position.x
				displacementy=-position.y
				firstrun=False

			if str(msg.header.stamp)[:-9]=="":
				groundtruth.write("0."+str(msg.header.stamp)[-9:]+" "+str(position.x+displacementx)+" "+str(position.y+displacementy)+" "+str(rot[2])+"\n")
			else:
				groundtruth.write(str(msg.header.stamp)[:-9]+"."+str(msg.header.stamp)[-9:]+" "+str(position.x+displacementx)+" "+str(position.y+displacementy)+" "+str(rot[2])+"\n")
	groundtruth.close()

def generateRelationsOandRE(folder,gtfile,seconds=0.5,SLAMFile=None,errorMode="T",alpha=0.99,maxError=0.02,skipOrderedRecomputation=False):
	'''
	Generates the Ordered and the Random relations files
	'''
	project_path = dirname(getcwd())
	pathToMetricEvaluator=project_path+"/metricEvaluator/metricEvaluator"
	ground={}	
	output=gtfile[:-4]

	if seconds=='0':
		print 'Error: Seconds 0'
		return

	if SLAMFile is None:
		SLAMFile = join(folder,output)+"Out.log"

	gt=open(join(folder,gtfile),"r")
	print join(folder,gtfile)

	#builds dictionary with all the ground truth
	for line in gt:
		words = line.split(" ")

		euler=[float(words[1]),float(words[2]),float(words[3])]

		if words[0] not in ground:
			ground[float(words[0])]=euler 
		else:
			ground.update({ float(words[0]): euler })

	gt.close()

	if not exists(join(folder,"Relations/Original/")):
		makedirs(join(folder,"Relations/Original/"))

	#RE
	relationsfileRE=open(folder+"Relations/Original/"+output+"RE.relations","w")

	n_samples = 500
	i=0
	
	while i < n_samples:
			firststamp=float(random.choice(ground.keys()))
			secondstamp=float(random.choice(ground.keys()))
			if firststamp > secondstamp:
				temp=firststamp
				firststamp=secondstamp
				secondstamp=temp
			firstpos=ground[firststamp]
			secondpos=ground[secondstamp]

			rel=getMatrixDiff(firstpos,secondpos)

			x = rel[0,3]
			y = rel[1,3]
			theta = math.atan2(rel[1,0],rel[0,0])

			relationsfileRE.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			i+=1 
	relationsfileRE.close()
	# now we invoke the metric evaluator on this relations file, we read the sample standard 
	# deviation and we exploit it to rebuild a better sample
	if errorMode=='T':
		errorWeights = "{1.0,1.0,1.0,0.0,0.0,0.0}"
	else:
		errorWeights = "{0.0,0.0,0.0,1.0,1.0,1.0}"
	p1=Popen([pathToMetricEvaluator, "-s",SLAMFile, "-r",folder+"Relations/Original/"+output+"RE.relations","-w",errorWeights, "-e","summary.error"])
	p1.wait()
	errorfile = open("summary.error", "r")
	content = errorfile.readlines()
	words = content[1].split(", ")
	std = float(words[1])
	var = math.pow(std,2)
	# now we can estimate the size of the 99% confidence sample
	z_a_2 = t.ppf(alpha,n_samples-1)#2.58
	delta = maxError
	n_samples = math.pow(z_a_2,2)*var/math.pow(delta,2)
	relationsfileRE=open(folder+"Relations/Original/"+output+"RE.relations","w")
	#relationsfileRE.seek(0)
	i=0
	while i < n_samples:
			firststamp=float(random.choice(ground.keys()))
			secondstamp=float(random.choice(ground.keys()))
			if firststamp > secondstamp:
				temp=firststamp
				firststamp=secondstamp
				secondstamp=temp
			firstpos=ground[firststamp]
			secondpos=ground[secondstamp]

			rel=getMatrixDiff(firstpos,secondpos)

			x = rel[0,3]
			y = rel[1,3]
			theta = math.atan2(rel[1,0],rel[0,0])

			relationsfileRE.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			i+=1 
	relationsfileRE.close()
	if not exists(join(folder,"Errors/Original/RE/")):
		makedirs(join(folder,"Errors/Original/RE/"))
	print folder+"Relations/Original/"+output+"RE.relations"
	p2=Popen([pathToMetricEvaluator, "-s",SLAMFile, "-r",folder+"Relations/Original/"+output+"RE.relations","-w","{1.0,1.0,1.0,0.0,0.0,0.0}", "-e",folder + "Errors/Original/RE/T.errors","-eu",folder + "Errors/Original/RE/T-unsorted.errors"])
	p2.wait()
	p3=Popen([pathToMetricEvaluator, "-s",SLAMFile, "-r",folder+"Relations/Original/"+output+"RE.relations","-w","{0.0,0.0,0.0,1.0,1.0,1.0}", "-e",folder + "Errors/Original/RE/R.errors","-eu",folder + "Errors/Original/RE/R-unsorted.errors"])
	p3.wait()


	#ORDERED
	if not(skipOrderedRecomputation):
		relationsfileOrdered=open(folder+"Relations/Original/"+output+"Ordered.relations","w")
		
		groundSorted=sorted(ground)
		idx = 1
		idx_delta = 10
		firststamp=groundSorted[idx]
		secondstamp=0
		#while secondstamp < groundSorted[-1]:
		while idx+idx_delta < len(groundSorted):
			secondstamp=groundSorted[idx+idx_delta]#round(firststamp+float(seconds),1)
			if firststamp in ground.keys():
				firstpos=ground[firststamp]
				if secondstamp in ground.keys():
					secondpos=ground[secondstamp]
					rel=getMatrixDiff(firstpos,secondpos)

					x = rel[0,3]
					y = rel[1,3]
					theta = math.atan2(rel[1,0],rel[0,0])

					relationsfileOrdered.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			firststamp=secondstamp
			idx += idx_delta

		relationsfileOrdered.close()

		if not exists(join(folder,"Errors/Original/Ordered/")):
			makedirs(join(folder,"Errors/Original/Ordered/"))
		p4=Popen([pathToMetricEvaluator, "-s",SLAMFile, "-r",folder+"Relations/Original/"+output+"Ordered.relations","-w","{1.0,1.0,1.0,0.0,0.0,0.0}", "-e",folder + "Errors/Original/Ordered/T.errors","-eu",folder + "Errors/Original/Ordered/T-unsorted.errors"])
		p4.wait()
		p5=Popen([pathToMetricEvaluator, "-s",SLAMFile, "-r",folder+"Relations/Original/"+output+"Ordered.relations","-w","{0.0,0.0,0.0,1.0,1.0,1.0}", "-e",folder + "Errors/Original/Ordered/R.errors","-eu",folder + "Errors/Original/Ordered/R-unsorted.errors"])
		p5.wait()

def getMatrixDiff(p1,p2):
	'''
	Computes the rototranslation difference of two points
	'''

	x1=p1[0]
	x2=p2[0]
	y1=p1[1]
	y2=p2[1]
	theta1=p1[2]
	theta2=p2[2]

	m_translation1=np.matrix(((1,0,0,x1),
		(0,1,0,y1),
		(0,0,1,0),
		(0,0,0,1)))	

	m_translation2=np.matrix(((1,0,0,x2),
		(0,1,0,y2),
		(0,0,1,0),
		(0,0,0,1)))		

	m_rotation1=np.matrix(((math.cos(theta1),-math.sin(theta1),0,0),
		(math.sin(theta1),math.cos(theta1),0,0),
		(0,0,1,0),
		(0,0,0,1)))

	m_rotation2=np.matrix(((math.cos(theta2),-math.sin(theta2),0,0),
		(math.sin(theta2),math.cos(theta2),0,0),
		(0,0,1,0),
		(0,0,0,1)))

	m1=m_translation1*m_rotation1
	m2=m_translation2*m_rotation2
	return m1.I*m2

def plotSlam(slam):
	file2=open(slam,'r')

	x=[]
	y=[]

	for line in file2:
		words = line.split(" ")
		x.append(words[5])
		y.append(words[6])

	file2.close()
	plt.plot(x,y,'r')

def plotGroundTruth(groundtruth):
	file=open(groundtruth,'r')

	xGT=[]
	yGT=[]

	for line in file:
		words = line.split(" ")
		xGT.append(words[1])
		yGT.append(words[2])

	file.close()
	plt.plot(xGT,yGT,'g')

def savePlot(slam,gt,save):
	plotSlam(slam)
	savefig(save+"_slam.png")
	plt.clf()
	plotGroundTruth(gt)
	savefig(save+"_gt.png")
	plotSlam(slam)
	savefig(save)

def savePlot2(slam,gt,save):
	'''
	Creates a figure with the trajectories slam and ground truth
	'''
	file2=open(slam,'r')

	x=[]
	y=[]

	for line in file2:
		words = line.split(" ")
		x.append(words[5])
		y.append(words[6])

	file2.close()
	file=open(gt,'r')

	xGT=[]
	yGT=[]

	for line in file:
		words = line.split(" ")
		xGT.append(words[1])
		yGT.append(words[2])

	file.close()

	fig,ax=plt.subplots()
	ax.cla()
	ax.plot(x,y,'r',xGT,yGT,'g')
	print 'SAVE'
	fig.savefig(save)
	plt.close(fig)

def generateAll(folder, skipGroundTruthConversion=False, skipOrderedRecomputation=False):
	'''
	Given a folder path if there is a .bag file and an Out.log file generates Relations, errors and trajectories
	'''
	if not(skipGroundTruthConversion):
		for f in listdir(folder):
			if isfile(join(folder, f)):
				if f[-4:] == ".bag":
					writeGroundTruth(join(folder, f),join(folder, f[:-4]))

	for f in listdir(folder):
		if isfile(join(folder, f)):
			if f[-7:] == "Out.log" and f[0:2]!="._": # to skip hidden macOS files
				generateRelationsOandRE(folder,f[:-7]+".log",skipOrderedRecomputation=skipOrderedRecomputation)
				savePlot2(join(folder, f),join(folder, f[:-7]+".log"),join(folder, "trajectories.png"))
	writeText(folder)



if __name__ == '__main__':
	#skipGroundTruthConversion = (sys.argv[2]=="True")
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,description='Given the directory of an individual output run, this tool generates all the support files that are necessary for the RPPF to actually train the models and perform predictions. More specifically:\n\n\t1. If the second (optional) parameter is set to True, it converts the .bag ground truth trajectory data into a .log ground truth trajectory data. Otherwise, the .log file is assumed to be already present and the conversion is skipped;\n\t2. It creates a Relations folder and generates both the ordered and randomly sampled relations files;\n\t3. It invokes the Freiburg Metric Evaluator tool on the generated relations, storing the corresponding error files in an Error folder;\n\t4. It plots a trajectories.png file overlaying the ground truth trajectory (in green) with the estimated SLAM trajectory (in red);\n\t5. It uses the last available map snapshot and the freshly computed mean translation error from the randomly sampled relations to generate an overlayed errorMap.png file.\n\nUnder normal conditions, there is no need to manually execute this component, as it is automatically invoked by launch.py at the end of each exploration run. However, it can also be executed manually, for instance to compute the relations associated with existing real world datasets (e.g. the RAWSEEDS Bicocca indoor datasets).')
	parser.add_argument('folder_of_individual_output_run',help='the folder that contains the output exploration data of an individual run')
	parser.add_argument('-s','--skip_ground_truth_conversion',action='store_true',help='skips the conversion of the ground truth data from the bag file to the log file and forces the re-usage of the existing ground truth log file; if the ground truth log file does not exist, the program will crash')
	args = parser.parse_args()
	generateAll(args.folder_of_individual_output_run,args.skip_ground_truth_conversion)
	#generateAll(sys.argv[1],skipGroundTruthConversion)
