#! /usr/bin/env python
import rospy
import time
from std_srvs.srv import Trigger

def explore():
	m=rospy.ServiceProxy('/StartMapping',Trigger)
	m()
	time.sleep(30)
	e=rospy.ServiceProxy('/StartExploration',Trigger)
	e()

if __name__ == '__main__':
    try:
        explore()
    except rospy.ROSInterruptException:
        pass