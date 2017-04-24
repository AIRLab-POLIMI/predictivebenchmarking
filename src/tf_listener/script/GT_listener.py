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
    listener2 = tf.TransformListener()
    listener3 = tf.TransformListener()
    listener4 = tf.TransformListener()
    tfodom_om=open(sys.argv[1]+"om.log","w")
    tfodom_mb=open(sys.argv[1]+"mb.log","w")
    tfodom_bm=open(sys.argv[1]+"bm.log","w")
    tfodom_mo=open(sys.argv[1]+"mo.log","w")

    rate=rospy.Rate(100.0)
    while not rospy.is_shutdown():
        try:
            (trans1,rot1) = listener1.lookupTransform('/odom','/map',rospy.Time(0))
            roteuler1=tf.transformations.euler_from_quaternion(rot1)
            tfodom_om.write("FLASER 0 0.0 0.0 0.0 " + str(trans1[0]) + " " + str(trans1[1]) + " " + str(roteuler1[2]) +" "+str(rospy.get_time())+"\n")

            (trans2,rot2) = listener2.lookupTransform('/map','/odom',rospy.Time(0))
            roteuler2=tf.transformations.euler_from_quaternion(rot2)
            tfodom_mo.write("FLASER 0 0.0 0.0 0.0 " + str(trans2[0]) + " " + str(trans2[1]) + " " + str(roteuler2[2]) +" "+str(rospy.get_time())+"\n")

            (trans3,rot3) = listener3.lookupTransform('/odom','/base_link',rospy.Time(0))
            roteuler3=tf.transformations.euler_from_quaternion(rot3)
            tfodom_bm.write("FLASER 0 0.0 0.0 0.0 " + str(trans3[0]) + " " + str(trans3[1]) + " " + str(roteuler3[2]) +" "+str(rospy.get_time())+"\n")

            (trans4,rot4) = listener4.lookupTransform('/map','/base_link',rospy.Time(0))
            roteuler4=tf.transformations.euler_from_quaternion(rot4)
            tfodom_mb.write("FLASER 0 0.0 0.0 0.0 " + str(trans4[0]) + " " + str(trans4[1]) + " " + str(roteuler4[2]) +" "+str(rospy.get_time())+"\n")

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        rate.sleep()
    tfodom_om.close()
    tfodom_mb.close()
    tfodom_bm.close()
    tfodom_mo.close()