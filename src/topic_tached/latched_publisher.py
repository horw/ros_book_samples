import rospy
from nav_msgs.msg import OccupancyGrid


def init():
    rospy.init_node('latched_publisher')
    publisher = rospy.Publisher('someLatchedChannel', OccupancyGrid, latch=True)
    rate = rospy.Rate(2)
    publisher.publish()
    rate.sleep()

# didn't complete
