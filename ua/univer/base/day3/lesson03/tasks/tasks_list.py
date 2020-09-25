# 1.создайте массив, содержащий 10 первых нечетных чисел.
# Выведете элементы массива на консоль в одну строку, разделяя запятой
def task1_v1():
    odd_list = []
    for x in range(1,20,2):
        odd_list.append(x)
    print(odd_list)

def task1_v2():
    odd_list = list(range(1,20,2))
    print(odd_list)

def task1_v3():
    odd_list = []
    x = 1
    while len(odd_list) < 10:
        odd_list.append(x)
        x += 2
    print(odd_list)

#2.ввести 10 целых значений с консоли и разместить в
#2 масива четные и нечетные
#3.подсчитать сколько четные и нечетные

def task2_v1(odd_list = [], even_list = []):
    count_odd = 0
    count_even = 0
    elements = []
    for _ in range(0, 5):
        num = int(input('Input number: '))
        elements.append(num)
    print(elements)

    for elem in elements:
        if elem % 2 == 0:
            odd_list.append(elem)
            count_odd += 1

        else:
            even_list.append(elem)
            count_even += 1

    print("Odd = ", odd_list)
    print("count odd = ", len(odd_list))
    print("Even = ", even_list)
    print("count even = ", len(even_list))

def task2_v2():

    odd_list = []
    even_list = []
    for _ in range(0, 10):

        num = int(input('Input number: '))

        if num % 2 == 0:
            odd_list.append(num)

        else:
            even_list.append(num)


    print("Odd = ", odd_list)
    print("count odd = ", len(odd_list))
    print("Even = ", even_list)
    print("count even = ", len(even_list))

    return odd_list, even_list
#3 подсчитать сколько четных и нечетных
def task3_count_even_odd():
    odd_list, even_list = task2_v2()
    print("", len(odd_list))
    print("", len(even_list))

#4.сумма елементов в каждом масиве и среднее арифметическое
def task4_sum_average():
   # even_list = []
   # odd_list = []
   # task2_v2(odd_list, even_list)
    odd_list, even_list = task2_v2()
    print(get_sum_and_aver(odd_list))
    print(get_sum_and_aver(even_list))
    print(odd_list)
    print(even_list)


def get_sum_and_aver(el_list):
    sum = 0
    for el in el_list:
        sum += el
    aver = sum / len(el_list)
    return sum, aver

#5поменять четные позиции в первом масиве на значения
#нечетных позиций из 2 массива

def task5_change_pos(odd_list, even_list):

    if len(odd_list) < len(even_list):
        max_number = len(odd_list)
    else:
        max_number = len(even_list)

    for i in range(0, max_number - 1):
        temp = odd_list[i]
        odd_list[i] = even_list[i+1]
        even_list[i + 1] = temp


#6.Дан массив размерности N,  найти наименьший элемент массива
#и вывести на консоль (если наименьших элементов несколько —
#вывести их индексы).

#def task6_find_min():




if __name__ == '__main__':
    odd_list, even_list = task2_v2()
    task5_change_pos(odd_list, even_list)