# -*- coding: utf8 -*-
import pickle

from ua.univer.base.day6.hw06oop.examples import cellphone

FILENAМE = 'cellphones.dat'

def main():
    again = 'д'
    output_file = open(FILENAМE,'wb')

    while again.lower() == 'д':
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Bвeдитe розничную цену: '))

        phone = cellphone.CellPhone(man, mod, retail)
        pickle.dump(phone, output_file)

        again = input('Введете еще один элемент данных? (д/н): ')

    output_file.close()
    print('Данные записаны в', FILENAМE)

main()

