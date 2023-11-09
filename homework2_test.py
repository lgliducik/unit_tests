# Домашнее задание к семинару №2 JUnit:
# 1. Настроить новый проект:
#  a). Нужно создать новый проект, со следующей структурой классов (3 отдельных класса):
#  b). Настроить тестовую среду
#      (создать тестовый класс VehicleTest, пометить папку как Test sources (зеленая папка),
#      импортировать необходимые для тестов библиотеки (JUnit, assertJ - все что было на семинаре))
#  c). Написать следующие тесты:
#      - проверка того, что экземпляр объекта Car также является экземпляром транспортного средства; (instanceof)
#      - проверка того, объект Car создается с 4-мя колесами
#      - проверка того, объект Motorcycle создается с 2-мя колесами
#      - проверка того, объект Car развивает скорость 60 в режиме тестового вождения (testDrive())
#      - проверка того, объект Motorcycle развивает скорость 75 в режиме тестового вождения (testDrive())
#      - проверить, что в режиме парковки (сначала testDrive, потом park, т.е эмуляция движения транспорта)
#      машина останавливается (speed = 0)
#      - проверить, что в режиме парковки (сначала testDrive, потом park  т.е эмуляция движения транспорта)
#      мотоцикл останавливается (speed = 0)

from homework2 import *


class TestVehicle:
    @staticmethod
    def test_car():
        car = Car("shcoda", "carog", 2020)
        assert isinstance(car, Vehicle)
        assert car.get_num_wheels() == 4
        car.test_drive()
        assert car.speed == 60

    @staticmethod
    def test_motorcycle():
        motorcycle = Motorcycle("иж-1", "иж", 2020)
        assert isinstance(motorcycle, Vehicle)
        assert motorcycle.get_num_wheels() == 2
        motorcycle.test_drive()
        assert motorcycle.speed == 75

    @staticmethod
    def test_emulation_car():
        car = Car("shcoda", "carog", 2020)
        car.test_drive()
        car.park()
        assert car.speed == 0

    @staticmethod
    def test_emulation_motorcycle():
        motorcycle = Motorcycle("иж-1", "иж", 2020)
        motorcycle.test_drive()
        motorcycle.park()
        assert motorcycle.speed == 0
