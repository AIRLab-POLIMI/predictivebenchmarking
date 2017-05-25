# Install script for directory: /home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ros/slampbenchmarking/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/adhoc_communication/msg" TYPE FILE FILES
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/adhoc_communication/srv" TYPE FILE FILES
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv"
    "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/adhoc_communication/cmake" TYPE FILE FILES "/home/ros/slampbenchmarking/build/aau_multi_robot/adhoc_communication/catkin_generated/installspace/adhoc_communication-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/ros/slampbenchmarking/devel/include/adhoc_communication")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/ros/slampbenchmarking/devel/share/roseus/ros/adhoc_communication")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/ros/slampbenchmarking/devel/share/common-lisp/ros/adhoc_communication")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/ros/slampbenchmarking/devel/share/gennodejs/ros/adhoc_communication")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/ros/slampbenchmarking/devel/lib/python2.7/dist-packages/adhoc_communication")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/ros/slampbenchmarking/devel/lib/python2.7/dist-packages/adhoc_communication")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/ros/slampbenchmarking/build/aau_multi_robot/adhoc_communication/catkin_generated/installspace/adhoc_communication.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/adhoc_communication/cmake" TYPE FILE FILES "/home/ros/slampbenchmarking/build/aau_multi_robot/adhoc_communication/catkin_generated/installspace/adhoc_communication-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/adhoc_communication/cmake" TYPE FILE FILES
    "/home/ros/slampbenchmarking/build/aau_multi_robot/adhoc_communication/catkin_generated/installspace/adhoc_communicationConfig.cmake"
    "/home/ros/slampbenchmarking/build/aau_multi_robot/adhoc_communication/catkin_generated/installspace/adhoc_communicationConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/adhoc_communication" TYPE FILE FILES "/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/package.xml")
endif()

