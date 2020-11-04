

from ua.univer.base.day8.vehicles.vehicle import Vehicle
from ua.univer.base.day8.vehicles.vehicle_able_interface import *


class BatMobile(Vehicle, MoveAble, SwimAble, FlyAble):

    def __init__(self, name, point, price, speed, year):
        super().__init__(name, point, price, speed, year)

    def display(self):
        print("BatMobile",self.__str__())

    def move(self):
        return self.speed

    def swim(self):
        return self.speed/2

    def fly(self):
        return self.speed*2

