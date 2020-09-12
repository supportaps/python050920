# 2. Площади прямоугольников. Площадь прямоугольника- это произведение его длины
# на его ширину. Напишите программу, которая запрашивает длину и ширину двух прямоугольников.
# Программа должна выводить пользователю сообщение о том, площадь какого
# прямоугольника больше, либо сообщать, что они одинаковы.

length1 = int(input(" Input lenght of the first rectangle: "))
width1 = int(input(" Input width of the first rectangle: "))
length2 = int(input(" Input lenght of the second rectangle: "))
width2 = int(input(" Input width of the second rectangle: "))

s1 = length1 * width1
s2 = length2 * width2

if s1 > s2:
    print(" The square of the first rectangle is bigger")
elif s1 < s2:
    print(" The square of the second rectangle is bigger")
else:
    print(" The squares are equal")