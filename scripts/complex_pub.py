#!/usr/bin/env python3
import rospy
from simpleCode.msg import Complex

if __name__ == '__main__':
    rospy.init_node("Complexe_Number_Publicher")
    publisher = rospy.Publisher("Complexe", Complex, queue_size=10)
    rospy.loginfo("Complexe Publisher Node Started !")

    while not rospy.is_shutdown():
        rel = float(input("Please Enter Rel(n) = "))
        img = float(input("Please Enter Img(n) = "))
        complexe_number = Complex()
        complexe_number.real = rel
        complexe_number.imaginary = img
        publisher.publish(complexe_number)