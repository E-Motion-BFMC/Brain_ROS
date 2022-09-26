#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import ringbuffer

class steeringNODE:
    def __init__(self):

        # In ROS, nodes are uniquely named. If two nodes with the same
        # name are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node('steeringNODE', anonymous=True)

        self._videoData = ringbuffer.ringbuffer(6)
        self.IMUData = ringbuffer.ringbuffer(6)
        #rospy.Subscriber("chatter", String, callback)

        rospy.spin()


    def _visualCallback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    def _IMUCallback(self, data):
        pass


if __name__ == '__main__':
    node = steeringNODE()
