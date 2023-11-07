# Задание 1. ** В классе Calculator создайте метод calculateDiscount,
# который принимает сумму покупки и процент скидки и возвращает сумму с учетом скидки.
# Ваша задача - проверить этот метод с использованием библиотеки AssertJ.
# Если метод calculateDiscount получает недопустимые аргументы,
# он должен выбрасывать исключение ArithmeticException.
# Не забудьте написать тесты для проверки этого поведения.


# Мы хотим улучшить функциональность нашего интернет-магазина.
# Ваша задача - добавить два новых метода в класс Shop:
# Метод sortProductsByPrice(), который сортирует список продуктов по стоимости.
# Метод getMostExpensiveProduct(), который возвращает самый дорогой продукт.
# Напишите тесты, чтобы проверить, что магазин хранит верный список продуктов
# (правильное количество продуктов, верное содержимое корзины).
# Напишите тесты для проверки корректности работы метода getMostExpensiveProduct.
# Напишите тесты для проверки корректности работы метода sortProductsByPrice
# (проверьте правильность сортировки). Используйте класс Product для создания экземпляров
# продуктов и класс Shop для написания методов сортировки и тестов.

import pytest


class WrongArgumentException(Exception):
    pass


class Calculator:
    @staticmethod
    def calculate_discount(price, discount):
        if price <= 0 or discount <= 0:
            raise WrongArgumentException()
        result = (price * discount)/100
        return result


def test_calculator():
    assert Calculator.calculate_discount(100, 20) == 20.0


def test_wrong_arguments():
    with pytest.raises(WrongArgumentException):
        Calculator.calculate_discount(-10, 20)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product({self.name}, {self.price})"

    def __repr__(self):
        return str(self)


class Shop:
    @staticmethod
    def sort_products_by_price(input_products: list):
        return sorted(input_products, key=lambda p: p.price)

    @staticmethod
    def get_most_expensive_product(input_products: list):
        return max(input_products, key=lambda p: p.price)


def test_get_most_expensive_product():
    products = [
        Product('prod1', 10),
        Product('prod2', 100),
        Product('prod3', 20),
    ]
    assert Shop.get_most_expensive_product(products).name == 'prod2'


def test_get_most_expensive_product_from_empty_list():
    products = []
    with pytest.raises(ValueError):
        Shop.get_most_expensive_product(products)


def test_get_most_expensive_product_double_product():
    products = [
        Product('prod1', 10),
        Product('prod2', 100),
        Product('prod3', 20),
    ]
    assert Shop.get_most_expensive_product(products).name == 'prod2'


def test_sort_products_by_price():
    products = [
        Product('prod1', 10),
        Product('prod2', 100),
        Product('prod3', 20),
    ]
    assert Shop.sort_products_by_price(products) == [products[0], products[2], products[1]]


def test_sort_empty_products():
    products = []
    assert Shop.sort_products_by_price(products) == []
