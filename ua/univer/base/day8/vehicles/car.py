from ua.univer.base.day8.vehicles.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, name, point, price, speed, year):
        super().__init__(name, point, price, speed, year)

    def display(self):
        print("Ship",self.__str__())

    def __str__(self):
        return super().__str__()