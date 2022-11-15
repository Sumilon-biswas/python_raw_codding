number1 = int(input("Input a frist number : "))
opetaror =input("Input a operator : +,-,/,*,//,% :")
number2 =int(input("Input a second number : "))

result = 0

if opetaror == '+':
    result = number1 + number2
elif opetaror == '-':
    result = number1 - number2
elif opetaror == '*':
    result = number1 * number2
elif opetaror == '/':
    result = number1 / number2
elif opetaror == '%':
    result = number1 % number2
elif opetaror == '//':
    result = number1 // number2
else:
    result ="Result is not found!"

print("Result is :",result)

