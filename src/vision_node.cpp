// SYSTEM
#include <iostream>
// ROS
#include <ros/ros.h>
#include <image_transport/image_transport.h> // THIS IS TOO MUCH?
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>
#include <std_msgs/UInt8.h>
// CUSTOM
#include "solve_puzzle.cpp"
using namespace std;
using namespace cv;


void Callback(const std_msgs::UInt8& msg)
{
    cout << "Predicted: " << msg << endl;
}


int main(int argc, char** argv)
{
  ros::init(argc, argv, "vision_node");

  ros::NodeHandle nh;

  image_transport::ImageTransport it(nh);

  auto pub = it.advertise("camera/image", 1);

  auto image = cv::imread("/home/master/catkin_ws/src/sudoku_ar/extracted_numbers/only_nums/12.png", CV_LOAD_IMAGE_COLOR);

  //cv::waitKey(30);

  auto msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", image).toImageMsg();

  ros::Rate loop_rate(10); //


  while (nh.ok()) {

    pub.publish(msg);

    auto sub = nh.subscribe("nn_predictions", 1, Callback);

    cout << "Subscription is done." << endl;

    ros::spinOnce();

    loop_rate.sleep();
  }
}
