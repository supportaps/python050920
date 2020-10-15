from datetime import date


class Cat:
    def __init__(self, name="Anonim", year=0, weight=0):
        self.__weight = weight
        self.__year = year
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return  date.today().year - self.__year

    def eat_mouse(self,mouse):
        self.set_weight(mouse.get_weight())
        mouse.set_weight(-mouse.get_weight())
        mouse.set_killer(self)

    def set_weight(self, value):
        if 0 < value < 20:
            self.__weight += value
        else:
            print("Error value of weight")

    def get_weight(self):
        return self.__weight;

    def show(self):
        print(self.get_name(), " : ", self.get_age(), " : ", self.get_weight())
