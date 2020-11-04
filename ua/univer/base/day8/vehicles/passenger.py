from ua.univer.base.day8.vehicles.vehicle import Vehicle


class Passenger():
    def __init__(self, passenger):
        self.passenger = passenger

    @property
    def passenger(self):
        return self.__passenger

    @passenger.setter
    def passenger(self, value):
        if value > 0:
            self.__passenger = value
        else:
            print("Error value")

    def __str__(self):
        return f"{self.passenger}"