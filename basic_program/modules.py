import  operation as oper
number1=int(input("Input value Number1 : "))
operator=input("INput any operator :+,-,*,/,// :")
number2=int(input("Input second number2 :"))

result = 0

if operator == '+':
    result = oper.addition(number1,number2)
elif operator == '-':
    result = oper.substraction(number1,number2)
elif operator == '*':
    result = oper.multipal(number1,number2)
elif operator == '/':
    result = oper.division(number1,number2)
elif operator == '//':
    result = oper.intagerdivsion(number1,number2)
elif operator == '%':
    result =oper.modules(number1,number2)
else:
    result ="please valide data type"

print(f"Result is ={result}")

