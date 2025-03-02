#!/usr/bin/env python3 
import rospy
import sys
from simpleCode.srv import distance, distanceRequest

def distance_service(x1, y1, x2, y2):
    rospy.wait_for_service('distance_server')
    
    try: 
        client = rospy.ServiceProxy('distance_server', distance)
        coordinates = distanceRequest()
        coordinates.x1 = x1
        coordinates.y1 = y1 
        coordinates.x2 = x2
        coordinates.y2 = y2
        response = client(coordinates)
    except rospy.ServiceException as e:
        rospy.logwarn(e)
    
    return response.distance

if __name__ == '__main__':
    rospy.init_node('distance_server')
    
    if len(sys.argv) != 5:
        rospy.logerr("Usage: rosrun simpleCode distance_client.py x1 y1 x2 y2")
        sys.exit(1)
    
    x1 = sys.argv[1]
    y1 = sys.argv[2]
    x2 = sys.argv[3]
    y2 = sys.argv[4]

    distance = distance_service(x1, y1, x2, y2)

    rospy.loginfo(f'Distance between A and B = {distance}')