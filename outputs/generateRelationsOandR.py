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

def generateRelationsMatrices(gtfile,output,seconds=1,SLAMFile=None,folder=None):

	if seconds=='0':
		print 'Error: Seconds 0'
		return

	gt=open(gtfile,"r")
	ground={}	

	#builds dictionary with all the ground truth
	for line in gt:
		words = line.split(" ")

		euler=[float(words[1]),float(words[2]),float(words[3])]

		if words[0] not in ground:
			ground[float(words[0])]=euler 
		else:
			ground.update({ float(words[0]): euler })

	gt.close()
	relationsRandomFile=open(output+"Random.relations","w")
	relationsOrderedFile=open(output+"Ordered.relations","w")

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

	groundSorted=sorted(ground)
	firststamp=groundSorted[1]
	secondstamp=0
	while secondstamp < groundSorted[-1]:
		secondstamp=round(firststamp+float(seconds),1)
		firstpos=ground[firststamp]
		if secondstamp in ground.keys():
			secondpos=ground[secondstamp]
			rel=getMatrixDiff(firstpos,secondpos)

			x = rel[0,3]
			y = rel[1,3]
			theta = math.atan2(rel[1,0],rel[0,0])

			relationsOrderedFile.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
		firststamp=secondstamp

	relationsOrderedFile.close()
	relationsRandomFile.close()

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

	generateRelationsMatrices(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
