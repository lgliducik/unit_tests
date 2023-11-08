from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def test_drive(self):
        pass

    @abstractmethod
    def park(self):
        pass


class Motorcycle(Vehicle):

    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.yearRelease = year
        self.numWheels = 2
        self.speed = 0

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0

    def get_company(self):
        return self.company

    def get_model(self):
        return self.model

    def get_year_release(self):
        return self.yearRelease

    def get_num_wheels(self):
        return self.numWheels

    def get_speed(self):
        return self.speed

    def __str__(self):
        return "This motorcycle is a “ + year + “ “ + make + “ “ + model + “;"


class Car (Vehicle):
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.yearRelease = year
        self.numWheels = 4
        self.speed = 0

    def test_drive(self):
        self.speed = 60

    def park(self):
        self.speed = 0

    def get_company(self):
        return self.company

    def get_model(self):
        return self.model

    def get_year_release(self):
        return self.yearRelease

    def get_num_wheels(self):
        return self.numWheels

    def get_speed(self):
        return self.speed

    def __str__(self):
        return "This car is a “ + year + “ “ + make + “ “ + model + "


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

class VehicleTest:
    @staticmethod
    def test_car():
        car = Car("shcoda", "carog", 2020)
        assert isinstance(car, Vehicle) is True
        assert car.get_num_wheels() == 4
        car.test_drive()
        assert car.speed == 60

    @staticmethod
    def test_motorcycle():
        motorcycle = Motorcycle("иж-1", "иж", 2020)
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
