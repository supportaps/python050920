#6. Налоr с продаж. Напишите программу, которая попросит пользователя ввести величину
#покупки. Затем программа должна вычислить федеральный и региональный налог с продаж.
#Допустим, что федеральный налог с продаж составляет 5%, а региональный - 2.5%.
#Программа должна показать сумму покупки, федеральный налог с продаж, региональный
#налог с продаж, общий налог с продаж и общую сумму продажи (т. е. сумму покупки и
#общего налога с продаж).
#Подсказка: для представления 2.5% используйте значение 0.025, для представления
#5% - 0.05.

total_purchase = float(input( " Input a purchase: "))
FEDERAL_TAX = 0.025
REGIONAL_TAX = 0.05

tax_federal = total_purchase * FEDERAL_TAX
tax_regional = total_purchase * REGIONAL_TAX
tax_total = tax_federal + tax_regional
sell_total = total_purchase + tax_total

print(" Sum of the purchase = ", total_purchase)
print(" Federal tax = ", tax_federal)
print(" Regional tax = ", tax_regional)
print(" Total = ", sell_total)