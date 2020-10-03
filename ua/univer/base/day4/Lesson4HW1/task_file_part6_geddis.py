import random

# 1. Вывод файла на экран. Допустим, что файл numbers.txt содержит ряд целых чисел и
#существует на диске компьютера. Напишите программу, которая выводит на экран все
#числа в файле.

def task1_v1():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 67, 5, 23, 1, 2, 43, 99]
    numbers_file = open("numbers.txt", "w")
    numbers_file.write(str(numbers))
    numbers_file.close()

    numbers_file = open("numbers.txt", "r")
    data = numbers_file.readline()
    print(data)
    numbers_file.close()

def task1_v2():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 67, 5, 23, 1, 2, 43, 99]
    with open("data.txt", "w") as wfile:
        wfile.write(str(numbers))

    with open("data.txt", "r") as rfile:
        print(rfile.readline())

# 2. Вывод на экран верхней части файла. Напишите программу, которая запрашивает
# у пользователя имя файла. Программа должна вывести на экран только первые пять строк
# содержимого файла. Если в файле меньше пяти строк, то она должна вывести на экран
# все содержимое файла.

def task2_v1():
    count = 0
    input_file_name = input("Input file name: ")
    file = open(input_file_name, "r")
    data = file.readline()
    print(data)
    while data != '':
        if count < 4 and data != '':
            data = file.readline()
            print(data)
            count +=1
    file.close()


def task2_v2():

    input_file_name = input("Input file name: ")
    file = open(input_file_name, "r")
    for i in range(5):
        line = file.readline()
        if line != '':
            print(line)

    file.close()

# 3. Номера строк. Напишите программу, которая запрашивает у пользователя имя файла.
# Программа должна вывести на экран содержимое файла, при этом каждая строка должна
# предваряться ее номером и двоеточием. Нумерация строк должна начинаться с 1.

def task3_v1():
    count = 1
    input_file_name = input("Input file name: ")
    file = open(input_file_name, "r")
    line = file.readline()
    print(str(count) + ":",line)

    while line != '':
        count += 1
        line = file.readline()
        if line != '':
            print(str(count) + ":", line)

def task3_v2():
    input_file_name = input("Input file name: ")
    file = open(input_file_name, "r")
    i = 0
    for line in file:
        i += 1
        print(str(i) + ":", line)


# 4. Счетчик значений. Допустим, что файл с серией имен (в виде строковых значений)
# называется names.txt и существует на диске компьютера. Напишите программу, которая
# показывает количество хранящихся в файле имен. (Подсказка: откройте файл и прочитайте
# каждую хранящуюся в нем строку . Примените переменную для подсчета количества
# прочитанных из файла значений.)

def task4():
    count = 0
    file = open("names.txt", "r", encoding="utf-8")
    for name in file:
        if name != "\n":
            count += 1
            #print(name)
    print(count)

# 5. Сумма чисел. Допустим, что файл с рядом целых чисел называется numbers .txt и существует
# на диске компьютера. Напишите программу, которая читает все хранящиеся
# в файле числа и вычисляет их сумму.

def task5():
    sum = 0
    numbers_file = open("numbers.txt", "r")
    arr = []

    for row in numbers_file:
        arr = row.replace("]", "").replace("[", "").replace(" ", "").split(",")
    for elem in arr:
        sum += int(elem)

    print(arr)
    print("The sum value is : ", sum)



# 6. Среднее арифметическое чисел. Допустим, что файл с рядом целых чис~л называется
# numbers.txt и существует на диске компьютера. Напишите программу, которая вычисляет
# среднее арифметическое всех хранящихся в файле чисел.

def task6():

    numbers_file = open("numbers.txt", "r")
    arr = []
    sum = 0
    for row in numbers_file:
        arr = row.replace("]", "").replace("[", "").replace(" ", "").split(",")
    for i in range(len(arr)):
        sum += int(arr[i])

    aver = sum / (i + 1)
    print("The average value is : ", aver)


# 7. Программа записи файла со случайными числами. Напишите программу, которая
# пишет в файл ряд случайных чисел . Каждое случайное число должно быть в диапазоне
# от 1 до 500. Приложение должно предоставлять пользователю возможность назначать
# количество случайных чисел, которые будут содержаться в файле.

def task7():

    random_list = []
    wfile = open("random_numbers_row.txt", "w")
    number_of_random_values = int(input("Input amount of random values: "))

    for i in range(number_of_random_values):
        random_number = random.randint(1, 500)
        random_list.append(random_number)


    wfile.write(str(random_list))
    wfile.close()

# 8. Программа чтения файлов со случайными числами. Выполнив предыдущее задание
# (программу записи файла со случайными числами), напишите еще одну программу, которая
# читает случайные числа из файла, выводит их на экран и затем показывает приведенные
# ниже данные:
# • сумму чисел;
# • количество случайных чисел, прочитанных из файла.

def task8():
    arr = []
    sum = 0

    task7()
    rfile = open("random_numbers_row.txt", "r")
    for row in rfile:
        arr = row.replace("]", "").replace("[", "").replace(" ", "").split(",")
    for i in range(len(arr)):
        sum += int(arr[i])


    print("The sum value is : ", sum)
    print("Total amount of numbers is: ", i + 1)

# 1 О. Очки в игре в гольф. Любительский гольф-клуб проводит турниры каждые выходные.
# Президент клуба попросил вас написать две программы:
# • программу, которая читает имя каждого игрока и его счет в игре, вводимые с клавиатуры,
# и затем сохраняет их в виде записей в файле golf.txt (каждая запись будет иметь
# поле для имени игрока и поле для счета игрока);
# • программу, которая читает записи из файла golf.txt и выводит их на экран.

def task10_1():

    wfile = open("golf.txt", "a")
    wfile.write("Name" + "Surname" + "Score")


    while True:
        #wfile = open("golf.txt", "a")
        name = input("Input the name of the player")
        score = input("Input the score of the player")

        wfile.write(name + score)


if __name__ == '__main__':
    task10_1()