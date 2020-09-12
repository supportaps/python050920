# 2. Вывести на консоль количество максимальных чисел среди этих четырех.

a = 4
b = 3
c = 4
d = 3
max = a
count = 0

if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d

if max == a:
    count += 1
if max == b:
    count += 1
if max == c:
    count += 1
if max == d:
    count += 1

print(" The max value is: ", max, "\n", "Number of max value is: ", count)