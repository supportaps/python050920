# -*- coding: utf8 -*-

from ua.univer.base.day6.hw06oop.hwexercises06geddis.car import Car
from ua.univer.base.day6.hw06oop.hwexercises06geddis.employee import Employee
from ua.univer.base.day6.hw06oop.hwexercises06geddis.personaldata import personalData
from ua.univer.base.day6.hw06oop.hwexercises06geddis.pet import Pet
from ua.univer.base.day6.hw06oop.hwexercises06geddis.retailitem import retailItem


def task1_class_Pet():
    name = input("Input name of the pet: ")
    type_of_pet = input("Input type of the pet: ")
    age = input("Input agef of your pet: ")
    pet1 = Pet(name, type_of_pet, age)
    pet1.set_name(name)
    pet1.set_animal_type(type_of_pet)
    pet1.set_age(age)
    print(
        f"Your pet name is: {pet1.get_name()} , he is a {pet1.get_animal_type()}, and he is {pet1.get_age()} years old")


def task2_class_Car():
    car = Car()
    for speed_up in range(5):
        car.accelerate()
        print(f"Current speed is {car.get_speed()}")
    for speed_down in range(5):
        car.breeak()
        print(f"Current speed is {car.get_speed()}")


def task3_personal_data():
    first_person = personalData()
    second_person = personalData()
    third_person = personalData()

    def create_three_persons(first_person, second_person, third_person):
        first_person.set_name('Jack')
        first_person.set_adress('kiev')
        first_person.set_age(36)
        first_person.set_phone_number('0503323045')
        second_person.set_name('Antony')
        second_person.set_adress('kiev')
        second_person.set_age(35)
        second_person.set_phone_number('0506666666')
        third_person.set_name('Denis')
        third_person.set_adress('kiev')
        third_person.set_age(37)
        third_person.set_phone_number('050333333333')

    def print_person(person):
        print(f"{person.get_name()}, {person.get_adress()}, {person.get_age()}, {person.get_phone_number()}")

    create_three_persons(first_person, second_person, third_person)
    print_person(first_person)
    print_person(second_person)
    print_person(third_person)


def task4_employee():
    def create_employee():
        employees = []
        employees.append(Employee('Suzan Meyers', 47899, 'BG', 'president'))
        employees.append(Employee('Mark Dzhouns', 39119, 'IT', 'programmer'))
        employees.append(Employee('Dzhoy Rodzhers', 81774, 'PR', 'engineer'))
        return employees

    for employee in create_employee():
        print(f"{employee.get_name()}, {employee.get_id()}, {employee.get_department()}, {employee.get_position()}")

def task5_item():
    def create_item():
        items = list()
        items.append(retailItem("Товар №1", "Пиджак", 12, 59.95))
        items.append(retailItem("Товар №2", "Дизайнерские джинсы", 40, 34.95))
        items.append(retailItem("Товар №3", "Рубашка", 20, 24.95))
        return items

    for item in create_item():
        print(f"{item.get_name()}, {item.get_description_of_item()}, {item.get_number_of_item()}, {item.get_prise()}")



if __name__ == '__main__':
    task5_item()
