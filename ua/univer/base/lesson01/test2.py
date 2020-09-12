#calculator

x = int(input("Enter x: "))
y = int(input("Enter y: "))
op = input("operation (+,-,*,/)")
if op == '+':
    result = x + y
elif op == '-':
    result = x - y
elif op == '/':
    result = x / y
elif op == '*':
    result = x * y

print("Sum = "+ str(result))