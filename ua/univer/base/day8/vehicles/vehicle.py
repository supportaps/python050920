import abc
from abc import ABC
from datetime import date


class Vehicle(ABC):
    def __init__(self,name, point, price, speed, year):
        self.name = name
        self.point = point
        self.price = price
        self.speed = speed
        self.year = year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if 1950<value<=date.today().year:
            self.__year = value
        else:
            self.__year = 0

    @abc.abstractmethod
    def display(self):
        pass

    def __str__(self):
        return f"{self.name}, {self.point}, {self.price}, {self.speed}, {self.year}"