

#include "kinect_proximity_safety_controller/safety_controller.h"
#include <ros/ros.h>
#include <iostream>

using namespace robocom ;


int main(int argc, char** argv){
  std::string name = "kinect_proximity_safety_controller" ;
  ros::init(argc, argv, name);
  ros::NodeHandle nh ;

  KinectSafetyController rangeController(nh, name) ;


  while (ros::ok()){
    rangeController.init() ;
    ros::spin();
  }

  return 0 ;
}
