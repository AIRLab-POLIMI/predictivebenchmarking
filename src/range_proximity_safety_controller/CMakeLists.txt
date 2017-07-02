cmake_minimum_required(VERSION 2.8.3)
project(range_proximity_safety_controller)


find_package(catkin REQUIRED COMPONENTS
  nodelet
  pluginlib
  geometry_msgs
  roscpp
  rospy
  std_msgs
)


catkin_package(
  INCLUDE_DIRS include
  LIBRARIES range_proximity_safety_controller_nodelet
  CATKIN_DEPENDS nodelet roscpp rospy std_msgs pluginlib geometry_msgs 
)


include_directories(include
  ${catkin_INCLUDE_DIRS}
)


 add_library(range_proximity_safety_controller_nodelet
   src/safety_controller.cpp
 )
 add_dependencies(range_proximity_safety_controller_nodelet
   ${catkin_EXPORTED_TARGETS}
 )
 target_link_libraries(range_proximity_safety_controller_nodelet
   ${catkin_LIBRARIES}
 )

add_executable(range_proximity_safety_controller_node 
    src/nodes/beebot_safety_controller_node.cpp
)
target_link_libraries(range_proximity_safety_controller_node 
    ${catkin_LIBRARIES}
)

 install(TARGETS range_proximity_safety_controller_nodelet
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
 
