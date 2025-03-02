#!/usr/bin/env python3 
import rospy 
import sys
from simpleCode.srv import wordCount, wordCountRequest

def count_word_client(phrase):
    rospy.wait_for_service('count_word')
    try:
        count_word_service = rospy.ServiceProxy('count_word', wordCount)
        request = wordCountRequest()
        request.phrase = phrase 
        response = count_word_service(phrase)
        return response.count
    
    except rospy.ServiceException as e :
        rospy.logwarn(e)

if __name__ == '__main__':
    rospy.init_node('Service_Client_Node')
    
    if len(sys.argv) != 2:
        rospy.logerr("Usage : rosrun simpleCode client_node.py 'your phrase'")
        sys.exit(1)
    
    phrase = sys.argv[1]
    word_count = count_word_client(phrase)
    
    rospy.loginfo(f'phrase : {phrase}')
    rospy.loginfo(f'Word count : {word_count}')
