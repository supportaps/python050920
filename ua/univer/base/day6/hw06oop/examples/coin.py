import random

class Coin:

    def __init__(self):
        self.__sideup = 'Eagle'

    def toss(self):
        if(random.randint(0, 1)) == 0:
            self.__sideup = 'Eagle'
        else:
            self.__sideup = 'Nut'

    def get_sideup(self):
        return self.__sideup

