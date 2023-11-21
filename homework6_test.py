from homework6 import CompareAverage
import pytest


def test_compare():
    assert CompareAverage.compare([1, 2, 3], [1, 2, 3]) == "Средние значения равны"
    assert CompareAverage.compare([], []) == "Средние значения равны"
    assert CompareAverage.compare([4, 2, 3], [1, 2, 3]) == "Первый список имеет большее среднее значение"
    assert CompareAverage.compare([1, 2, 3], [4, 2, 3]) == "Второй список имеет большее среднее значение"


def test_compare_wrong_parameters():
    with pytest.raises(TypeError):
        CompareAverage.compare(1, [4, 2, 3])
    with pytest.raises(TypeError):
        CompareAverage.compare([4, 2, 3], 1)
