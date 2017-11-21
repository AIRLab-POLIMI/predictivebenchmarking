/*
 * Copyright (c) 2016, NTU iCeiRA.
 * All right reserved
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of Yujin Robot nor the names of its
 *       contributors may be used to endorse or promote products derived from
 *       this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

/**
 * @file kinect_proximity_safety_controller/include/kinect_proximity_safety_controller/safety_controller.h
 *
 * @brief range safety controller relying on kinect scannings.
 *
 * This controller uses only kinect scanning to serves as a proximity detecting and obstacle avoiding controller.
 *
 * @author Valerio Castelli, Politecnico di Milano
 *
 **/

/************************************************************************
 * Ifdefs
 ************************************************************************/

#ifndef _SAFETY_CONTROLLER_H_
#define _SAFETY_CONTROLLER_H_

/*************************************************************************
 * Includes
 *************************************************************************/

#include <string>
#include <boost/concept_check.hpp>
#include <boost/graph/graph_concepts.hpp>
#include <ros/ros.h>
#include <std_msgs/Empty.h>
#include <geometry_msgs/Twist.h>
#include <sensor_msgs/LaserScan.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <sensor_msgs/Image.h>
#include <actionlib_msgs/GoalID.h>
#include <stdio.h>

namespace enc = sensor_msgs::image_encodings;

namespace robocom
{
  /**
   * @brief keeps track of safety distance and commands the reactive evasive maneuvre accordingly.
   *
   * The SafetyController keeps track of lethal range from the laser readings, Potential Field with upper bound
   * will be used to determine a gradient of repulsive velocity. Once out of the range of action, the controller
   * will be shut down.
   *
   * The Safety Controller should be used in conjuction with Velocity Multiplexer and Velocity Smoother.
   **/
// Values expressed in millimeters
#define ROWS 240
#define COLS 320
#define RES ROWS*COLS
#define MIN_INITIAL_DEPTH 50000
#define MIN_ACCEPTABLE_DEPTH 600
#define SAFETY_THRESHOLD 30// percent
#define EXTRA_SAFETY_ESCAPE_DURATION 4 // seconds
  class KinectSafetyController
  {

  public:
    KinectSafetyController(ros::NodeHandle& nh, std::string& name) :
      nh_(nh),
      name_(name),
      last_event_time_(ros::Time(0)),
      cmdvel_(new geometry_msgs::Twist()){} ;
    ~KinectSafetyController(){} ;

    /**
     * Set up necessary publishers/subscrivers and variables
     * @return true, if successful
     */
    bool init()
    {
      // how long to keep sending messages after the range is breached.
      double time_to_extend_repulsion ;

      nh_.getParam("SafetyController/time_to_extend_repulsion", time_to_extend_repulsion) ;
      nh_.getParam("SafetyController/safety_threshold", safetyThresh) ;

      time_to_extend_repulsion_ = ros::Duration(time_to_extend_repulsion) ;

      sub_ = nh_.subscribe("/camera/depth/image_raw", 20, &KinectSafetyController::imageCallback,this) ;

      velocity_command_publisher_ = nh_.advertise< geometry_msgs::Twist >("cmd_vel", 10) ;

	  move_base_goal_stopper_ = nh_.advertise<actionlib_msgs::GoalID>("move_base/cancel",10);

	  isRobotSafe_ = true;

      return true ;
    }

    /**
     * @brief If an event flag is received, the controller is activated and proceed to evasive maneuvre
     */
    void evasiveMan(bool rangeBreached_) ;

  private:
    ros::NodeHandle nh_ ;
    std::string name_ ;
    ros::Subscriber reset_safety_states_subscriber_ ;
    ros::Publisher velocity_command_publisher_ ;
    ros::Publisher move_base_goal_stopper_ ;
    ros::Subscriber sub_ ;
    ros::Duration time_to_extend_repulsion_ ;
    ros::Time last_event_time_ ;
    bool rangeBreached_ ;
	bool isRobotSafe_;
    double safetyThresh ;  // in meters

    float scan_min_range, scan_min_angle ;

    geometry_msgs::TwistPtr cmdvel_ ;  // velocity commands


    /**
     * @brief Keep track of laser readings. Once passing the allowed range, a flag is raised
     * announcing an event
     */
    void laserScanVigilanteCB(const sensor_msgs::LaserScan::ConstPtr& msg) ;

	void imageCallback(const sensor_msgs::ImageConstPtr& msg);

  } ;  // Class definition


void KinectSafetyController::imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
    cv_bridge::CvImagePtr cv_ptr;
    try
    {
      cv_ptr = cv_bridge::toCvCopy(msg, enc::TYPE_16UC1);//now cv_ptr is the matrix, do not forget "TYPE_" before "16UC1"
    }
    catch (cv_bridge::Exception& e)
    {
      ROS_ERROR("cv_bridge exception: %s", e.what());
      return;
    }

 // This could probably be some % threshold, like if 30% of the values are below the minimum threshold then stop
// (this is to avoid false readings of individual pixels)
	ushort minDepth = MIN_INITIAL_DEPTH; // 5 meters is far enough to be overwritten by actual depth data
	int numCriticalPixels = 0;
	// Kinect depth camera il 320 columns x 240 rows
	for (short r = 0; r < 240; r++){
		for (short c = 0; c < 320; c++){
			ushort depth = cv_ptr->image.at<ushort>(cv::Point(r,c));
			if (depth > 0 && depth < minDepth) // 0 is an invalid number that is returned if no data is available
				minDepth = depth;
			//if (depth < MIN_ACCEPTABLE_DEPTH)
				//numCriticalPixels++;
		}
	}
    //ushort depth = cv_ptr->image.at<ushort>(cv::Point(400,400));//you can change 240,320 to your interested pixel
	// if we fall here, it's actually because ALL pixels are reporting a 0 value, which means object too close to estimate
	// its distance, so we forcefully set the value to the minimum acceptable depth
	if (minDepth == MIN_INITIAL_DEPTH)
		minDepth = MIN_ACCEPTABLE_DEPTH;
    //ROS_INFO("Depth: %hu", minDepth);
	//float perc = (float)numCriticalPixels / RES * 100;
	if (minDepth <= MIN_ACCEPTABLE_DEPTH){
    	//ROS_INFO("WARNING: TOO CLOSE!");
		if (isRobotSafe_) {
			// If we get too close, immediately stop robot and cancel goal
			actionlib_msgs::GoalID goal_msg;
			move_base_goal_stopper_.publish(goal_msg);
			isRobotSafe_ = false;
			// wait a couple of seconds for safety
        	ros::Duration(2.0).sleep();
			// Then trigger the recovery behavior
        	cmdvel_.reset(new geometry_msgs::Twist());
        	cmdvel_->angular.z = 0.0;
        	cmdvel_->linear.x = -0.1;
			ROS_INFO("Kinect says we're too close, distance is %hu - reversing thrust",minDepth);
			velocity_command_publisher_.publish(cmdvel_);
		}
	}
	else{
		if (!isRobotSafe_) {
			// if we get here, we have just come back into the safe zone
			// but don't immediately stop, it's better to put some extra space between us and the obstacle
			float elapsed_time = 0;
			ROS_INFO("Distance is now %hu", minDepth);
			while (elapsed_time < EXTRA_SAFETY_ESCAPE_DURATION){
				ROS_INFO("Extending reverse thrust period");
           		ros::Duration(0.5).sleep();
            	elapsed_time+=0.5;
			}
			// once we get out of here, we are reasonably certain to be safe - stop robot and wait for planner
			cmdvel_.reset(new geometry_msgs::Twist());
	        cmdvel_->angular.z = 0.0;
	        cmdvel_->linear.x = 0.0;
			ROS_INFO("We should be ok now, stopping reverse thrust");
			velocity_command_publisher_.publish(cmdvel_);
		}
		isRobotSafe_ = true;
	}
}



void KinectSafetyController::laserScanVigilanteCB(const sensor_msgs::LaserScan::ConstPtr& msg)
{
  scan_min_range = msg->ranges[0] ;
  scan_min_angle = 0 ;

  for (int j = 0 ; j <=180; j++) {
    if(msg->ranges[j] < scan_min_range){
      scan_min_range = msg->ranges[j] ;
      scan_min_angle = j/2 ;
    }
  }
  //std::cout << "minimum range is " << scan_min_range << "at angle of" << scan_min_angle << "." << std::endl ;
  //ROS_INFO_STREAM("Minimum range is " << scan_min_range << "at angle of" << scan_min_angle << ".") ;

  if (scan_min_range <= safetyThresh ){
    rangeBreached_ = true ;
    last_event_time_ = ros::Time::now() ;
    ROS_WARN_STREAM("Safety range breached !! Safety Controller enabled") ;
    KinectSafetyController::evasiveMan(rangeBreached_);
  }
  else{
    rangeBreached_ = false ;
  }
}

void KinectSafetyController::evasiveMan(bool rangeBreached_)
{

  if(rangeBreached_ = true){
    ROS_WARN_STREAM("Begin evasive maneuvre") ;
    // if the obstacle is at the right side of the robot
    if(scan_min_angle < 90){
      cmdvel_.reset(new geometry_msgs::Twist()) ;
      cmdvel_->angular.z = 0.2 ;
      cmdvel_->linear.x = -0.1 ;
      std::cout << "reversing left" << std::endl ;
      velocity_command_publisher_.publish(cmdvel_) ;
    }
    // if the obstacle is at the left side of the robot
    else {
      cmdvel_.reset(new geometry_msgs::Twist()) ;
      cmdvel_->angular.z = -0.2 ;
      cmdvel_->linear.x = -0.1 ;
      std::cout << "reversing right" << std::endl ;
      velocity_command_publisher_.publish(cmdvel_) ;
    }
  }
    // if we want to extend the safet state and we are within the time, just keep sending velocity command.
  else if(time_to_extend_repulsion_ > ros::Duration(1e-10) &&
           ros::Time::now() - last_event_time_ < time_to_extend_repulsion_) {
    velocity_command_publisher_.publish(cmdvel_);
  }

}



} // namespace

#endif
