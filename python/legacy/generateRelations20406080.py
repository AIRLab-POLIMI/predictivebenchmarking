import sys
import random
import rosbag
from geometry_msgs.msg import Vector3, Quaternion
from nav_msgs.msg import Odometry
import rospy
import roslib
import tf
import math
import numpy as np
from subprocess import call
from scipy.stats import t

def generateRelationsMatrices(gtfile,output,SLAMFile=None,folder=None):

	gt=open(gtfile,"r")
	npose=0
	ground={}	
	ground20={}
	ground40={}
	ground60={}
	ground80={}

	#builds dictionary with all the ground truth
	for line in gt:
		words = line.split(" ")

		euler=[float(words[1]),float(words[2]),float(words[3])]

		if words[0] not in ground:
			ground[float(words[0])]=euler 
		else:
			ground.update({ float(words[0]): euler })

		npose+=1

	gt.seek(0)

	count=0
	for line in gt:
		count+=1
		words = line.split(" ")

		euler=[float(words[1]),float(words[2]),float(words[3])]

		if count < npose*0.2:
			if words[0] not in ground20:
				ground20[float(words[0])]=euler 
			else:
				ground20.update({ float(words[0]): euler })

		if count < npose*0.4:
			if words[0] not in ground40:
				ground40[float(words[0])]=euler 
			else:
				ground40.update({ float(words[0]): euler })

		if count < npose*0.6:
			if words[0] not in ground60:
				ground60[float(words[0])]=euler 
			else:
				ground60.update({ float(words[0]): euler })

		if count < npose*0.8:
			if words[0] not in ground80:
				ground80[float(words[0])]=euler 
			else:
				ground80.update({ float(words[0]): euler })

	gt.close()

	relationsRandomFile=open(output+"Random.relations","w")

	i=0
	while i < len(ground.keys())/2:
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

			relationsRandomFile.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			i+=1 

	call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random.relations","-w","{1.0,1.0,1.0,0.0,0.0,0.0}", "-e",folder+"T.error"])
	call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random.relations","-w","{0.0,0.0,0.0,1.0,1.0,1.0}", "-e",folder+"R.error"])

	relationsRandomFile.close()

	relationsRandomFile20=open(output+"Random20.relations","w")

	i=0
	while i < len(ground20.keys())/2:
			firststamp=float(random.choice(ground20.keys()))
			secondstamp=float(random.choice(ground20.keys()))
			if firststamp > secondstamp:
				temp=firststamp
				firststamp=secondstamp
				secondstamp=temp
			firstpos=ground20[firststamp]
			secondpos=ground20[secondstamp]

			rel=getMatrixDiff(firstpos,secondpos)

			x = rel[0,3]
			y = rel[1,3]
			theta = math.atan2(rel[1,0],rel[0,0])

			relationsRandomFile20.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			i+=1 

	call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random20.relations","-w","{1.0,1.0,1.0,0.0,0.0,0.0}", "-e",folder+"20T.error"])
	call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random20.relations","-w","{0.0,0.0,0.0,1.0,1.0,1.0}", "-e",folder+"20R.error"])

	relationsRandomFile20.close()

	relationsRandomFile40=open(output+"Random40.relations","w")

	i=0
	while i < len(ground40.keys())/2:
			firststamp=float(random.choice(ground40.keys()))
			secondstamp=float(random.choice(ground40.keys()))
			if firststamp > secondstamp:
				temp=firststamp
				firststamp=secondstamp
				secondstamp=temp
			firstpos=ground40[firststamp]
			secondpos=ground40[secondstamp]

			rel=getMatrixDiff(firstpos,secondpos)

			x = rel[0,3]
			y = rel[1,3]
			theta = math.atan2(rel[1,0],rel[0,0])

			relationsRandomFile40.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			i+=1 

	call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random40.relations","-w","{1.0,1.0,1.0,0.0,0.0,0.0}", "-e",folder+"40T.error"])
	call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random40.relations","-w","{0.0,0.0,0.0,1.0,1.0,1.0}", "-e",folder+"40R.error"])

	relationsRandomFile40.close()

	relationsRandomFile60=open(output+"Random60.relations","w")

	i=0
	while i < len(ground60.keys())/2:
			firststamp=float(random.choice(ground60.keys()))
			secondstamp=float(random.choice(ground60.keys()))
			if firststamp > secondstamp:
				temp=firststamp
				firststamp=secondstamp
				secondstamp=temp
			firstpos=ground60[firststamp]
			secondpos=ground60[secondstamp]

			rel=getMatrixDiff(firstpos,secondpos)

			x = rel[0,3]
			y = rel[1,3]
			theta = math.atan2(rel[1,0],rel[0,0])

			relationsRandomFile60.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			i+=1 

	call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random60.relations","-w","{1.0,1.0,1.0,0.0,0.0,0.0}", "-e",folder+"60T.error"])
	call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random60.relations","-w","{0.0,0.0,0.0,1.0,1.0,1.0}", "-e",folder+"60R.error"])

	relationsRandomFile60.close()

	relationsRandomFile80=open(output+"Random80.relations","w")

	i=0
	while i < len(ground80.keys())/2:
			firststamp=float(random.choice(ground80.keys()))
			secondstamp=float(random.choice(ground80.keys()))
			if firststamp > secondstamp:
				temp=firststamp
				firststamp=secondstamp
				secondstamp=temp
			firstpos=ground80[firststamp]
			secondpos=ground80[secondstamp]

			rel=getMatrixDiff(firstpos,secondpos)

			x = rel[0,3]
			y = rel[1,3]
			theta = math.atan2(rel[1,0],rel[0,0])

			relationsRandomFile80.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			i+=1 

	call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random80.relations","-w","{1.0,1.0,1.0,0.0,0.0,0.0}", "-e",folder+"80T.error"])
	call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random80.relations","-w","{0.0,0.0,0.0,1.0,1.0,1.0}", "-e",folder+"80R.error"])

	relationsRandomFile80.close()

def getMatrixDiff(p1,p2):

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

if __name__ == '__main__':

	generateRelationsMatrices(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
