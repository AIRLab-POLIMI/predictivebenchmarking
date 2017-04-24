#!/usr/bin/env python  
import roslib
roslib.load_manifest('tf_listener')
import rospy
import math
import tf
import geometry_msgs.msg
import sys

if __name__ == '__main__':
    rospy.init_node('tf_listener', anonymous=True)

    listener1 = tf.TransformListener()
    tfodom=open(sys.argv[1],"w")

    rate=rospy.Rate(100.0)
    while not rospy.is_shutdown():
        try:
            (trans1,rot1) = listener1.lookupTransform('/map','/base_link',rospy.Time(0))
            roteuler1=tf.transformations.euler_from_quaternion(rot1)
            tfodom.write("FLASER 0 0.0 0.0 0.0 " + str(trans1[0]) + " " + str(trans1[1]) + " " + str(roteuler1[2]) +" "+str(rospy.get_time())+"\n")

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        rate.sleep()
    tfodom.close()
