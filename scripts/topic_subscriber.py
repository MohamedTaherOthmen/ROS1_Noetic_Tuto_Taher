#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callBack(msg):
	print(msg.data)

if __name__ == '__main__' :
	rospy.init_node('topic_subscriber')
	sub = rospy.Subscriber('counter', Int32, callback=callBack)
	rospy.spin()
