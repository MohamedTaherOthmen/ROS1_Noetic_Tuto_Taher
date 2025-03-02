#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node('topic_latched_publisher')
    latched_pub = rospy.Publisher('counter', Int32, latched=True)
    latched_pub.pub(1234)

