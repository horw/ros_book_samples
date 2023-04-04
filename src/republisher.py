import rospy
from jsk_recognition_msgs.msg import BoundingBoxArray, BoundingBox
from utils import init_logger
from visualization_msgs.msg import MarkerArray, Marker

rospy.init_node('republisher123')


topic = 'visualization_marker_array'
publisher = rospy.Publisher(topic, MarkerArray)



# rate = rospy.Rate(10.0)
def callback(msg: BoundingBoxArray):

    markerArray = MarkerArray()
    for box in msg.boxes:
        # box
        marker = Marker()
        marker.header.frame_id = "map"
        marker.type = marker.CUBE
        marker.action = marker.ADD
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.pose.orientation.w = 2.0
        marker.pose.position.x = box.pose.position.x + 300
        marker.pose.position.y = box.pose.position.y + 150
        marker.pose.position.z = 1#box.pose.position.z

        markerArray.markers.append(marker)

    id = 1
    for m in markerArray.markers:
        m.id = id
        id += 1
    # publisher.publish(markerArray)
    # if counter == 1000:
    publisher.publish(markerArray)
    # print(msg)
    # rate.sleep()


subscriber = rospy.Subscriber('/x2v_bounding_boxs', BoundingBoxArray, callback=callback)
rospy.spin()
