#!/usr/bin/env python3 
import rospy 
from simpleCode.srv import wordCount, wordCountResponse

def count_words(request):
    rospy.loginfo(f'Phrase = {request.phrase}')
    return wordCountResponse(len(request.phrase.split()))

if __name__ == '__main__':
    rospy.init_node('Service_Server_Node')
    service = rospy.Service('count_word', wordCount, handler=count_words)
    rospy.spin()
