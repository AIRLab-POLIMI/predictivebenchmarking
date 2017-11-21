#include <vector>
#include <string>
#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <nav_msgs/Path.h>
#include "robocom/PathPublisher.h"

PathPublisher::PathPublisher(ros::NodeHandle& nh, string tfPosTargetFrame, string tfPosSourceFrame,
				string pathHeaderFrameId, string pathTopic)
	: nh(nh), tfPosTargetFrame(tfPosTargetFrame), tfPosSourceFrame(tfPosSourceFrame),
		pathHeaderFrameId(pathHeaderFrameId), pathTopic(pathTopic) {
	pathPublisher = nh.advertise<nav_msgs::Path>(pathTopic, 50);
	poses = vector<geometry_msgs::PoseStamped>(0);
}

void PathPublisher::getPose() {
	tf::StampedTransform transform;
	try {
		listener.lookupTransform(tfPosTargetFrame, tfPosSourceFrame, ros::Time(0), transform);

		geometry_msgs::PoseStamped poseStamped;
   		poseStamped.header.stamp = ros::Time::now();
		poseStamped.header.frame_id = pathHeaderFrameId;
   		poseStamped.pose.position.x = transform.getOrigin().getX();
   		poseStamped.pose.position.y = transform.getOrigin().getY();
  		poseStamped.pose.position.z = transform.getOrigin().getZ();
		poseStamped.pose.orientation.x = transform.getRotation().getX();
		poseStamped.pose.orientation.y = transform.getRotation().getY();
		poseStamped.pose.orientation.z = transform.getRotation().getZ();
		poseStamped.pose.orientation.w = transform.getRotation().getW();
   		poses.push_back(poseStamped);

   		ROS_INFO("getPose");

	} catch (tf::TransformException ex) {
		ROS_ERROR("%s",ex.what());
	}
}

void PathPublisher::publishPath() {
	nav_msgs::Path path;
	path.header.stamp = ros::Time::now();
  	path.header.frame_id = pathHeaderFrameId;
   	path.poses = poses;
   	pathPublisher.publish(path);
}
