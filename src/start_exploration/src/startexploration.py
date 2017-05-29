#! /usr/bin/env python
'''
This node calls the 2 services to start the exploration with nav2d
'''
import rospy
import time
from std_srvs.srv import Trigger

def explore():
	m=rospy.ServiceProxy('/StartMapping',Trigger)
	m()
	time.sleep(25)
	e=rospy.ServiceProxy('/StartExploration',Trigger)
	e()

if __name__ == '__main__':
    try:
        explore()
    except rospy.ROSInterruptException:
        pass