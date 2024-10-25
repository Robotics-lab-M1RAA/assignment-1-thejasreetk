#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def call_back(msg):
    rospy.loginfo(msg.data)

def node2():
    rospy.init_node("M1RAA 2024",anonymous=True)
    rate = rospy.Rate(10)

    rospy.Subscriber("hello_class",String,callback=call_back)

    publisher1 = rospy.Publisher("welcome",String,queue_size=10)
    publisher2 = rospy.Publisher("hello_college",String,queue_size=10)

    msg1 = String()
    msg2 = String()

    msg1.data = "Hello THEJASREE Welcome!"
    msg2.data = "Hello CET!"

    while not rospy.is_shutdown():
        publisher1.publish(msg1)
        rospy.loginfo(msg1.data)

        publisher2.publish(msg2)
        rospy.loginfo(msg2.data)
        rate.sleep()


if __name__ == "__main__" :
    try:
        node2()
    except rospy.ROSInterruptException:
        pass