# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "adhoc_communication: 14 messages, 18 services")

set(MSG_I_FLAGS "-Iadhoc_communication:/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Inav_msgs:/opt/ros/kinetic/share/nav_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(adhoc_communication_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv" "adhoc_communication/ExpFrontierElement:adhoc_communication/ExpFrontier"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg" "adhoc_communication/ExpFrontierElement"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg" "adhoc_communication/ExpClusterElement"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv" "adhoc_communication/ExpCluster:adhoc_communication/ExpClusterElement"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv" "adhoc_communication/MmPoint"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv" "geometry_msgs/Quaternion"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv" "adhoc_communication/ExpCluster:adhoc_communication/ExpAuctionElement:adhoc_communication/ExpClusterElement:adhoc_communication/ExpAuction"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv" "geometry_msgs/PoseStamped:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/Point:geometry_msgs/Pose:adhoc_communication/MmRobotPosition"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv" "geometry_msgs/Twist:geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv" "adhoc_communication/MmControl"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg" "adhoc_communication/MmPoint"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv" "nav_msgs/MapMetaData:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/Point:nav_msgs/OccupancyGrid:adhoc_communication/MmMapUpdate:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv" "nav_msgs/MapMetaData:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/Point:nav_msgs/OccupancyGrid:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv" "adhoc_communication/CMgrRobotUpdate:adhoc_communication/CMgrDimensions"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv" "adhoc_communication/CMgrRobotUpdate:adhoc_communication/CMgrDimensions"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv" ""
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg" "nav_msgs/MapMetaData:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/Point:nav_msgs/OccupancyGrid:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg" "adhoc_communication/ExpCluster:adhoc_communication/ExpClusterElement:adhoc_communication/ExpAuctionElement"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg" "adhoc_communication/CMgrDimensions"
)

get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg" NAME_WE)
add_custom_target(_adhoc_communication_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "adhoc_communication" "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg" "geometry_msgs/Quaternion:geometry_msgs/PoseStamped:geometry_msgs/Pose:std_msgs/Header:geometry_msgs/Point"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)

### Generating Services
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_cpp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
)

### Generating Module File
_generate_module_cpp(adhoc_communication
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(adhoc_communication_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(adhoc_communication_generate_messages adhoc_communication_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_cpp _adhoc_communication_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(adhoc_communication_gencpp)
add_dependencies(adhoc_communication_gencpp adhoc_communication_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS adhoc_communication_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_msg_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)

### Generating Services
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)
_generate_srv_eus(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
)

### Generating Module File
_generate_module_eus(adhoc_communication
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(adhoc_communication_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(adhoc_communication_generate_messages adhoc_communication_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_eus _adhoc_communication_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(adhoc_communication_geneus)
add_dependencies(adhoc_communication_geneus adhoc_communication_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS adhoc_communication_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_msg_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)

### Generating Services
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)
_generate_srv_lisp(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
)

### Generating Module File
_generate_module_lisp(adhoc_communication
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(adhoc_communication_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(adhoc_communication_generate_messages adhoc_communication_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_lisp _adhoc_communication_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(adhoc_communication_genlisp)
add_dependencies(adhoc_communication_genlisp adhoc_communication_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS adhoc_communication_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_msg_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)

### Generating Services
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)
_generate_srv_nodejs(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
)

### Generating Module File
_generate_module_nodejs(adhoc_communication
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(adhoc_communication_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(adhoc_communication_generate_messages adhoc_communication_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_nodejs _adhoc_communication_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(adhoc_communication_gennodejs)
add_dependencies(adhoc_communication_gennodejs adhoc_communication_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS adhoc_communication_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_msg_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)

### Generating Services
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/PoseStamped.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/nav_msgs/cmake/../msg/MapMetaData.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/nav_msgs/cmake/../msg/OccupancyGrid.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)
_generate_srv_py(adhoc_communication
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv"
  "${MSG_I_FLAGS}"
  "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg;/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
)

### Generating Module File
_generate_module_py(adhoc_communication
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(adhoc_communication_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(adhoc_communication_generate_messages adhoc_communication_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpFrontier.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontier.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpFrontierElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpCluster.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpCluster.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmControl.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrDimensions.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastString.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmPoint.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendQuaternion.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmPoint.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendExpAuction.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpClusterElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/RecvString.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmRobotPosition.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ShutDown.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuctionElement.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendTwist.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmControl.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmListOfPoints.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendMmMapUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendString.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendOccupancyGrid.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/SendCMgrRobotUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetNeighbors.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/ChangeMCMembership.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/BroadcastCMgrRobotUpdate.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/srv/GetGroupState.srv" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmMapUpdate.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/ExpAuction.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/CMgrRobotUpdate.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg/MmRobotPosition.msg" NAME_WE)
add_dependencies(adhoc_communication_generate_messages_py _adhoc_communication_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(adhoc_communication_genpy)
add_dependencies(adhoc_communication_genpy adhoc_communication_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS adhoc_communication_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/adhoc_communication
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(adhoc_communication_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET nav_msgs_generate_messages_cpp)
  add_dependencies(adhoc_communication_generate_messages_cpp nav_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(adhoc_communication_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/adhoc_communication
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(adhoc_communication_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET nav_msgs_generate_messages_eus)
  add_dependencies(adhoc_communication_generate_messages_eus nav_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(adhoc_communication_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/adhoc_communication
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(adhoc_communication_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET nav_msgs_generate_messages_lisp)
  add_dependencies(adhoc_communication_generate_messages_lisp nav_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(adhoc_communication_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/adhoc_communication
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(adhoc_communication_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET nav_msgs_generate_messages_nodejs)
  add_dependencies(adhoc_communication_generate_messages_nodejs nav_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(adhoc_communication_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/adhoc_communication
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(adhoc_communication_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET nav_msgs_generate_messages_py)
  add_dependencies(adhoc_communication_generate_messages_py nav_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(adhoc_communication_generate_messages_py geometry_msgs_generate_messages_py)
endif()
