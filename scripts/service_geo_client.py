#!/usr/bin/env python3
import rospy
import sys
from simpleCode.srv import geo, geoRequest

def get_pos_x_y(x, y):
    rospy.wait_for_service('geo_service')
    
    try:
        pos_generate = rospy.ServiceProxy('geo_service', geo)
        request = geoRequest()
        request.x = float(x)  
        request.y = float(y)  
        response = pos_generate(request)
        return response.pos
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

if __name__ == '__main__':
    rospy.init_node('geo_node_client') 
    
    if len(sys.argv) != 3:
        rospy.logerr("Usage: rosrun simpleCode geo_client_node.py x y")
        sys.exit(1)  
    x = sys.argv[1]
    y = sys.argv[2]
    
    pos = get_pos_x_y(x, y)

    rospy.loginfo(f'Position = {pos}')