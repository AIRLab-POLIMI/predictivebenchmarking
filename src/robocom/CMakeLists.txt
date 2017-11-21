cmake_minimum_required(VERSION 2.8.3)
project(robocom)

find_package(catkin REQUIRED COMPONENTS roscpp
					sensor_msgs
					robocom_msgs
					tf)

catkin_package()

include_directories(include ${catkin_INCLUDE_DIRS})

###########
## Build ##
###########
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
add_library(robocom src/Odometry.cpp
                    src/EuleroOdometry.cpp

 		    src/RungeKutta4Odometry.cpp
		    src/PathPublisher.cpp)

add_executable(odometry src/OdometryNode.cpp)
add_executable(path src/PathNode.cpp)

target_link_libraries(odometry robocom ${catkin_LIBRARIES})
target_link_libraries(path robocom ${catkin_LIBRARIES})

add_dependencies(odometry ${catkin_EXPORTED_TARGETS})
add_dependencies(path ${catkin_EXPORTED_TARGETS})

#############
## Install ##
#############
 
install(TARGETS robocom odometry path
	ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )
