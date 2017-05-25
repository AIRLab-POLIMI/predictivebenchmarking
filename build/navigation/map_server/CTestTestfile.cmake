# CMake generated Testfile for 
# Source directory: /home/ros/slampbenchmarking/src/navigation/map_server
# Build directory: /home/ros/slampbenchmarking/build/navigation/map_server
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_map_server_gtest_map_server_utest "/home/ros/slampbenchmarking/build/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/ros/slampbenchmarking/build/test_results/map_server/gtest-map_server_utest.xml" "--return-code" "/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest --gtest_output=xml:/home/ros/slampbenchmarking/build/test_results/map_server/gtest-map_server_utest.xml")
add_test(_ctest_map_server_rostest_test_rtest.xml "/home/ros/slampbenchmarking/build/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/ros/slampbenchmarking/build/test_results/map_server/rostest-test_rtest.xml" "--return-code" "/opt/ros/kinetic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/ros/slampbenchmarking/src/navigation/map_server --package=map_server --results-filename test_rtest.xml --results-base-dir \"/home/ros/slampbenchmarking/build/test_results\" /home/ros/slampbenchmarking/src/navigation/map_server/test/rtest.xml ")
