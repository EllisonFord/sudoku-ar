cmake_minimum_required(VERSION 3.10)
project(testing_ground)

#find_package( OpenCV REQUIRED )

set(CMAKE_CXX_STANDARD 17)

add_executable(testing_ground main.cpp)


target_link_libraries( testing_ground ${OpenCV_LIBS} )