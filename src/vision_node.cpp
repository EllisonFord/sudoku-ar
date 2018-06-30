#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>

using namespace cv;

/*
class SudokuROS
{
private:

public:

};
*/

ros::NodeHandle r;
ros::Publisher laser_scan_pub = r.advertise<sensor_msgs::LaserScan>("laser_scan", 81);

void Callback(const nxt_msgs::Range  &msg)
{
  sensor_msgs::LaserScan pub;
  laser_scan_pub.publish(pub);
}



int main(int argc, char** argv)
{
  ros::init(argc, argv, "vision_node");

  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("point_cloud", 81, Callback);

  ros::spin();

  /*
  image_transport::ImageTransport it(nh);

  auto pub = it.advertise("camera/image", 81);

  auto image = cv::imread(argv[1], CV_LOAD_IMAGE_COLOR);

  cv::waitKey(30);

  auto msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", image).toImageMsg();

  ros::Rate loop_rate(5);


  while (nh.ok()) {

    pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
  }
   */
}
