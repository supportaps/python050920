# 1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.
a = 2
b = 3
c = 4
d = 3

if a < b and a < c and a < d:
    min = a
elif b < a and b < c and b < d:
    min = b
elif c < b and c < a and c < d:
    min = c
else: min = d
print(min)

