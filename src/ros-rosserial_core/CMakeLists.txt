cmake_minimum_required(VERSION 2.8.3)
project(rosserial_core)
find_package(catkin REQUIRED)

catkin_package(
  CATKIN_DEPENDS message_runtime
)

install(DIRECTORY src/ros_lib
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/src
)

install(PROGRAMS src/rosserial_core/make_libraries.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
