#!/usr/bin/env python  
'''
This node listens to the tf published by gmapping and writes it to a file with the 
FLASER notation so to be readable from the MetricEvaluator
'''
import roslib
roslib.load_manifest('tf_listener')
import rospy
import math
import tf2_ros
import tf2_geometry_msgs
import geometry_msgs.msg
import sys

def callback(pose):
    # Each time I get a pose, I should transform it
    global static_trans
    # I get the fixed static transform between the two
    static_transform = tf_buffer.lookup_transform('map','world',rospy.Time(0),rospy.Duration(1.0))
    pose_transformed = tf2_geometry_msgs.do_transform_pose(pose, static_transform)
    pub.publish(pose_transformed)

if __name__ == '__main__':
    global static_trans
    global pub
    global tf_buffer
    rospy.init_node('tf_listener', anonymous=True)
    tf_buffer = tf2_ros.Buffer(rospy.Duration(10.0)) #tf buffer length
    listener = tf2_ros.TransformListener(tf_buffer)

    tfodom=open(sys.argv[1],"w")

    rate=rospy.Rate(100.0)
    # I create a new topic
    pub = rospy.Publisher('/optitrack_pose', geometry_msgs.msg.PoseStamped, queue_size=10)
    # Then I subscribe to pose
    rospy.Subscriber("/pose", geometry_msgs.msg.PoseStamped, callback)

    while not rospy.is_shutdown():
        rate.sleep()
    tfodom.close()

