cmake_minimum_required(VERSION 3.1)
project(PDS)

set(CMAKE_CXX_STANDARD 17)
SET(CMAKE_CXX_FLAGS_DEBUG  "-O3 -g -DNO_DEFAULT_MAPPING")
SET(CMAKE_CXX_FLAGS_RELEASE  "-O3 -g -DNO_DEFAULT_MAPPING")
SET(CMAKE_CXX_FLAGS -pthread)


add_executable(PDS utilities.h utilities.cpp utimer.cpp knn_sequential.cpp knn_parallel.cpp knn_ff.cpp)
