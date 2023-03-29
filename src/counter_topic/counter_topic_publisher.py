import rospy
from std_msgs.msg import Int32
from utils import init_logger


rospy.init_node('name1')
pub = rospy.Publisher('counter', Int32, queue_size=10)

rate = rospy.Rate(2)
counter = 0


def run():
    global counter
    while not rospy.is_shutdown():
        pub.publish(counter)
        counter += 1
        rate.sleep()

if __name__ == '__main__':
    run()


