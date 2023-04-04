import rospy

import tf_conversions
from src.utils import init_logger

import tf2_ros
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
import turtlesim.msg


def handle_turtle_pos(msg, turtlename):
    br = TransformBroadcaster()
    t = TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = turtlename
    t.transform.translation.x = msg.x
    t.transform.translation.y = msg.y
    t.transform.translation.z = 0.0
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    br.sendTransform(t)


if __name__ == '__main__':
    rospy.init_node('tf2_turtle_broadcaster')
    turtlename = "turtle2"
    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,
                     handle_turtle_pos,
                     turtlename)
    rospy.spin()
