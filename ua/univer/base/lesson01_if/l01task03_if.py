# 3. Даны 5 чисел (тип int). Вывести вначале наименьшее,
#    а затем наибольшее из данных чисел.

a = 2
b = 3
c = 4
d = 3
e = 5
min = a
max = a

if b < min:
    min = b
elif b > max:
    max = b
if c < min:
    min = c
elif c > max:
    max = c
if d < min:
    min = d
elif d > max:
    max = d
if e < min:
    min = e
elif e > max:
    max = e

print(" The smallest value is: ",min, "\n", "The biggest value is: ",max)