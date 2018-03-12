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

def make_tf_msg(x, y, theta, t):
    trans = TransformStamped()
    trans.header.stamp = t
    trans.header.frame_id = '/base_link'
    trans.child_frame_id = '/base_laser_link'
    trans.transform.translation.x = x
    trans.transform.translation.y = y
    trans.transform.translation.z = 0.45
    q = tf.transformations.quaternion_from_euler(0, 0, theta)
    trans.transform.rotation.x = q[0]
    trans.transform.rotation.y = q[1]
    trans.transform.rotation.z = q[2]
    trans.transform.rotation.w = q[3]

    msg = TFMessage()
    msg.transforms.append(trans)
    return msg

def csv2bag(ground_truth_file,odometry_file,laser_file,output_folder):
    output_folder = sys.argv[4]
    # infer name from ground truth
    dataset_name = sys.argv[1].split('/')[-1]
    savename = join(output_folder,dataset_name.split('.')[0])+'.bag'
    print savename
    # we need to read these 3 data elements together
    # idea: we build a dictionary were keys are timestamps
    dataset = [] 
    dataset_items = {'ground_truth': sys.argv[1],'odometry': sys.argv[2], 'laser': sys.argv[3]}
    for key,value in dataset_items.iteritems():
        dataset_item = open(value)
        # skip the csv header
        first = True
        for line in dataset_item.readlines():
            if first:
                first = False
            else:
                line = line.strip()
                tokens = line.split(',')
                timestamp = float(tokens[0])
                tokens = [elem.strip() for elem in tokens]
                data = (key, ','.join(tokens[1:]))      
                dataset.append((timestamp, data))      
        dataset_item.close()
    # probably useful to sort here
    dataset = sorted(dataset, key=lambda x: x[0])

    bag = rosbag.Bag(savename, 'w')
    iteration = 0
    odom_x, odom_y, odom_theta = 0,0,0
    for timestamp, data in dataset:
        # we need to decide how to interpret this data
        if True:#iteration%20==0:
            if data[0] == 'ground_truth':
                line = data[1].strip()
                tokens = line.split(',')
                msg = Odometry()
                msg.header.frame_id = 'odom'
                t = rospy.Time(timestamp)
                msg.header.stamp = t       
                msg.pose.pose.position.x = float(tokens[0])
                msg.pose.pose.position.y = float(tokens[1])
                msg.pose.pose.position.z = 0.0
                odom_quat = tf.transformations.quaternion_from_euler(0, 0, float(tokens[2]))
                msg.pose.pose.orientation = Quaternion(*odom_quat)
                msg.child_frame_id = "base_link"
                # I have to figure out if this data is available
                msg.twist.twist.linear.x = 0.0
                msg.twist.twist.linear.y = 0.0
                msg.twist.twist.angular.z =  0.0
                bag.write('base_pose_ground_truth', msg, t)

            elif data[0] == 'odometry':
                line = data[1].strip()
                tokens = line.split(',')

                msg = Odometry()
                msg.header.frame_id = 'odom'
                t = rospy.Time(timestamp)
                msg.header.stamp = t       
                msg.pose.pose.position.x = float(tokens[3])
                msg.pose.pose.position.y = float(tokens[4])
                msg.pose.pose.position.z = 0.0
                odom_quat = tf.transformations.quaternion_from_euler(0, 0, float(tokens[5]))
                msg.pose.pose.orientation = Quaternion(*odom_quat)
                msg.child_frame_id = "base_link"
                # I have to figure out if this data is available
                msg.twist.twist.linear.x = 0.0
                msg.twist.twist.linear.y = 0.0
                msg.twist.twist.angular.z =  0.0

                bag.write('odom', msg, t)

                odom_trans = TransformStamped()
                odom_trans.header.stamp = rospy.Time(timestamp)
                odom_trans.header.frame_id = "/odom"
                odom_trans.child_frame_id = "/base_link"
                odom_trans.transform.translation.x = float(tokens[3])
                odom_trans.transform.translation.y = float(tokens[4])
                odom_trans.transform.translation.z = 0.0
                odom_trans.transform.rotation = Quaternion(*odom_quat)
                tf_msg = TFMessage()
                tf_msg.transforms.append(odom_trans)
                bag.write('tf', tf_msg, t)

                odom_x, odom_y, odom_theta = [float(t) for t in tokens[3:6]]
                t = rospy.Time(timestamp)
                tf_msg = make_tf_msg(0.08, 0.0, 0.0, t)
                bag.write('tf', tf_msg, t)
            elif data[0] == 'laser':
                line = data[1].strip()
                tokens = line.split(',')

                msg = LaserScan()
                num_scans = len(tokens)-2

                msg.header.frame_id = 'base_laser_link'
                t = rospy.Time(timestamp)
                msg.header.stamp = t
                msg.angle_min = -90.0 / 180.0 * pi
                msg.angle_max = 90.0 / 180.0 * pi
                msg.angle_increment = pi / num_scans
                msg.time_increment = 0.2 / 360.0
                msg.scan_time = 0.2
                msg.range_min = 0.001
                msg.range_max = 50.0
                msg.ranges = [float(r) for r in tokens[2:(num_scans + 1)]]

                bag.write('base_scan', msg, t)

                # experimental: reuse immediately preceding odometry data as pose
                #t = rospy.Time(timestamp)
                #tf_msg = make_tf_msg(odom_x, odom_y, odom_theta, t)
                #bag.write('tf', tf_msg, t)
        iteration+=1

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='This tool merges the ground truth, odometry and laser csv files of the RAWSEEDS Bicocca dataset into a single ROS .bag file, performing the necessary synchronisation adjustments. The resulting file is stored in the <output_folder> with the same name of the ground truth file and can be subsequently played and inspected with the standard rosbag tool. It is an expansion of a previous work made by Martin Guenther.')
    parser.add_argument('ground_truth_file',help='the csv file containing the ground truth poses')
    parser.add_argument('odometry_file',help='the csv file containing the odometry data')
    parser.add_argument('laser_file',help='the csv file containing the SICK laser data')
    parser.add_argument('output_folder', help='the folder where the converted bag files are stored')
    args = parser.parse_args()
    csv2bag(args.ground_truth_file,args.odometry_file,args.laser_file,args.output_folder)
