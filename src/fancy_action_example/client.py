import rospy
import time
from src.utils import init_logger

import actionlib
from ros_book_samples.msg import TimerAction, TimerGoal, TimerResult, TimerFeedback


def feedback_cb(feedback: TimerFeedback):
    print('[Feedback] Time elapsed: %f' % (feedback.time_elapsed.to_sec()))
    print('[Feedback] Time remaining: %f' % (feedback.time_remaining.to_sec()))


rospy.init_node('timer_action_client_v2')
client = actionlib.SimpleActionClient('timer', TimerAction)
client.wait_for_server()
goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(500.0)
client.send_goal(goal, feedback_cb=feedback_cb)
# time.sleep(3)
# client.cancel_goal()
client.wait_for_result()
print('[Result] State: %d' % (client.get_state()))
print('[Result] Status: %s' % (client.get_goal_status_text()))
result: TimerResult = client.get_result()
print('[Result] Time elapsed: %f' % (result.time_elapsed.to_sec()))
print('[Result] Time elapsed: %d' % result.updates_sent)

