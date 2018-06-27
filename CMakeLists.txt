cmake_minimum_required(VERSION 3.10)
project(sudoku_ar)

#find_package( OpenCV REQUIRED )

set(CMAKE_CXX_STANDARD 17)

add_executable(sudoku_ar main.cpp)


target_link_libraries( sudoku_ar ${OpenCV_LIBS} )