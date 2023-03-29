import rospy
from std_msgs.msg import Int32
from utils import init_logger
rospy.init_node('double')


def callback(msg):
    doubled = Int32()
    doubled.data = msg.data * 2
    pub.publish(doubled)


sub = rospy.Subscriber('number', Int32, callback=callback)
pub = rospy.Publisher('doubled', Int32, queue_size=10)
rospy.spin()