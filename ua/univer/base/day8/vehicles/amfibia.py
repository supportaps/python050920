from ua.univer.base.day8.vehicles.vehicle import Vehicle
from ua.univer.base.day8.vehicles.vehicle_able_interface import *

class Amfibia(Vehicle, MoveAble, SwimAble):

    def __init__(self, name, point, price, speed, year):
        super().__init__(name, point, price, speed, year)

    def display(self):
        print("Amfibia", self.__str__())

    def move(self):
        return self.speed

    def swim(self):
        return self.speed / 3

