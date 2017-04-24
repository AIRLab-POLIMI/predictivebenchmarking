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

def writeGroundTruth(data,outputFile):

	groundtruth=open(outputFile,"w")

	firstrun=True
	displacementx=0
	displacementy=0

	for topic,msg,t in rosbag.Bag(data).read_messages():
		if topic=="/base_pose_ground_truth":

			#senza traslare a (0,0) la ground truth
			'''
			position=msg.pose.pose.position
			quaternion=Quaternion()
			quaternion=(msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
			rot=tf.transformations.euler_from_quaternion(quaternion)

			if str(msg.header.stamp)[:-9]=="":
				groundtruth.write("0."+str(msg.header.stamp)[-9:]+" "+str(position.x)+" "+str(position.y)+" "+str(rot[2])+"\n")
			else:
				groundtruth.write(str(msg.header.stamp)[:-9]+"."+str(msg.header.stamp)[-9:]+" "+str(position.x)+" "+str(position.y)+" "+str(rot[2])+"\n")
			
			'''

			#trasla a (0,0) ground truth
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

	'''
	def writeOdom(data):
	odom=open(sys.argv[2][:-4]+"odom.log","w")

	for topic,msg,t in rosbag.Bag(sys.argv[1]).read_messages():
		if topic=="/odom":
			writeOdom(msg)


	odom.close()
	position=data.pose.pose.position
	quaternion=Quaternion()
	quaternion=(data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w)
	rot=tf.transformations.euler_from_quaternion(quaternion)
	if str(data.header.stamp)[:-9]=="":
		odom.write("0."+str(data.header.stamp)[-9:]+" "+str(position.x)+" "+str(position.y)+" "+str(rot[2])+"\n")
	else:
		odom.write(str(data.header.stamp)[:-9]+"."+str(data.header.stamp)[-9:]+" "+str(position.x)+" "+str(position.y)+" "+str(rot[2])+"\n")
	'''

def generateRelations(gtfile,seconds):
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
	relationsfile=open(gtfile[:-4]+".relations","w")

	if seconds=='0':
		#builds relations file taking random ground truth and computing the difference
		i=0
		while i<(len(ground.keys())/7):
			firststamp=float(random.choice(ground.keys()))
			secondstamp=float(random.choice(ground.keys()))
			if firststamp > secondstamp:
				temp=firststamp
				firststamp=secondstamp
				secondstamp=temp
			firstpos=ground[firststamp]
			secondpos=ground[secondstamp]
			relation=[float(secondpos[0])-float(firstpos[0]), float(secondpos[1])-float(firstpos[1]), float(secondpos[2])-float(firstpos[2])]
			relationsfile.write(str(firststamp)+" "+str(secondstamp)+" "+str(relation[0])+" "+str(relation[1])+" 0.000000 0.000000 0.000000 "+str(relation[2])+"\n")
			i+=1 

	elif seconds=='ordered':
		#builds relations file with ordered time
		groundSorted=sorted(ground)
		for time in groundSorted[::10]:
			firststamp=time
			secondstamp=time+8
			firstpos=ground[firststamp]
			if secondstamp in ground.keys():
				secondpos=ground[secondstamp]
				relation=[float(secondpos[0])-float(firstpos[0]), float(secondpos[1])-float(firstpos[1]), float(secondpos[2])-float(firstpos[2])]
				relationsfile.write(str(firststamp)+" "+str(secondstamp)+" "+str(relation[0])+" "+str(relation[1])+" 0.000000 0.000000 0.000000 "+str(relation[2])+"\n")

	elif seconds=='ordered-2':
		#builds relations file with ordered time
		groundSorted=sorted(ground)
		firststamp=groundSorted[1]
		secondstamp=0
		while secondstamp < groundSorted[-1]:
			secondstamp=firststamp+2
			firstpos=ground[firststamp]
			if secondstamp in ground.keys():
				secondpos=ground[secondstamp]
				relation=[float(secondpos[0])-float(firstpos[0]), float(secondpos[1])-float(firstpos[1]), float(secondpos[2])-float(firstpos[2])]
				relationsfile.write(str(firststamp)+" "+str(secondstamp)+" "+str(relation[0])[:9]+" "+str(relation[1])[:9]+" 0.000000 0.000000 0.000000 "+str(relation[2])[:9]+"\n")
			firststamp=secondstamp


	elif seconds=='MCO':
		#builds relations file with ordered time
		groundSorted=sorted(ground)
		for time in groundSorted[::10]:
			firststamp=time
			secondstamp=time+8
			firstpos=ground[firststamp]
			xi=firstpos


			#inverse relationship
			xi=[1,2,3]
			xi[0]=-firstpos[0]*math.cos(firstpos[2])-firstpos[1]*math.sin(firstpos[2])
			xi[1]=firstpos[0]*math.sin(firstpos[2])-firstpos[1]*math.cos(firstpos[2])
			xi[2]=-firstpos[2]

			if secondstamp in ground.keys():
				xj=ground[secondstamp]	

				#compose the relation xj-xi
				relation=[0,0,0]
				relation[0]=xj[0]+xi[0]*math.cos(xj[2])-xi[1]*math.sin(xj[2])
				relation[1]=xj[1]+xi[0]*math.sin(xj[2])+xi[1]*math.cos(xj[2])
				relation[2]=xj[2]+xi[2]

				relationsfile.write(str(firststamp)+" "+str(secondstamp)+" "+str(relation[0])+" "+str(relation[1])+" 0.000000 0.000000 0.000000 "+str(relation[2])+"\n")

	else:
		#builds relations file with max 2 time difference between poses
		i=0
		while i<(len(ground.keys())/7):
			firststamp=float(random.choice(ground.keys()))
			secondstamp=0
			while secondstamp not in ground.keys():
				secondstamp=float(firststamp)+random.randint(1,float(seconds)*10)*0.1 
			firstpos=ground[firststamp]
			secondpos=ground[secondstamp]
			relation=[float(secondpos[0])-float(firstpos[0]), float(secondpos[1])-float(firstpos[1]), float(secondpos[2])-float(firstpos[2])]
			relationsfile.write(str(firststamp)+" "+str(secondstamp)+" "+str(relation[0])+" "+str(relation[1])+" 0.000000 0.000000 0.000000 "+str(relation[2])+"\n")
			i+=1 
		relationsfile.close()

def generateRelationsMatrices(gtfile,seconds):
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
	relationsfile=open(gtfile[:-4]+".relations","w")

	#builds relations file taking random ground truth and computing the difference
	i=0
	while i < ( len(ground.keys()) / 7 ):
		if seconds=='0':
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

			relationsfile.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			i+=1 

		elif seconds=='ordered':
			#builds relations file with ordered time
			groundSorted=sorted(ground)
			for time in groundSorted[::10]:
				firststamp=time
				secondstamp=time+8
				firstpos=ground[firststamp]
				if secondstamp in ground.keys():
					secondpos=ground[secondstamp]
					rel=getMatrixDiff(firstpos,secondpos)

					x = rel[0,3]
					y = rel[1,3]
					theta = math.atan2(rel[1,0],rel[0,0])

					relationsfile.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
					i+=1 
	relationsfile.close()

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

	#takes bag file and output file as input 
	#writeGroundTruth(sys.argv[1],sys.argv[2])

	#takes output file created by the previous function and the range of seconds to generate the relations
	#generateRelations(sys.argv[2],sys.argv[3])

	generateRelationsMatrices(sys.argv[1],sys.argv[2])