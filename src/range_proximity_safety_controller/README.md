# range_proximity_safety_controller

Range Proximity Safety Controller only needs laser scanning as input to act as a spontaneous safety controller depending on the detected ranges of the vehicle in relation to the robot. The project only depends on a single frontal laser range finder. However, it is possible to apply on rear laser scanner as well if you know how to do, hehe.

# 1. Motivation

This project is created under the necessity of using autonomous navigation on erratic robot which may collide with anything in its path as the planner may not be able to replan instantaneously for some mysterious reasons. The safety controller prevent the robot from running into wall or obstacles by issueing cmd_vel command to the driver. Thus, this safety controller may be used under similar framework to [Kobuki control system](http://wiki.ros.org/kobuki/Tutorials/Kobuki's%20Control%20System) and don't forget to remap the cmd_vel topic to your own. Failing to do so would have you prepare to get your robot screwed up!  :bomb:

The project is still under development, but that does not mean you can't use it at your own risk. :stuck_out_tongue: I wrote it as a node, but it was originally intended to be a NODELET ! If I have some spare time will come back and fix it. 

And one last thing. Relax! The node only requires laser scan, no tf frame or odometry is needed, so, enjoy! You are welcome.

## 1.1 Subscribed Topics

scan ([sensor_msgs/LaserScan](http://docs.ros.org/api/sensor_msgs/html/msg/LaserScan.html))
  
  The laser scan used for distance verification.

## 1.2 Published Topics

cmd_vel ([geometry_msgs/Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html))
  
  Output velocity. When used in conjuction with a velocity multiplexe, remap it to ~/cmd_vel_safety for safety velocity command.

# 2. Installation

To install it, first get your workspace set up. If you don't know what to do, head over to [How to create ROS Workspace](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

If you have the workspace up and running, open a terminal, cd the workspace's directory and clone this package as:

	git clone https://github.com/Megacephalo/range_proximity_safety_controller.git

then, compile it as:

	roscd && cd ..
	catkin_make

If you hit 100% no error, you are all set and ready to go !

# 3. Test

Before you solemnly swear that you are up to no good with this package, please try

	roslaunch range_proximity_safety_controller proximity_range_safety_controller_node.launch

This launch file launches the node range_proximity_safety_controller_node. If you want to know how remap its topic in a launch file, refer to its source code file as such:

	roscd range_proximity_safety_controller/launch/

and open the file proximity_range_safety_controller_node.launch and watch how the heck it works. One important thing is that you can adjust two parameters with the config file at the config file. It should come in handy!
	
# 4. Contributors

This project is created and maintenanted by:

Charly Huang a.k.a. Megacephalo

National Taiwan University, iCeiRA
June 16, 2016

