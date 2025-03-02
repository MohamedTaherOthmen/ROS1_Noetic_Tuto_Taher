#!/usr/bin/env python3
import rospy
from simpleCode.msg import Complex

def complexDisplay(msg: Complex):
    rel = str(msg.real)
    img = str(msg.imaginary)
    print(img + "i + " + rel)

if __name__ == '__main__' :
    rospy.init_node("Complexe_Number_Subscriber")
    rospy.loginfo("Complexe Subscriber Node Started !")
    sub = rospy.Subscriber("Complexe", Complex, callback=complexDisplay)

    rospy.spin()

