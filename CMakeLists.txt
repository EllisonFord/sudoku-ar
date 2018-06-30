cmake_minimum_required(VERSION 2.8.3)
project(sudoku_ar)

add_compile_options(-std=c++17)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  cv_bridge
  image_transport
  message_generation
)


## Generate added messages and services with any dependencies listed here
#generate_messages(
#  DEPENDENCIES
#  std_msgs
#)

catkin_package()


## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
include
  ${catkin_INCLUDE_DIRS}
)


add_executable(vision_node src/vision_node.cpp)
target_link_libraries(vision_node ${catkin_LIBRARIES})

add_executable(solve_puzzle src/solve_puzzle.cpp)

find_package(OpenCV REQUIRED)
target_link_libraries(vision_node ${OpenCV_LIBS})

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "/usr/local/lib/cmake")
