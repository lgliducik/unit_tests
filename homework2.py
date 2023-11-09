import pytest
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
