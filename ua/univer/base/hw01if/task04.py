#4. Римские цифры. Напишите программу, которая предлагает пользователю ввести число
#в диапазоне от 1 до 10. Программа должна показать для этого числа римскую цифру.
#Если число находится вне диапазона 1--1 О, то программа должна вывести сообщение об
#ошибке. В табл. 3.8 приведены римские цифры для чисел от 1до10.

value = int(input( "Input vale from 1 to 10: "))

if value == 1:
    print('I')
elif value == 2:
    print('II')
elif value == 3:
    print("III")
elif value == 4:
    print('IV')
elif value == 5:
    print('X')
elif value == 6:
    print('VI')
elif value == 7:
    print('VII')
elif value == 8:
    print('VIII')
elif value == 9:
    print('IX')
elif value == 10:
    print('X')
else:
    ( "Your input isn't correct")