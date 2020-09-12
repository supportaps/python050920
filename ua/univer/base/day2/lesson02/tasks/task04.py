# 4. Вывести 10 первых чисел последовательности 0, -5,-10,-15..



range = range(-15, 0, 1)
count = 0
for i in range:
    count = count + 1
    if count <= 10:
        print(i, end=' ')
    else:
        break

