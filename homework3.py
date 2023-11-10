# *Задание 1.
# Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет,
# является ли переданное число четным или нечетным. (код приложен в презентации)

# Задание 2.
# Разработайте и протестируйте метод numberInInterval, который проверяет,
# попадает ли переданное число в интервал (25;100). (код приложен в презентации)

import pytest


def even_odd_number(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False


@pytest.mark.parametrize("number", [2, 4, 6, 8, 10])
def test_even_number(number):
    assert even_odd_number(number)


@pytest.mark.parametrize("number", [1, 3, 5, 7, 9])
def test_odd_number(number):
    assert not even_odd_number(number)


def number_in_interval(n: int) -> bool:
    if 25 < n < 99:
        return True
    else:
        return False


@pytest.mark.parametrize("number", [i for i in range(26, 99)])
def test_number_in_interval(number):
    assert number_in_interval(number)


@pytest.mark.parametrize("number", [i for i in range(0, 26)])
def test_number_not_in_interval(number):
    assert not number_in_interval(number)


@pytest.mark.parametrize("number", [i for i in range(99, 200)])
def test_number_not_in_interval_large(number):
    assert not number_in_interval(number)
