# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

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
CMAKE_SOURCE_DIR = /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/build

# Include any dependencies generated for this target.
include CMakeFiles/MQF.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/MQF.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/MQF.dir/flags.make

CMakeFiles/MQF.dir/src/gqf.cpp.o: CMakeFiles/MQF.dir/flags.make
CMakeFiles/MQF.dir/src/gqf.cpp.o: ../src/gqf.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/MQF.dir/src/gqf.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MQF.dir/src/gqf.cpp.o -c /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/src/gqf.cpp

CMakeFiles/MQF.dir/src/gqf.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MQF.dir/src/gqf.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/src/gqf.cpp > CMakeFiles/MQF.dir/src/gqf.cpp.i

CMakeFiles/MQF.dir/src/gqf.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MQF.dir/src/gqf.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/src/gqf.cpp -o CMakeFiles/MQF.dir/src/gqf.cpp.s

CMakeFiles/MQF.dir/src/gqf.cpp.o.requires:

.PHONY : CMakeFiles/MQF.dir/src/gqf.cpp.o.requires

CMakeFiles/MQF.dir/src/gqf.cpp.o.provides: CMakeFiles/MQF.dir/src/gqf.cpp.o.requires
	$(MAKE) -f CMakeFiles/MQF.dir/build.make CMakeFiles/MQF.dir/src/gqf.cpp.o.provides.build
.PHONY : CMakeFiles/MQF.dir/src/gqf.cpp.o.provides

CMakeFiles/MQF.dir/src/gqf.cpp.o.provides.build: CMakeFiles/MQF.dir/src/gqf.cpp.o


CMakeFiles/MQF.dir/src/utils.cpp.o: CMakeFiles/MQF.dir/flags.make
CMakeFiles/MQF.dir/src/utils.cpp.o: ../src/utils.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/MQF.dir/src/utils.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MQF.dir/src/utils.cpp.o -c /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/src/utils.cpp

CMakeFiles/MQF.dir/src/utils.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MQF.dir/src/utils.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/src/utils.cpp > CMakeFiles/MQF.dir/src/utils.cpp.i

CMakeFiles/MQF.dir/src/utils.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MQF.dir/src/utils.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/src/utils.cpp -o CMakeFiles/MQF.dir/src/utils.cpp.s

CMakeFiles/MQF.dir/src/utils.cpp.o.requires:

.PHONY : CMakeFiles/MQF.dir/src/utils.cpp.o.requires

CMakeFiles/MQF.dir/src/utils.cpp.o.provides: CMakeFiles/MQF.dir/src/utils.cpp.o.requires
	$(MAKE) -f CMakeFiles/MQF.dir/build.make CMakeFiles/MQF.dir/src/utils.cpp.o.provides.build
.PHONY : CMakeFiles/MQF.dir/src/utils.cpp.o.provides

CMakeFiles/MQF.dir/src/utils.cpp.o.provides.build: CMakeFiles/MQF.dir/src/utils.cpp.o


# Object files for target MQF
MQF_OBJECTS = \
"CMakeFiles/MQF.dir/src/gqf.cpp.o" \
"CMakeFiles/MQF.dir/src/utils.cpp.o"

# External object files for target MQF
MQF_EXTERNAL_OBJECTS =

libMQF.a: CMakeFiles/MQF.dir/src/gqf.cpp.o
libMQF.a: CMakeFiles/MQF.dir/src/utils.cpp.o
libMQF.a: CMakeFiles/MQF.dir/build.make
libMQF.a: CMakeFiles/MQF.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX static library libMQF.a"
	$(CMAKE_COMMAND) -P CMakeFiles/MQF.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/MQF.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/MQF.dir/build: libMQF.a

.PHONY : CMakeFiles/MQF.dir/build

CMakeFiles/MQF.dir/requires: CMakeFiles/MQF.dir/src/gqf.cpp.o.requires
CMakeFiles/MQF.dir/requires: CMakeFiles/MQF.dir/src/utils.cpp.o.requires

.PHONY : CMakeFiles/MQF.dir/requires

CMakeFiles/MQF.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/MQF.dir/cmake_clean.cmake
.PHONY : CMakeFiles/MQF.dir/clean

CMakeFiles/MQF.dir/depend:
	cd /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/build /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/build /home/mabuelanin/Desktop/SWIG/practice/use_shared/MQF/build/CMakeFiles/MQF.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/MQF.dir/depend

