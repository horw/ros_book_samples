import rospy

from ros_book_samples.msg import Complex
from random import random
from utils import init_logger

def callback(msg: Complex):
    print("Real: ", msg.real)
    print("Imaginary: ", msg.imaginary)


if __name__ == '__main__':
    rospy.init_node('complex_processor_node')
    pub = rospy.Subscriber('complex', Complex, callback)
    rospy.spin()
