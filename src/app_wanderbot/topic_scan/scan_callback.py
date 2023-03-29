import rospy
from sensor_msgs.msg import LaserScan
from src.utils import init_logger


def callback(msg: LaserScan):
    range_ahead = msg.ranges[len(msg.ranges)//2]
    print("range ahead: %0.1f" % range_ahead)
    # print(msg)


rospy.init_node('scan_node')
sub = rospy.Subscriber('scan', LaserScan, callback=callback)

rospy.spin()
