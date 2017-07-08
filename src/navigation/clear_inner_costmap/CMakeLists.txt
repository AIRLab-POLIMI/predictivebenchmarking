cmake_minimum_required(VERSION 2.8.3)
project(clear_inner_costmap)

find_package(catkin REQUIRED
    COMPONENTS
        cmake_modules
        roscpp
        nav_core
        costmap_2d
        actionlib_msgs
        std_msgs
        pluginlib
        )


find_package(Eigen3 REQUIRED)
find_package(PCL REQUIRED)
remove_definitions(-DDISABLE_LIBUSB-1.0)
find_package(Boost REQUIRED COMPONENTS thread)
include_directories(
    include
    ${catkin_INCLUDE_DIRS}
    ${EIGEN3_INCLUDE_DIRS}
    ${PCL_INCLUDE_DIRS}
)
add_definitions(${EIGEN3_DEFINITIONS})

catkin_package(
    INCLUDE_DIRS include
    LIBRARIES clear_inner_costmap
    CATKIN_DEPENDS
        roscpp
        pluginlib
        nav_core
)

add_library(${PROJECT_NAME} src/clear_inner_costmap.cpp)
add_dependencies(${PROJECT_NAME} geometry_msgs_generate_messages_cpp)
target_link_libraries(${PROJECT_NAME}
    ${Boost_LIBRARIES}
    ${catkin_LIBRARIES}
    )

## Install project namespaced headers
install(DIRECTORY include/${PROJECT_NAME}/
    DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
    FILES_MATCHING PATTERN "*.h"
    PATTERN ".svn" EXCLUDE)

install(TARGETS clear_inner_costmap
       ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
       LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
       )

install(FILES recovery_plugin.xml
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)


