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
 * @file range_proximity_safety_controller/include/range_proximity_safety_controller/safety_controller.h 
 * 
 * @brief range safety controller relying on laser scannings.
 * 
 * This controller uses only laser scaning to serves as a proximity detecting and obstacle avoiding controller.
 * 
 * @author Charly Huang, NTU iCeiRA
 * 
 * Big thanks to Yujin Robot for inspiring this project.
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
#include <stdio.h>

namespace beebot
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
  class SafetyController
  {
  public:
    SafetyController(ros::NodeHandle& nh, std::string& name) :
      nh_(nh),
      name_(name),
      last_event_time_(ros::Time(0)),
      cmdvel_(new geometry_msgs::Twist()){} ;
    ~SafetyController(){} ;
    
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

      laser_sub_ = nh_.subscribe("scan", 20, &SafetyController::laserScanVigilanteCB, this) ;
      
      velocity_command_publisher_ = nh_.advertise< geometry_msgs::Twist >("cmd_vel", 10) ;
      
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
    ros::Subscriber laser_sub_ ;
    ros::Duration time_to_extend_repulsion_ ;
    ros::Time last_event_time_ ;
    bool rangeBreached_ ;
    double safetyThresh ;  // in meters
    
    float scan_min_range, scan_min_angle ;
    
    geometry_msgs::TwistPtr cmdvel_ ;  // velocity commands
    
    
    /**
     * @brief Keep track of laser readings. Once passing the allowed range, a flag is raised
     * announcing an event
     */ 
    void laserScanVigilanteCB(const sensor_msgs::LaserScan::ConstPtr& msg) ;
    
  } ;  // Class definition



void SafetyController::laserScanVigilanteCB(const sensor_msgs::LaserScan::ConstPtr& msg)
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
    SafetyController::evasiveMan(rangeBreached_);
  }
  else{
    rangeBreached_ = false ;
  }
}

void SafetyController::evasiveMan(bool rangeBreached_)
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
