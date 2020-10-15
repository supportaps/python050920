# -*- coding: utf8 -*-
from ua.univer.base.day6.hw06oop.examples import bankaccount, cellphone
from ua.univer.base.day6.hw06oop.examples.cellphone import CellPhone
from ua.univer.base.day6.hw06oop.examples.coin import Coin


def example_with_coin():
    my_coin = Coin()
    print("This side is up: ", my_coin.get_sideup())
    # print("Throwing the coin: ")
    print("I'm going to throw up the coin ten times: ")
    for i in range(10):
        my_coin.toss()
        print("This side up is: ", my_coin.get_sideup())


def example_with_bancaccount():
    start_bal = float(input("Input your current savings: "))
    savings = bankaccount.BankAccount(start_bal)
    pay = float(input("How much have you earned for last week: "))
    print("Adding your savings on your account....")
    savings.deposit(pay)
    print(savings)
    cash = float(input('How much would you like to withdraw? '))
    print("Withdrawing cash from you account.....")
    savings.withdraw(cash)
    print(savings)


def example_with_cellphone():
    man = input('Введите производителя: ')
    mod = input('Введите номер модели: ')
    retail = float(input('Bвeдитe розничную цену: '))
    phone = CellPhone(man, mod, retail)
    print('Вот введенные Вами данные:')
    print('Производитель:', phone.get_manufact())
    print('Номер модели: ', phone.get_model())
    print('Розничная цена: $', format(phone.get_retail_price(), '.2f'), sep='')

    def make_list():
        phone_list = []

        print('Введите данные о пяти телефонах.')

        for count in range(1, 6):
            print('Hoмep телефона ' + str(count) + ':')
            man = input('Введите производителя: ')
            mod = input('Введите номер модели: ')
            retail = float(input('Bвeдитe розничную цену: '))
            print()
            phone = cellphone.CellPhone(man, mod, retail)
            phone_list.append(phone)

        return phone_list

    def display_list(phone_list):
        for item in phone_list:
            print(item.get_manufact())
            print(item.get_model())
            print(item.get_retail_price())
            print()

    phones = make_list()
    print('Boт введенные Вами данные:')
    display_list(phones)


if __name__ == '__main__':







    example_with_cellphone()