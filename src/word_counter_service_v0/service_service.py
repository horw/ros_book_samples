import rospy
from utils import init_logger

from ros_book_samples.srv import WordCount,\
    WordCountRequest, WordCountResponse


def count_words(request: WordCountRequest):
    return WordCountResponse(len(request.words.split()))


if __name__ == '__main__':
    rospy.init_node('word_count_server')
    publisher = rospy.Service('word_count', WordCount, count_words)
    rospy.spin()

