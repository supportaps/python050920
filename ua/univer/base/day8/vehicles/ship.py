from ua.univer.base.day8.vehicles.cargo import Cargo
from ua.univer.base.day8.vehicles.passenger import Passenger
from ua.univer.base.day8.vehicles.vehicle import Vehicle
from ua.univer.base.day8.vehicles.vehicle_able_interface import SwimAble


class Ship(Vehicle, Passenger, Cargo, SwimAble):
    def __init__(self, name, point, price, speed, year, passenger, port, cargo_weight):
        Vehicle.__init__(self,name, point, price, speed, year)
        Passenger.__init__(self,passenger)
        Cargo.__init__(self,cargo_weight)
        self.port = port

    def display(self):
        print("Ship",self.__str__())

    def swim(self):
        return self.speed

    def __str__(self):
        return f"{Vehicle.__str__(self)}, {Passenger.__str__(self)}, {self.port}, {Cargo.__str__(self)}"