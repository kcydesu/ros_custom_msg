#!/usr/bin/env python
# license removed for brevity
import rospy
from templecar.msg import Drive
import random

def talker():
    pub = rospy.Publisher('driving_controls', Drive, queue_size=10)
    rospy.init_node('drive_commands', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # Picks two random numbers in the range for our car
        steering = random.randint(12,23)
        speed = random.randint(12,23)
        
        # Creates a 'blank' Drive message and sets values
        msg = Drive()
        msg.steering = steering
        msg.speed = speed
        
        # Logs and publishes message
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
