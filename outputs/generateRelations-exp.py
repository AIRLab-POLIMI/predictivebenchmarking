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

def generateRelationsMatrices(gtfile,output,typeOfRelations,seconds=1):

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
	relationsfile=open(output+".relations","w")

	#builds relations file taking random ground truth and computing the difference
	if typeOfRelations=='R':
		i=0
		while i < ( len(ground.keys()) / 7 ):
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

	elif typeOfRelations=='OandR':
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

		call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random.relations","-w","{1.0,1.0,1.0,0.0,0.0,0.0}", "-e",folder+"TerrorRandom.error","-eu",folder+"TerrorRandom-unsorted.error"])
		call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Random.relations","-w","{0.0,0.0,0.0,1.0,1.0,1.0}", "-e",folder+"RerrorRandom.error","-eu",folder+"RerrorRandom-unsorted.error"])


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

		call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Ordered.relations","-w","{1.0,1.0,1.0,0.0,0.0,0.0}", "-e",folder+"TerrorOrdered.error","-eu",folder+"TerrorOrdered-unsorted.error"])
		call(["../metricEvaluator/metricEvaluator", "-s",SLAMFile, "-r",output+"Ordered.relations","-w","{0.0,0.0,0.0,1.0,1.0,1.0}", "-e",folder+"RerrorOrdered.error","-eu",folder+"RerrorOrdered-unsorted.error"])


		relationsOrderedFile.close()
		relationsRandomFile.close()

	elif typeOfRelations=='O':
		#builds relations file with ordered time
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

				relationsfile.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			firststamp=secondstamp

	elif typeOfRelations=='O+R':
		#builds relations file with ordered time
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

				relationsfile.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			firststamp=secondstamp 

		i=0
		while i < ( len(ground.keys()) / 10 ):
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

	elif typeOfRelations=='AllLoops':
		#builds relations file with ordered time
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

				relationsfile.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			firststamp=secondstamp 

		#finds all the loops in the log file
		'''
		firststamp=groundSorted[1]
		for i in range(1,len(groundSorted)):
			for j in range(i,len(groundSorted),10):
				stamp1=groundSorted[i]
				stamp2=groundSorted[j]

				x1 = ground[stamp1][0]
				y1 = ground[stamp1][1]
				x2 = ground[stamp2][0]
				y2 = ground[stamp2][1]

				xdelta=math.fabs(x1-x2)
				ydelta=math.fabs(y1-y2)
				if xdelta > 0.5 or ydelta > 0.5 and not moved:
					moved=True

				#loop closing condition
				if xdelta < 0.3 and ydelta < 0.3 and stamp2 -  stamp1 > 20 and moved:
					moved=False
					rel=getMatrixDiff(ground[stamp1],ground[stamp2])

					x = rel[0,3]
					y = rel[1,3]
					theta = math.atan2(rel[1,0],rel[0,0])

					relationsfile.write(str(stamp1)+" "+str(stamp2)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")'''
		firststamp=groundSorted[1]
		#print len(groundSorted)
		found = False
		i = 1
		while i < len(groundSorted):
		#for i in range(1,len(groundSorted)):
			#print i
			for j in range(i,len(groundSorted)):
				# check if their time difference is over a min
				# threshold to avoid recognizing false movements
				stamp1=groundSorted[i]
				stamp2=groundSorted[j]
				if stamp2-stamp1 > 5:
					# if so we should have actually moved, so 
					# let's see how far apart the two points are
					x1 = ground[stamp1][0]
					y1 = ground[stamp1][1]
					x2 = ground[stamp2][0]
					y2 = ground[stamp2][1]

					xdelta=math.fabs(x1-x2)
					ydelta=math.fabs(y1-y2)	 
					if xdelta <= 0.3 and ydelta <= 0.5: 	
						# looks like it's a good candidate for loop closing,
						# but have we actually moved or have we just stayed here?
						#print "Candidate loop found"
						distance = 0
						for k in range(i,j): # p stands for progressive
							sp1 = groundSorted[k]
							sp2 = groundSorted[k+1]
							xp1	= ground[sp1][0]
							yp1 = ground[sp1][1]
							xp2 = ground[sp2][0]
							yp2 = ground[sp2][1]
							
							dx = math.fabs(xp1-xp2)
							dy = math.fabs(yp1-yp2)
							# Euclidean distance
							distance += math.sqrt(math.pow(dx,2)+math.pow(dy,2))	
						# let's check how far we've come against a predefined threshold
						#print distance
						if distance > 5: # then we have actually found a loop, add the relation
							rel=getMatrixDiff(ground[stamp1],ground[stamp2])

							x = rel[0,3]
							y = rel[1,3]
							theta = math.atan2(rel[1,0],rel[0,0])

							relationsfile.write(str(stamp1)+" "+str(stamp2)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
							# note that at this point, the next timestamp will also be considered 
							# as a loop: to avoid this, we need to introduce a form of delay operator
							# cheap approach (to be improved): skip j forward of a few positions
							j += 50
							found = True
							#print "Found"
			if found: # let's skip over the immediately following timestamps
				i += 50
				found = False
			else:
				i += 1	
	elif typeOfRelations=='Smart':
		groundSorted=sorted(ground)
		loops={}

		#ordered relations
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

				relationsfile.write(str(firststamp)+" "+str(secondstamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
			firststamp=secondstamp

		firststamp=groundSorted[1]
		print "Sorted completed"
		print len(groundSorted)
		found = False
		i = 1
		print "Beginning loop detection"
		while i < 0:#len(groundSorted):
		#for i in range(1,len(groundSorted)):
			print i
			for j in range(i,len(groundSorted)):
				# check if their time difference is over a min
				# threshold to avoid recognizing false movements
				stamp1=groundSorted[i]
				stamp2=groundSorted[j]
				if stamp2-stamp1 > 5:
					# if so we should have actually moved, so 
					# let's see how far apart the two points are
					x1 = ground[stamp1][0]
					y1 = ground[stamp1][1]
					x2 = ground[stamp2][0]
					y2 = ground[stamp2][1]

					xdelta=math.fabs(x1-x2)
					ydelta=math.fabs(y1-y2)	 
					if xdelta <= 0.3 and ydelta <= 0.5: 	
						# looks like it's a good candidate for loop closing,
						# but have we actually moved or have we just stayed here?
						#print "Candidate loop found"
						distance = 0
						for k in range(i,j): # p stands for progressive
							sp1 = groundSorted[k]
							sp2 = groundSorted[k+1]
							xp1	= ground[sp1][0]
							yp1 = ground[sp1][1]
							xp2 = ground[sp2][0]
							yp2 = ground[sp2][1]
							
							dx = math.fabs(xp1-xp2)
							dy = math.fabs(yp1-yp2)
							# Euclidean distance
							distance += math.sqrt(math.pow(dx,2)+math.pow(dy,2))	
						# let's check how far we've come against a predefined threshold
						#print distance
						if distance > 5: # then we have actually found a loop, add the relation
							rel=getMatrixDiff(ground[stamp1],ground[stamp2])

							x = rel[0,3]
							y = rel[1,3]
							theta = math.atan2(rel[1,0],rel[0,0])

							relationsfile.write(str(stamp1)+" "+str(stamp2)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
							# note that at this point, the next timestamp will also be considered 
							# as a loop: to avoid this, we need to introduce a form of delay operator
							# cheap approach (to be improved): skip j forward of a few positions
							j += 50
							found = True
							#print "Found"
			if found: # let's skip over the immediately following timestamps
				i += 50
				found = False
			else:
				i += 1	

		#find and writes relations every 10 meters
		'''
		firststamp=groundSorted[1]
		for stamp in groundSorted:
			dist = math.sqrt(math.pow((ground[firststamp][0] - ground[stamp][0]),2) + math.pow((ground[firststamp][1] - ground[stamp][1]),2))
			if dist > 10:
				rel=getMatrixDiff(ground[firststamp],ground[stamp])

				x = rel[0,3]
				y = rel[1,3]
				theta = math.atan2(rel[1,0],rel[0,0])
				relationsfile.write(str(firststamp)+" "+str(stamp)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")
				firststamp=stamp'''
		print "Beginning distance check"
		firststamp=groundSorted[1]
		for i in range(1,len(groundSorted),5):
			print i
			for j in range(i,len(groundSorted),5):
				stamp1=groundSorted[i]
				stamp2=groundSorted[j]

				x1 = ground[stamp1][0]
				y1 = ground[stamp1][1]
				x2 = ground[stamp2][0]
				y2 = ground[stamp2][1]

				dx=math.fabs(x1-x2)
				dy=math.fabs(y1-y2)
				distance = math.sqrt(math.pow(dx,2)+math.pow(dy,2))
				if distance > 0:
					rel=getMatrixDiff(ground[stamp1],ground[stamp2])

					x = rel[0,3]
					y = rel[1,3]
					theta = math.atan2(rel[1,0],rel[0,0])

					relationsfile.write(str(stamp1)+" "+str(stamp2)+" "+str(x)+" "+str(y)+" 0.000000 0.000000 0.000000 "+str(theta)+"\n")



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

	generateRelationsMatrices(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
