#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from std_msgs.msg import UInt8
from use_cnn import predict

pub = rospy.Publisher('nn_predictions', UInt8, queue_size=81)

def publish_predictions(data):

    predictions = predict(input_imgs=None)

    predictions = 5 # TEMP PLACEHOLDER

    pub.publish(predictions)
    rate = rospy.Rate(10) # 10hz
    rate.sleep()
    

def start_node():
    rospy.init_node('predictions_node', anonymous=True)

#    rospy.Subscriber('vision_node', Image, predict) # TEMP STRING
    rospy.Subscriber('chatter', String, publish_predictions) # TEMP STRING

    print("Node successfully started.")

    rospy.spin()


if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass


"""
EXTRA CODE
rospy.loginfo(rospy.get_caller_id() + "I heard something" + data.data)
    rospy.get_time()


"""