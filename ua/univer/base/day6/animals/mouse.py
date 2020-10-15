from datetime import date


class Mouse:
    def __init__(self, name, weight):
        self.__weight = weight
        self.__name = name
        self.__killer = None
        self.__date_of_kill = None

    def set_killer(self, cat):
        self.__killer = cat
        self.__date_of_kill = date.today()

    def set_weight(self, food_weight):
        if food_weight < 3:
            self.__weight += food_weight
        else:
            print("Error weight")

    def get_weight(self):
        return self.__weight

    def get_name(self):
        return self.__name

    def show(self):
        if(self.get_weight()!=0):
            print("Mouse ", self.get_name(), ": ", self.get_weight() )
        else:
            print("Mouse ", self.get_name(),"....RIP....",self.__killer.get_name(),"...",self.__date_of_kill)