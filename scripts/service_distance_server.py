#!/usr/bin/env python3
import rospy 
import math
from simpleCode.srv import distance, distanceResponse

def distance_calcull(request):
    distance = math.sqrt(pow(request.x1 + request.x1, 2)+pow(request.x2 + request.y2, 2))
    rospy.loginfo(f'The Distance between A({request.x1},{request.y1}) and B({request.x2},{request.y2}) = {distance}')
    return distanceResponse(distance)


if __name__ == '__main__' :
    rospy.init_node('distance_server')
    server = rospy.Service('distance_service', distance, handler=distance_calcul)

    rospy.spin()