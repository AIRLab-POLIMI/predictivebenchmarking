# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "nav2d_operator: 1 messages, 0 services")

set(MSG_I_FLAGS "-Inav2d_operator:/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(nav2d_operator_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg" NAME_WE)
add_custom_target(_nav2d_operator_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "nav2d_operator" "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(nav2d_operator
  "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/nav2d_operator
)

### Generating Services

### Generating Module File
_generate_module_cpp(nav2d_operator
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/nav2d_operator
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(nav2d_operator_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(nav2d_operator_generate_messages nav2d_operator_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg" NAME_WE)
add_dependencies(nav2d_operator_generate_messages_cpp _nav2d_operator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(nav2d_operator_gencpp)
add_dependencies(nav2d_operator_gencpp nav2d_operator_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS nav2d_operator_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(nav2d_operator
  "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/nav2d_operator
)

### Generating Services

### Generating Module File
_generate_module_eus(nav2d_operator
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/nav2d_operator
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(nav2d_operator_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(nav2d_operator_generate_messages nav2d_operator_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg" NAME_WE)
add_dependencies(nav2d_operator_generate_messages_eus _nav2d_operator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(nav2d_operator_geneus)
add_dependencies(nav2d_operator_geneus nav2d_operator_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS nav2d_operator_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(nav2d_operator
  "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/nav2d_operator
)

### Generating Services

### Generating Module File
_generate_module_lisp(nav2d_operator
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/nav2d_operator
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(nav2d_operator_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(nav2d_operator_generate_messages nav2d_operator_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg" NAME_WE)
add_dependencies(nav2d_operator_generate_messages_lisp _nav2d_operator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(nav2d_operator_genlisp)
add_dependencies(nav2d_operator_genlisp nav2d_operator_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS nav2d_operator_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(nav2d_operator
  "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/nav2d_operator
)

### Generating Services

### Generating Module File
_generate_module_nodejs(nav2d_operator
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/nav2d_operator
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(nav2d_operator_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(nav2d_operator_generate_messages nav2d_operator_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg" NAME_WE)
add_dependencies(nav2d_operator_generate_messages_nodejs _nav2d_operator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(nav2d_operator_gennodejs)
add_dependencies(nav2d_operator_gennodejs nav2d_operator_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS nav2d_operator_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(nav2d_operator
  "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/nav2d_operator
)

### Generating Services

### Generating Module File
_generate_module_py(nav2d_operator
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/nav2d_operator
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(nav2d_operator_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(nav2d_operator_generate_messages nav2d_operator_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ros/slambenchmarking/src/navigation_2d/nav2d_operator/msg/cmd.msg" NAME_WE)
add_dependencies(nav2d_operator_generate_messages_py _nav2d_operator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(nav2d_operator_genpy)
add_dependencies(nav2d_operator_genpy nav2d_operator_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS nav2d_operator_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/nav2d_operator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/nav2d_operator
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/nav2d_operator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/nav2d_operator
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/nav2d_operator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/nav2d_operator
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/nav2d_operator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/nav2d_operator
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/nav2d_operator)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/nav2d_operator\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/nav2d_operator
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
