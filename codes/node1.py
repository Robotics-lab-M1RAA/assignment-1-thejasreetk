#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def call_back(msg):
    rospy.loginfo(msg.data)

def node1():
    rospy.init_node("THEJASREE")
    rospy.Subscriber("welcome",String,callback=call_back)
    publisher = rospy.Publisher("hello_class",String,queue_size=10)
    rate = rospy.Rate(10)
    msg = String()
    msg.data = "Hello RAA24_26!"
    while not rospy.is_shutdown():
        publisher.publish(msg)
        rospy.loginfo(msg.data)
        rate.sleep()

if __name__ == "__main__" :
    try:
        node1()
    except rospy.ROSInterruptException:
        pass