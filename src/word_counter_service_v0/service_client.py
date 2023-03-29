import rospy
from utils import init_logger

from ros_book_samples.srv import WordCount, WordCountResponse

if __name__ == '__main__':
    rospy.init_node('client_words_service')
    rospy.wait_for_service('word_count')

    word_counter = rospy.ServiceProxy('word_count', WordCount)

    resp: WordCountResponse = word_counter('hello bro where are you')
    print(resp)
