#!/usr/bin/env python3
import rospy 
from simpleCode.srv import geo, geoResponse

def geo_position(request):
    pos = '(' + str(request.x) + ' ,' + str(request.y) + ')'
    rospy.loginfo(f'{pos} --  x = {request.x} et y = {request.y}')
    return geoResponse(pos, request.x, request.y)

if __name__ == '__main__':
    rospy.init_node('geo_node_server')
    service = rospy.Service('geo_service', geo,handler=geo_position)
    rospy.spin()