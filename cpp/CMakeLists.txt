cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project (cpp-files)

set(CMAKE_CXX_STANDARD 17)

add_executable(type type.cpp)
add_executable(b2e bin_to_edgelist.cpp)