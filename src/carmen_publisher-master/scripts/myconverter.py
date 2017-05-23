#!/usr/bin/env python
import rospy,rosbag
import roslib
import tf
import numpy as np
import sys, getopt
import os.path
from geometry_msgs.msg import Vector3, Quaternion, TransformStamped, Transform, Point
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from tf2_msgs.msg import TFMessage
from tf.msg import tfMessage
from std_msgs.msg import Header

from math import radians, floor

def fillUpLaserMessage(tfmsg,words,seq):

	robot=True
	laser_msg=LaserScan()

	laser_msg.header.frame_id = "base_link"
	
	laser_msg.angle_increment = float(words[4])
	laser_msg.angle_min = float(words[2]) + float(laser_msg.angle_increment/2)
	laser_msg.angle_max = float(words[2]) + float(words[3]) - float(laser_msg.angle_increment/2)

	laser_msg.range_min = 0.
	laser_msg.range_max = float(words[5])

	ranges = []
	num_range_readings = int(words[8])
	last_range_reading = num_range_readings + 8

	for word in words[9:last_range_reading+1]:
		ranges.append( float( word ))

	laser_msg.ranges = ranges

	# min-max angle fitting, Karto need
	'''factor_angle_fitting = laser_msg.angle_increment / float(2)
	while (round((laser_msg.angle_max - laser_msg.angle_min)/laser_msg.angle_increment) + 1) != num_range_readings:

		if (round((laser_msg.angle_max - laser_msg.angle_min)/laser_msg.angle_increment) + 1) > num_range_readings:
			laser_msg.angle_min = laser_msg.angle_min + factor_angle_fitting
		else:
			laser_msg.angle_max = laser_msg.angle_max - factor_angle_fitting

		factor_angle_fitting = factor_angle_fitting / float(2)'''

	laser_msg.header.stamp = rospy.Time( float(words[last_range_reading+13]) ) 

	odommsg=TransformStamped()
	posemsg=Odometry()

	if robot:
		position = Vector3(float(words[last_range_reading+5]), float(words[last_range_reading+6]), 0.0)
		poseposition = Point(float(words[last_range_reading+5]), float(words[last_range_reading+6]), 0.0)
		quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0, float(words[last_range_reading+7]))
	else: 
		position = Vector3(float(words[last_range_reading+2]), float(words[last_range_reading+3]), 0.0)
		poseposition = Point(float(words[last_range_reading+2]), float(words[last_range_reading+3]), 0.0)
		quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0, float(words[last_range_reading+4]))

	headerOdom=Header()
	headerOdom.seq=seq
	headerOdom.frame_id="odom"
	headerOdom.stamp=rospy.Time( float(words[last_range_reading+13]) )
	odommsg.header=headerOdom

	odommsg.child_frame_id = "base_link"
	odommsg.transform.translation = position
	odommsg.transform.rotation.x  = quaternion[0]
	odommsg.transform.rotation.y  = quaternion[1]
	odommsg.transform.rotation.z  = quaternion[2]
	odommsg.transform.rotation.w  = quaternion[3]

	tfmsg.transforms.append(odommsg)

	posemsg.header=headerOdom
	
	posemsg.pose.pose.position = poseposition
	posemsg.pose.pose.orientation.x = quaternion[0]
	posemsg.pose.pose.orientation.y = quaternion[1]
	posemsg.pose.pose.orientation.z = quaternion[2]
	posemsg.pose.pose.orientation.w = quaternion[3]
	
	posemsg.child_frame_id  = "base_link"
	
	return (tfmsg,posemsg,laser_msg)

def fillUpOldLaserMessage(words):
	
	laser_msg=LaserScan()

	laser_msg.header.frame_id = "base_link"		
	ranges = []
	num_range_readings = int(words[1])
	last_range_reading = num_range_readings + 1
	for word in words[2:last_range_reading+1]:					
		ranges.append( float( word ) )

	ang_range = float( 180 )

	# Get angular resolution
	ang_res = (radians(ang_range) / (num_range_readings - 0.0))
		
	# Get max reading
	max_reading = 20.

	# init laser msg
	ang_min = radians( - ang_range / 2. )
	ang_max = radians( + ang_range / 2. ) - ang_res

	laser_msg.angle_min 	   = ang_min
	laser_msg.angle_max 	   = ang_max
	laser_msg.angle_increment = ang_res

	laser_msg.range_min = 0
	laser_msg.range_max = max_reading
		
	laser_msg.ranges = ranges		
	laser_msg.header.stamp = rospy.Time( float(words[last_range_reading+7]) )

	return laser_msg

def fillUpOdomMessage(tfmsg,words,seq):

	headerOdom=Header()
	headerOdom.seq=seq
	headerOdom.frame_id="odom"
	headerOdom.stamp=rospy.Time( float(words[7]) )

	if float(words[7]) < 0:
		return

	position = Vector3(float(words[1])-10, float(words[2])-50, 0.0)
	poseposition = Point(float(words[1])-10, float(words[2])-50, 0.0)
			
	quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0, float(words[3]))

	odommsg=TransformStamped()
	posemsg=Odometry()

	odommsg.header=headerOdom
	posemsg.header=headerOdom

	odommsg.child_frame_id="base_link"
	posemsg.child_frame_id="base_link"

	posemsg.pose.pose.position = poseposition
	posemsg.pose.pose.orientation.x = quaternion[0]
	posemsg.pose.pose.orientation.y = quaternion[1]
	posemsg.pose.pose.orientation.z = quaternion[2]
	posemsg.pose.pose.orientation.w = quaternion[3]

	odommsg.transform.translation = position
	odommsg.transform.rotation.x = quaternion[0]
	odommsg.transform.rotation.y = quaternion[1]
	odommsg.transform.rotation.z = quaternion[2]
	odommsg.transform.rotation.w = quaternion[3]

	tfmsg.transforms.append(odommsg)
	
	return (tfmsg,posemsg)

def fillUpOdomFromFlaser(tfmsg,words,seq):

	num_range_readings = int(words[1])
	last_range_reading = num_range_readings + 1

	headerOdom=Header()
	headerOdom.seq=seq
	headerOdom.frame_id="odom"
	headerOdom.stamp=rospy.Time( float(words[last_range_reading+7]) )

	position = Vector3(float(words[last_range_reading+4])-576.536523, float(words[last_range_reading+5]), 0.0)
	poseposition = Point(float(words[last_range_reading+4])-576.536523, float(words[last_range_reading+5]), 0.0)
			
	quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0, float(words[last_range_reading+6]))

	odommsg=TransformStamped()
	posemsg=Odometry()

	odommsg.header=headerOdom
	posemsg.header=headerOdom

	odommsg.child_frame_id="base_link"
	posemsg.child_frame_id="base_link"

	posemsg.pose.pose.position = poseposition
	posemsg.pose.pose.orientation.x = quaternion[0]
	posemsg.pose.pose.orientation.y = quaternion[1]
	posemsg.pose.pose.orientation.z = quaternion[2]
	posemsg.pose.pose.orientation.w = quaternion[3]

	odommsg.transform.translation = position
	odommsg.transform.rotation.x = quaternion[0]
	odommsg.transform.rotation.y = quaternion[1]
	odommsg.transform.rotation.z = quaternion[2]
	odommsg.transform.rotation.w = quaternion[3]

	tfmsg.transforms.append(odommsg)
	
	return (tfmsg,posemsg)

def convert(inputfile,outputfile):

	tfmsg=tfMessage()
	seq=0
	csail=False

	#open input
	try:
		inCompleteName = os.path.expanduser(inputfile)
		carmenlog = open(inCompleteName, "r")
	except (IOError, ValueError):
		rospy.logerr("Couldn't open %", inputfile)
		exit(-1)

	#create output
	try:
		outCompleteName = os.path.expanduser(outputfile)
		bag = rosbag.Bag(outCompleteName, "w")
	except (IOError, ValueError):
		rospy.logerr("Couldn't open %", outputfile)
		exit(-1)

	#read all input lines
	for line in carmenlog:

		words = line.split(" ")

		if words[0]=="ODOM":
			values=fillUpOdomMessage(tfmsg,words,seq)
			tfmsg=values[0]
			pose=values[1]
			bag.write("/base_odometry/odom",pose , pose.header.stamp)
			bag.write("/tf", tfmsg , pose.header.stamp)
			seq+=1

		if words[0]=="FLASER" and not csail:
			laser_msg=fillUpOldLaserMessage(words)
			laser_msg.header.seq = laser_msg.header.seq + 1
			bag.write("/base_scan",laser_msg, laser_msg.header.stamp)

		if words[0]=="ROBOTLASER1":
			values=fillUpLaserMessage(tfmsg,words,seq)
			laser_msg=values[2]
			laser_msg.header.seq = laser_msg.header.seq + 1
			pose=values[1]
			tfmsg=values[0]
			#bag.write("/base_odometry/odom", pose , pose.header.stamp)
			#bag.write("/tf", tfmsg , pose.header.stamp)
			bag.write("/base_scan", laser_msg , laser_msg.header.stamp)
			seq+=1
			
		if words[0]=="FLASER" and csail:
			laser_msg=fillUpOldLaserMessage(words)
			laser_msg.header.seq = laser_msg.header.seq + 1
			bag.write("/base_scan",laser_msg, laser_msg.header.stamp)
			values=fillUpOdomFromFlaser(tfmsg,words,seq)
			tfmsg=values[0]
			pose=values[1]
			bag.write("/base_odometry/odom",pose , pose.header.stamp)
			bag.write("/tf", tfmsg , pose.header.stamp)
			seq+=1

		tfmsg=tfMessage()
	
	bag.close()


if __name__ == '__main__':
	
	rospy.init_node('myconverter', anonymous=True)
	
	if len(sys.argv) < 3:
		sys.exit()

	try:
		opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		sys.exit()
		
	for opt, arg in opts:
		if opt in ('-h', "--help"):
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	convert(inputfile, outputfile)
	
	rospy.loginfo("Job's done.")