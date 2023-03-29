import rospy

from ros_book_samples.srv import WordCountV2, WordCountV2Request, WordCountV2Response
from utils import init_logger


if __name__ == '__main__':
    rospy.init_node('v2WordCounterClient')
    rospy.wait_for_service('v2_word_counter')
    cc = rospy.ServiceProxy('v2_word_counter', WordCountV2)
    res: WordCountV2Response = cc("1", 10)
    print(res)
    # rospy.spin()
