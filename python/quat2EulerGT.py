''' This little helper tool converts ground truth carmen log files that rely on quaternions for angular
positioning, like those of the vision tud munich dataset, into log files that use euler theta rotation.'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Software License Agreement (BSD License)
#
# Copyright (c) 2016, Martin Guenther
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

'''This is a converter for the Intel Research Lab SLAM dataset
   ( http://kaspar.informatik.uni-freiburg.de/~slamEvaluation/datasets/intel.clf )
   to rosbag'''

import rospy
import rosbag
import sys,argparse
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from math import pi
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import TransformStamped, Quaternion
import tf
from os.path import join
from collections import OrderedDict
import numpy as np
import math

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

def applyMatrixDiff(p1,diff):
	'''
	Computes the rototranslation difference of two points
	'''

	x1=p1[0]
	y1=p1[1]
	theta1=p1[2]

	m_translation1=np.matrix(((1,0,0,x1),
		(0,1,0,y1),
		(0,0,1,0),
		(0,0,0,1)))		

	m_rotation1=np.matrix(((math.cos(theta1),-math.sin(theta1),0,0),
		(math.sin(theta1),math.cos(theta1),0,0),
		(0,0,1,0),
		(0,0,0,1)))

	m1=m_translation1*m_rotation1
	return m1*diff

def rotatePoint(p,theta):
	R = np.matrix(((math.cos(theta),-math.sin(theta)),(math.sin(theta),math.cos(theta))))
	return p * R

def getAngle(slamLines,gtLines,diff):
	p1s = slamLines[1]
	tokens = p1s.split(' ')
	p1 = (float(tokens[5]),float(tokens[6]))
	print p1
	p2s = slamLines[2067]#2718
	tokens = p2s.split(' ')
	p2 = (float(tokens[5]),float(tokens[6]))
	print p2
	p1g = gtLines[3]
	tokens = p1g.split(' ')
	p3 = (float(tokens[1]),float(tokens[2]),0)
	p3 = applyMatrixDiff(p3,diff)
	p3 = [p3[0,3],p3[1,3]]
	print p3
	p2g = gtLines[5342]#8861
	tokens = p2g.split(' ')
	p4 = (float(tokens[1]),float(tokens[2]),0)
	p4 = applyMatrixDiff(p4,diff)
	p4 = [p4[0,3],p4[1,3]]
	print p4
	ref_angle_slam = math.atan2(p2[0]-p1[0], p2[1]-p1[1])
	print ref_angle_slam
	# Correct for negative angles
	if ref_angle_slam < 0:
		ref_angle_slam += 2*np.pi
	ref_angle_gt = math.atan2(p4[0]-p3[0],p4[1]-p3[1])
	print ref_angle_gt
	if ref_angle_gt < 0:
		ref_angle_gt += 2*np.pi
	angle_diff = (np.pi - math.fabs(math.fabs(ref_angle_slam - ref_angle_gt) - np.pi))
	print -angle_diff
	return -angle_diff


def convertGT(quatGTPath, slamPath):
	quatGTPath = sys.argv[1]
	slamPath = sys.argv[2]
	dataset_name = quatGTPath.split('/')[-1]
	output_folder = '/'.join(quatGTPath.split('/')[:-1])
	savename = join(output_folder,dataset_name.split('.')[0])+'.log'
	print savename
	# now we open the file 
	quatGT = open(quatGTPath, 'r')
	eulGT = open(savename, 'w')
	slamFile = open(slamPath,'r')
	# retrieve first movement
	lines = slamFile.readlines()
	slam_lines = lines
	firstMovement = lines[1]
	tokens = firstMovement.split(' ')
	p2_x = float(tokens[5])
	p2_y = float(tokens[6])
	p2_theta = 0
	p2_yaw = float(tokens[7])
	p2 = [p2_x,p2_y,p2_theta]
	# also from quatGT
	lines = quatGT.readlines()
	lines_to_skip = 3
	firstMovement = lines[lines_to_skip]
	tokens = firstMovement.split(' ')
	p1_x = float(tokens[1])
	p1_y = float(tokens[2])
	p1_quat = (float(tokens[4]),float(tokens[5]),float(tokens[6]),float(tokens[7]))
	rot = tf.transformations.euler_from_quaternion(p1_quat)
	print p2_yaw
	print rot[2]
	p2_quat = tf.transformations.quaternion_from_euler(0,0,p2_yaw)
	rot = tf.transformations.euler_from_quaternion(p2_quat)
	print rot[2]
	quat_diff = tf.transformations.quaternion_multiply(tf.transformations.quaternion_inverse(p1_quat),p2_quat)
	p2_quat = tf.transformations.quaternion_multiply(p1_quat,quat_diff)
	rot = tf.transformations.euler_from_quaternion(p2_quat)
	print rot[2]
	p1_theta = 0#rot[2]
	p1 = [p1_x,p1_y,p1_theta]
	diff = getMatrixDiff(p1,p2)
	# about quaternions: we need to compute the difference
	counter = 0
	# angle = 5.3*np.pi/4 # for 360 dataset
	# angle = 5.01*np.pi/4 # for slam,slam2 dataset
	# angle = -2.16 # for slam 3 dataset
	# let's determine automatically the angle
	angle = 5.01*np.pi/4#getAngle(slam_lines,lines,diff)
	for line in lines[lines_to_skip:]:
		line = line.strip()
		tokens = line.split(' ')
		quaternion = Quaternion()
		quaternion = (float(tokens[4]),float(tokens[5]),float(tokens[6]),float(tokens[7]))
		quaternion = tf.transformations.quaternion_multiply(quaternion,quat_diff)
		rot = tf.transformations.euler_from_quaternion(quaternion)
		# build the point
		p1 = [float(tokens[1]),float(tokens[2]),0]
		p2 = applyMatrixDiff(p1,diff)
		x = p2[0,3]
		y = p2[1,3]
		xy = [x,y]
		xy = rotatePoint(xy,angle)
		theta = math.atan2(p2[1,0],p2[0,0])
		p1 = [xy[0,0],xy[0,1],0]
		if counter == 0:
			p2 = [p2_x,p2_y,0]
			diff_2 = getMatrixDiff(p1,p2)
		p2 = applyMatrixDiff(p1,diff_2)
		x = p2[0,3]
		y = p2[1,3]
		tokens = [tokens[0],str(x),str(y),str(rot[2])] 
		line = ' '.join(tokens)
		eulGT.write("%s\n" % line)
		counter += 1
	quatGT.close()
	eulGT.close()

if __name__=='__main__':
	parser = argparse.ArgumentParser(description='This tool converts the ground truth txt file format used by the vision.in.tum.de datasets into a .log file that can be used with generateAll.py. Not only it converts the original quaternion-based angle representation into a euler-based one, it also realignes and rotates the ground truth reference frame to match the one used by the SLAM representation in order to allow meaningful comparisons. **NOTE**: this is a highly experimental tool! As we lack a formal and complete definition of the rototranslation required to align the two frames, the value of the angle must be either determined by hand and guesswork or by using the experimental angle estimation routine included in the script; however, even the latter approach requires manual handwork, in that it is necessary to specify a pair of matching timestamp lines in the two files to estimate the angle difference.')
	parser.add_argument('quat_GT_file',help='the log file containing the original GT with angles expressed as quartenions')
	parser.add_argument('slam_file', help='the log file of a SLAM trajectory reconstruction generated from the same run of the GT')
	args = parser.parse_args()
	convertGT(args.quat_GT_file,args.slam_file)