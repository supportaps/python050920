# 1. При помощи цикла for вывести на экран нечетные числа
# от 1 до 99.

def print_odd_with_if():
    for i in range(1, 100):
        if i % 2 != 0:
            print(i, end=' ')


def print_odd_by_range(start,stop):
    for i in range(start, stop, 2):
        print(i, end=' ')
    print('\n')

def print_odd_by_while():
    i = 1
    while i < 100:
        print(i)
        i+=1

def sum(x:int,y:int) -> int:
    return x+y

def task02_print_N_K(n, k):
    for i in range(n):
        print(k)

def task03_print_from_a_to_b_with_count(a, b):
    if a < b :
        count = 0
        for i in range(a, b + 1, 1):
            print(i, end=", ")
            count += 1
            print("count = ", count)

def task04_print_10_number_from(start = 0, step = -5):
    count = 10
    x = start
    while count > 0 :
        print(x)
        x = x + step
        count -= 1

def task05_factorial(n):
    fact = 1
    for i in range(1, n + 1, 1):
        fact = fact * i
    return fact

def task06_pow(x, n):
    p = 1
    for i in range(n):
        p = p * x
    return p

def task08_draw_shape():

    number_of_shape = int(input("Choice the shape:\n1. Square\n2. Rectangular triangle\n3. Equilateral triangle\n4. Rhomb\n"))
    symbol2 = ""
    space = ""
    symbol3 = ""

    if number_of_shape == 1:
        for i in range(10):
            symbol2 = "*" + "  " + symbol2

        for l in range(len(symbol2) - 4):
            space = str(i).replace(str(i), " ") + space

        for j in range(10):
            if j == 0:
                print(symbol2)
            elif j >= 1 and j <= 8:
                print("*" + space + "*")
            elif j == 9:
                print(symbol2)

    if number_of_shape == 2:

        for i in range(10):
            symbol2 = "*" + "  " + symbol2
            print(symbol2)

    if number_of_shape == 3:

        for i in range(10):
            symbol2 = "*" + "  " + symbol2
            symbol3 = "   " + "*" + symbol2
            for l in range(len(symbol2) - 4):
                space = str(i).replace(str(i), " ") + space
                print(symbol3 + symbol2)





if __name__ == '__main__':
    task04_print_10_number_from()