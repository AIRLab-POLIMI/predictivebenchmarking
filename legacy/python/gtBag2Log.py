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


if __name__ == '__main__':

	#takes bag file and output file as input 
	writeGroundTruth(sys.argv[1],sys.argv[2])
