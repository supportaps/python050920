# -*- coding: utf8 -*-
import pickle

FILENAМE = 'cellphones.dat'

def main():

    end_of_file = False
    input_file = open(FILENAМE, 'rb')

    while not end_of_file:
        try:
            phone = pickle.load(input_file)
            display_data(phone)
        except EOFError:

            end_of_file = True

    input_file.close()

def display_data(phone):
    print('Производитель: ', phone.get_manufact())
    print('Номер модели: ', phone.get_model())
    print('Розничная цена: $',
          format(phone.get_retail_price(), ',.2f'),
          sep='')
    print()

main()

