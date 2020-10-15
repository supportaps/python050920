
from ua.univer.base.day6.hw06oop.examples import coin


def main():


    my_coin = coin.Coin()
    print(my_coin.get_sideup())
    flip(my_coin)
    print(my_coin.get_sideup())



def flip(coin_obj):
   coin_obj.toss()



main()