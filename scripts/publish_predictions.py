#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from std_msgs.msg import UInt8

pub = rospy.Publisher('nn_predictions', UInt8, queue_size=81)

def predict(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard something" + data.data)
    
    # rospy.get_time()
    prediction = 5
    pub.publish(prediction)
    
    rate = rospy.Rate(10) # 10hz    
    rate.sleep()
    

def start_node():

    rospy.init_node('predictions_node', anonymous=True)

    # SUBSCRIBE TO THE IMAGES
#    rospy.Subscriber('vision_node', Image, predict) # TEMP STRING
    rospy.Subscriber('chatter', String, predict) # TEMP STRING

    print("Got here")

    rospy.spin()


if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
