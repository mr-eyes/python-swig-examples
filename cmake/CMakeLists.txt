cmake_minimum_required(VERSION 3.10)

find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})

find_package(PythonInterp REQUIRED)

message (STATUS "Using this Python interpreter: " ${PYTHON_EXECUTABLE})

find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_PATH})

