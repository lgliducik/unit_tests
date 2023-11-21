# Задание 1. Создайте программу на Python или Java,
# которая принимает два списка чисел и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.
"""This module for compare coverage"""


class CompareAverage:
    """
    A class CompareAverage solve average from 2 list and compare it.

    ...

    Methods
    -------
    find_average(input_list):
        find average in input_list.
    compare(input_list1, input_list2):
        compare average from 2 lists.
    """

    @staticmethod
    def find_average(list1: list) -> float:
        """
        find average in input_list.
        :param list1:
        :return average(float):
        """
        if not isinstance(list1, list):
            raise TypeError("input object is not a list")
        if not list1:
            return 0
        result = 0
        for item in list1:
            result += item
        return result/len(list1)

    @staticmethod
    def compare(list1: list, list2: list):
        """

        compare average from 2 lists.

        :param list1:
        :param list2:
        :return string:
        """
        middle1 = CompareAverage.find_average(list1)
        middle2 = CompareAverage.find_average(list2)
        result_str = ""
        if middle1 > middle2:
            result_str = "Первый список имеет большее среднее значение"
        if middle2 > middle1:
            result_str = "Второй список имеет большее среднее значение"
        if middle1 == middle2:
            result_str = "Средние значения равны"
        return result_str
