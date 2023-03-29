import rospy

from ros_book_samples.srv import WordCountV2, WordCountV2Request, WordCountV2Response
from utils import init_logger


def processor(req: WordCountV2Request):
    words = req.words
    min_len = req.min_word_len
    words_len = len(words)
    if words_len > min_len:
        return WordCountV2Response(
            words_len, 0
            # **{
            #     "count": words_len,
            #     "ignored": 0
            # }
        )
    else:
        return WordCountV2Response(
            0, words_len
            #            **{
            #     "count": 0,
            #     "ignored": words_len
            # }
        )


if __name__ == '__main__':
    rospy.init_node('v2WordCounter')
    rospy.Service('v2_word_counter', WordCountV2, processor)
    rospy.spin()
