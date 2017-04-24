#!/usr/bin/env python
import rospy,rosbag
import numpy as np
from sensor_msgs.msg import LaserScan

def listener():
	rospy.init_node('lasernoise', anonymous=True)

	rospy.Subscriber("base_scan", LaserScan, talker)

	rospy.spin()

def talker(data):
	pub = rospy.Publisher('base_scan_noise', LaserScan, queue_size=1)
	noiseranges=data.ranges
	noise=np.random.normal(0,0.3,len(noiseranges))
	noiseranges += noise
	data.ranges=noiseranges
	pub.publish(data)

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass