class Car:

    def __init__(self):
        self.__year_model = 1990
        self.__make = 'BMW'
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5
        return self.__speed

    def breeak(self):
        self.__speed -= 5
        return self.__speed

    def get_speed(self):
        return self.__speed