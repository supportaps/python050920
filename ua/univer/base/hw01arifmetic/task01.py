#1. Персональные данные. Напишите программу, которая выводит приведенную ниже информацию:
#• ваше имя;
#• ваш адрес проживания, с городом, областью и почтовым индексом;
#• ваш номер телефона;
#• вашу специализацию в учебном заведении.

name = input("Input your name ")
street = input("Input your street ")
city = input("Input your city ")
region = input("Input your region ")
index = input("Input your index ")
adress = [street, city, region, index]
phone_number = input("Input your number phone ")
specialisation = input("Input your number specialisation ")

print(" ",name, '\n', adress, '\n', phone_number, '\n', specialisation)