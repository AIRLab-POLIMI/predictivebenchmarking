# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ros/slampbenchmarking/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ros/slampbenchmarking/build

# Include any dependencies generated for this target.
include navigation/map_server/CMakeFiles/map_server_utest.dir/depend.make

# Include the progress variables for this target.
include navigation/map_server/CMakeFiles/map_server_utest.dir/progress.make

# Include the compile flags for this target's objects.
include navigation/map_server/CMakeFiles/map_server_utest.dir/flags.make

navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o: navigation/map_server/CMakeFiles/map_server_utest.dir/flags.make
navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o: /home/ros/slampbenchmarking/src/navigation/map_server/test/utest.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ros/slampbenchmarking/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o"
	cd /home/ros/slampbenchmarking/build/navigation/map_server && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/map_server_utest.dir/test/utest.cpp.o -c /home/ros/slampbenchmarking/src/navigation/map_server/test/utest.cpp

navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/map_server_utest.dir/test/utest.cpp.i"
	cd /home/ros/slampbenchmarking/build/navigation/map_server && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ros/slampbenchmarking/src/navigation/map_server/test/utest.cpp > CMakeFiles/map_server_utest.dir/test/utest.cpp.i

navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/map_server_utest.dir/test/utest.cpp.s"
	cd /home/ros/slampbenchmarking/build/navigation/map_server && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ros/slampbenchmarking/src/navigation/map_server/test/utest.cpp -o CMakeFiles/map_server_utest.dir/test/utest.cpp.s

navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o.requires:

.PHONY : navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o.requires

navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o.provides: navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o.requires
	$(MAKE) -f navigation/map_server/CMakeFiles/map_server_utest.dir/build.make navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o.provides.build
.PHONY : navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o.provides

navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o.provides.build: navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o


navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o: navigation/map_server/CMakeFiles/map_server_utest.dir/flags.make
navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o: /home/ros/slampbenchmarking/src/navigation/map_server/test/test_constants.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ros/slampbenchmarking/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o"
	cd /home/ros/slampbenchmarking/build/navigation/map_server && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o -c /home/ros/slampbenchmarking/src/navigation/map_server/test/test_constants.cpp

navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/map_server_utest.dir/test/test_constants.cpp.i"
	cd /home/ros/slampbenchmarking/build/navigation/map_server && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ros/slampbenchmarking/src/navigation/map_server/test/test_constants.cpp > CMakeFiles/map_server_utest.dir/test/test_constants.cpp.i

navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/map_server_utest.dir/test/test_constants.cpp.s"
	cd /home/ros/slampbenchmarking/build/navigation/map_server && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ros/slampbenchmarking/src/navigation/map_server/test/test_constants.cpp -o CMakeFiles/map_server_utest.dir/test/test_constants.cpp.s

navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o.requires:

.PHONY : navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o.requires

navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o.provides: navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o.requires
	$(MAKE) -f navigation/map_server/CMakeFiles/map_server_utest.dir/build.make navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o.provides.build
.PHONY : navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o.provides

navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o.provides.build: navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o


# Object files for target map_server_utest
map_server_utest_OBJECTS = \
"CMakeFiles/map_server_utest.dir/test/utest.cpp.o" \
"CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o"

# External object files for target map_server_utest
map_server_utest_EXTERNAL_OBJECTS =

/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: navigation/map_server/CMakeFiles/map_server_utest.dir/build.make
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: gtest/libgtest.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /home/ros/slampbenchmarking/devel/lib/libmap_server_image_loader.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libSDLmain.a
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libSDL.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libSDL_image.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/libtf.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/libtf2_ros.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/libactionlib.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/libmessage_filters.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/libroscpp.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/libtf2.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/librosconsole.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/librostime.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /opt/ros/kinetic/lib/libcpp_common.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libSDLmain.a
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libSDL.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: /usr/lib/x86_64-linux-gnu/libSDL_image.so
/home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest: navigation/map_server/CMakeFiles/map_server_utest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ros/slampbenchmarking/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable /home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest"
	cd /home/ros/slampbenchmarking/build/navigation/map_server && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/map_server_utest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
navigation/map_server/CMakeFiles/map_server_utest.dir/build: /home/ros/slampbenchmarking/devel/lib/map_server/map_server_utest

.PHONY : navigation/map_server/CMakeFiles/map_server_utest.dir/build

navigation/map_server/CMakeFiles/map_server_utest.dir/requires: navigation/map_server/CMakeFiles/map_server_utest.dir/test/utest.cpp.o.requires
navigation/map_server/CMakeFiles/map_server_utest.dir/requires: navigation/map_server/CMakeFiles/map_server_utest.dir/test/test_constants.cpp.o.requires

.PHONY : navigation/map_server/CMakeFiles/map_server_utest.dir/requires

navigation/map_server/CMakeFiles/map_server_utest.dir/clean:
	cd /home/ros/slampbenchmarking/build/navigation/map_server && $(CMAKE_COMMAND) -P CMakeFiles/map_server_utest.dir/cmake_clean.cmake
.PHONY : navigation/map_server/CMakeFiles/map_server_utest.dir/clean

navigation/map_server/CMakeFiles/map_server_utest.dir/depend:
	cd /home/ros/slampbenchmarking/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ros/slampbenchmarking/src /home/ros/slampbenchmarking/src/navigation/map_server /home/ros/slampbenchmarking/build /home/ros/slampbenchmarking/build/navigation/map_server /home/ros/slampbenchmarking/build/navigation/map_server/CMakeFiles/map_server_utest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : navigation/map_server/CMakeFiles/map_server_utest.dir/depend

