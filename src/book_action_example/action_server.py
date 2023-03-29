#! /usr/bin/env python
# -*- coding: utf-8 -*-

import roslib
import rospy
import actionlib

from ros_book_samples.msg import DoDishesAction, DoDishesResult, DoDishesFeedback

class DoDishesServer:
    # Определяем обьекты Обратная связь и Результат
    _feedback = DoDishesFeedback()
    _result = DoDishesResult()

    def __init__(self):
        # Создаем и запускаем SimpleActionServer для обработки запросов
        self.server = actionlib.SimpleActionServer('do_dishes', DoDishesAction, self.execute, False)
        self.server.start()

    def execute(self, goal):
        # Определяем внутренние переменные каждого запроса
        r = rospy.Rate(1) # эмулируем задержку в 1 секунду на выполнение
        self.clear_dishes = 0

        # Моем каждую тарелку
        for i in range(1, goal.dishes+1):
            self.server.publish_feedback(DoDishesFeedback(i))
            self.clear_dishes+=1
            r.sleep()
        # После запуршения отправляем сообщение о завержении
        self.server.set_succeeded(DoDishesResult(self.clear_dishes))


if __name__ == '__main__':
    rospy.init_node('do_dishes_server')
    server = DoDishesServer()
    rospy.spin()
