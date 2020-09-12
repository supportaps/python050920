#4. Общий объем продаж. Покупатель приобретает в магазине пять товаров. Напишите программу,
#которая запрашивает цену каждого товара и затем выводит накопленную стоимость
#приобретаемых товаров, сумму налога с продаж и итоговую сумму. Допустим, что
#налог с продаж составляет 7%.

item1 = float(input(" Input the cost of the item 1: "))
item2 = float(input(" Input the cost of the item 2: "))
item3 = float(input(" Input the cost of the item 3: "))
item4 = float(input(" Input the cost of the item 4: "))
item5 = float(input(" Input the cost of the item 5: "))

cost_items = item1 + item2 + item3 + item4 + item5
tax = (cost_items / 100) * 7
prise = cost_items - tax


print(" The cost of the items is: ", cost_items)
print(" The tax is: ", tax)
print(" The final prise is: ", tax)