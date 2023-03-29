import rospy
from std_msgs.msg import Int32
from utils import init_logger


def callback(msg):
    rospy.loginfo(msg)

def run():
    rospy.init_node('counter_listener')
    sub = rospy.Subscriber('counter', Int32, callback)
    rospy.spin()


if __name__ == '__main__':
    run()