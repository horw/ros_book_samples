import rospy

from ros_book_samples.msg import Complex
from random import random

rospy.init_node('complex_sender_node')
pub = rospy.Publisher('complex', Complex, queue_size=10)

rate = rospy.Rate(2)
while not rospy.is_shutdown():
    msg = Complex()
    msg.real = random()
    msg.imaginary = random()

    pub.publish(msg)
    rate.sleep()

