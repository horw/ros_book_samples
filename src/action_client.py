#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import rospy
import actionlib
import sys

# Подключение классов DoDishesAction и DoDishesGoal из пакета ros_book_samples
from ros_book_samples.msg import DoDishesAction, DoDishesGoal

# Функция для обрабоки сигнала Обратной связи (Action Feadback)
def action_feedback(fb):
    print(fb)

# Функция клиента
def action_client():
    # Создаем клиента для работы с Действиями с именем do_dishes
    client = actionlib.SimpleActionClient('do_dishes', DoDishesAction)

    # Ожидание подключение к серверу
    client.wait_for_server()

    # Создание задачи на 10 тарелок
    goal = DoDishesGoal(dishes=10)

    # Отправка задачи на сервер и определение метода обработки для Обратной связи (Action Feadback)
    client.send_goal(goal, feedback_cb=action_feedback)

    # Ожидание результата (Action Result) работы сервера
    client.wait_for_result()

    # Возвращаем полученный от сервера результат
    return client.get_result()

if __name__ == '__main__':
    try:
        # Инициализация ноды и запуск SimpleActionClient
        rospy.init_node('book_action_client_py')
        result = action_client()
        print("Result:", result)
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
