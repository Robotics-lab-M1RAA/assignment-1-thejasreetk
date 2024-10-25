#!/usr/bin/python3
import rospy

from std_msgs.msg import String
def talker():
    rospy.init_node("thejasree_node1",anonymous=True)
    pub = rospy.Publisher("Greetings",String,queue_size=10)
    rate =rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = String()
        msg.data = "hello I'm THEJASREE T K"
        pub.publish(msg)
        rospy.loginfo(msg.data)
        rate.sleep()
if __name__=="__main__" :
    try:
        talker()
    except rospy.ROSInterruptException:
        pass 
