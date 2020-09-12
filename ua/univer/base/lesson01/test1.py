# Buy alcohol in the market
# 10.00 < time < 23.00
# age > 18

time = float(input(" current time? "))
age = int(input(" age?"))
result = bool(time > 10.00 and time < 23.00 and age > 23)
print(" you can buy alcohol ", result)
