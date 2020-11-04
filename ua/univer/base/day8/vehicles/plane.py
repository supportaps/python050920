from ua.univer.base.day8.vehicles.passenger import Passenger
from ua.univer.base.day8.vehicles.vehicle import Vehicle


class Plane(Vehicle, Passenger):
    def __init__(self,name, point, price, speed, year, passenger, height):
        super().__init__(name,point,price,speed,year)
        Passenger.__init__(self,passenger)
        self.height = height

    def display(self):
        print("Plane",self.__str__())

    def __str__(self):
        return f"{super().__str__()}, {Passenger.__str__(self)}, {self.height}"