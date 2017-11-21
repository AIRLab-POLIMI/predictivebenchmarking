cmake_minimum_required(VERSION 2.8.3)
project(kinect_proximity_safety_controller)

set(catkin_RUN_PACKAGES
  actionlib
  cv_bridge
  sensor_msgs
  roslib
  roscpp
  image_transport
)

set(catkin_BUILD_PACKAGES
  ${catkin_RUN_PACKAGES}
  cmake_modules
  dynamic_reconfigure
)

find_package(OpenCV REQUIRED)
find_package(Boost REQUIRED COMPONENTS system thread filesystem)

find_package(catkin REQUIRED COMPONENTS
  nodelet
  pluginlib
  geometry_msgs
  roscpp
  rospy
  std_msgs
  ${catkin_BUILD_PACKAGES}
)


catkin_package(
  INCLUDE_DIRS include
  LIBRARIES kinect_proximity_safety_controller_nodelet
  CATKIN_DEPENDS nodelet roscpp rospy std_msgs pluginlib geometry_msgs sensor_msgs
  DEPENDS OpenCV Boost
)


include_directories(include
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS}
)


 add_library(kinect_proximity_safety_controller_nodelet
   src/safety_controller.cpp
 )
 add_dependencies(kinect_proximity_safety_controller_nodelet
   ${catkin_EXPORTED_TARGETS}
 )
 target_link_libraries(kinect_proximity_safety_controller_nodelet
   ${catkin_LIBRARIES}
   ${OpenCV_LIBRARIES}
   ${Boost_LIBRARIES}
 )

add_executable(kinect_proximity_safety_controller_node 
    src/nodes/robocom_safety_controller_node.cpp
)
target_link_libraries(kinect_proximity_safety_controller_node 
    ${catkin_LIBRARIES}
)

 install(TARGETS kinect_proximity_safety_controller_nodelet
   DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
 )


 install(DIRECTORY include/${PROJECT_NAME}/
   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
 )

  install(DIRECTORY plugins
   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
 )

#  install(DIRECTORY launch
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )
 
