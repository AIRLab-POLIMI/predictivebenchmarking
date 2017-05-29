#!/usr/bin/env python  
'''
This node listens to the tf published by gmapping and writes it to a file with the 
FLASER notation so to be readable from the MetricEvaluator
'''
import roslib
roslib.load_manifest('tf_listener')
import rospy
import math
import tf
import geometry_msgs.msg
import sys

if __name__ == '__main__':
    rospy.init_node('tf_listener', anonymous=True)

    listener = tf.TransformListener()
    tfodom=open(sys.argv[1],"w")

    rate=rospy.Rate(100.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/map','/base_link',rospy.Time(0))
            roteuler=tf.transformations.euler_from_quaternion(rot)
            tfodom.write("FLASER 0 0.0 0.0 0.0 " + str(trans[0]) + " " + str(trans[1]) + " " + str(roteuler[2]) +" "+str(rospy.get_time())+"\n")
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        rate.sleep()
    tfodom.close()