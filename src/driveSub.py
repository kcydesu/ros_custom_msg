#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    # This is where we implement the code to control the servos
    rospy.loginfo(rospy.get_caller_id() + "Steering: %d, Speed: %d", data.steering, data.speed)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('driver', anonymous=True)

    rospy.Subscriber("driving_controls", Drive, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
