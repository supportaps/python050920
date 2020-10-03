import random

def sum_calculation(elements_list):
    sum = 0
    for el in elements_list:
        sum += el

    average = sum / len(elements_list)
    return sum, average


def find_min(el_list):
    mymin = el_list[0]
    for el in el_list:
        if el < mymin:
            mymin = el
    return mymin

def find_max(el_list):
    mymax = el_list[0]
    for el in el_list:
        if el > mymax:
            mymax = el
    return mymax

#1. Общий объем продаж. Разработайте программу, которая просит пользователя ввести
#продажи магазина за каждый день недели. Суммы должны быть сохранены в списке.
#Примените цикл, чтобы вычислить общий объем продаж за неделю и показать результат.


def general_total_selling():

     DAYS = 7
     x = 0
     selling_per_day = [] * DAYS
     sum_of_selling_per_week = 0

     while x <= DAYS - 1:
         input_data = float(input("Input selling for " + str(x + 1) + " day: "))
         #selling_per_day[x]  = input_data
         selling_per_day.append(input_data)
         sum_of_selling_per_week = sum_of_selling_per_week + selling_per_day[x]
         x = x + 1

     print(selling_per_day)
     print("SUM per week is: ", sum_of_selling_per_week)


#2. Генератор лотерейных чисел. Разработайте программу, которая генерирует семизначную
#комбинацию лотерейных чисел. Программа должна сгенерировать семь случайных
#чисел, каждое в диапазоне от О до 9, и присвоить каждое число элементу списка. (Случайные
#числа рассматривались в главе 5.) Затем напишите еще один цикл, который показывает
#содержимое списка.

def generator_random_value():

     random_list = []

     for i in range(0,9):
         random_number = random.randint(0,9)
         random_list.append(random_number)

     for x in random_list:
        print(random_list[x])

#3. Статистика дождевых осадков. Разработайте программу, которая позволяет пользователю
#занести в список общее количество дождевых осадков за каждый из 12 месяцев.
#Программа должна вычислить и показать суммарное количество дождевых осадков за
#год, среднее ежемесячное количество дождевых осадков и месяцы с самым высоким и
#самым низким количеством дождевых осадков.


def stat_rain():

    MONTH = 12
    rain_list = []

    for x in range(MONTH):
        rain_per_month = int(input("Input rain per month: "))
        rain_list.append(rain_per_month)

    sum_of_rain_per_year, average_per_year = sum_calculation(rain_list)

    mymin = rain_list[0]
    for el in rain_list:
        if el < mymin:
            mymin = el

    mymax = rain_list[0]
    for el in rain_list:
        if el > mymax:
            mymax= el

    print("SUM of rain per YEAR: ", sum_of_rain_per_year)
    print("SUM of rain per YEAR: ", average_per_year)
    print("Min rain value is: ", mymin)
    print("Max rain value is: ", mymax)


#4. Проrрамма анализа чисел. Разработайте программу, которая просит пользователя ввести
#ряд из 20 чисел. Программа должна сохранить числа в списке и затем показать приведенные
#ниже данные:
#• наименьшее число в списке;
#• наибольшее число в списке;
#• сумму чисел в списке;
#• среднее арифметическое значение чисел в списке.



def analyse_numbers():
    x = 0
    number_string = []
    input_value = 0
    while x < 20:
        input_value = int(input("Input number: "))
        number_string.append(input_value)
        x += 1

    min = find_min(number_string)
    max = find_max(number_string)
    sum, average = sum_calculation(number_string)

    print("Min value in the string is: ", min)
    print("Max value in the string is: ", max)
    print("Sum value in the string is: ", sum)
    print("Average value in the string is: ", average)


#Проверка допустимости номера расходноrо счета. Среди исходного кода главы 7,
#а также в подпапке data "Решений задач по программированию" соответствующей главы
#вы найдете файл charge_accounts.txt. Этот файл содержит список допустимых номеров
#расходных счетов компании. Каждый номер счета представляет собой семизначное число,
#в частности 5658845.
#Напишите программу, которая считывает содержимое файла в список. Затем эта программа
#должна попросить пользователя ввести номер расходного счета. Программа
#должна определить, что номер является допустимым, путем его поиска в списке. Если
#число в списке имеется, то программа должна вывести сообщение, указывающее на то,
#что номер допустимый. Если числа в списке нет, то программа должна вывести сообщение,
#указывающее на то, что номер недопустимый.

def check_number_from_file():

    count = 0
    number_of_count = 0
    number_list = []
    charge_accounts_file = open(r'C:\Users\yakovalenko\PycharmProjects\Python05_09_2020\ua\univer\base\day3\lesson03\Lesson03HW031\charge_accounts.txt', 'r')
    file_contents = charge_accounts_file.readlines()

    while True:
        number_of_count = input("Input 7 symbols number: ")
        for i in number_of_count:
            count += 1
        if count == 7:
            break
        else:
            print("You have entered more or less then 7 symbols.")
            count = 0


    for item in file_contents:
        if int(item.replace('\n', '')) == int(number_of_count):
            print("The number you have entered", item.replace('\n', ''), " is appropriate")
            break
    else:
        print("The number you have entered", item.replace('\n', ''), " isn't appropriate")





if __name__ == '__main__':
    stat_rain()