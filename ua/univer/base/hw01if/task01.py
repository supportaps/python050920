# l. День недели. Напишите программу, которая запрашивает у пользователя число в диапазоне
# от 1 до 7. Эта программа должна показать соответствующий день недели, где
# l - понедельник, 2 - вторник, 3 - среда, 4 - четверг, 5 - пятница, 6 - суббота и
# 7 - воскресенье. Программа должна вывести сообщение об ошибке, если пользователь
# вводит номер, который находится вне диапазона от 1 до 7.

day_value = int(input(" Input value: "))

if day_value == 1:
    print(" Monday")
elif day_value == 2:
    print(" Tuesday")
elif day_value == 3:
    print(" Wednesday")
elif day_value == 4:
    print(" Thursday")
elif day_value == 5:
    print(" Friday")
elif day_value == 6:
    print(" Saturday")
elif day_value == 7:
    print(" Sanday")
else:
    print( "Please enter value from 1 to 7: ")
