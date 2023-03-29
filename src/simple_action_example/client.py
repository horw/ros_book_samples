import time

import rospy

import actionlib
from ros_book_samples.msg import TimerAction, TimerGoal, TimerResult
from src.utils import init_logger


if __name__ == '__main__':
    rospy.init_node('timer_action_client')
    client = actionlib.SimpleActionClient('timer',
                                          TimerAction)
    client.wait_for_server()
    goal = TimerGoal()
    goal.time_to_wait = rospy.Duration.from_sec(5.0)
    client.send_goal(goal)
    client.wait_for_result()
    result: TimerResult = client.get_result()
    print('Time elapsed: %f' % result.time_elapsed.to_sec())
