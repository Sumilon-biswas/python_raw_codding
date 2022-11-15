
"""

lambda function is a without a name .
it is not powerful as named function
it is working with single expression/single line of code

syntex of lambda

lambda agrument:expression

"""

# add=lambda  a,b:a+b
# print(add(5,8))

addition=lambda a,b:a+b
substruction=lambda a,b:a-b
multification=lambda a,b:a*b
division=lambda  a,b:a/b
modulals=lambda a,b:a%b
floorDivision=lambda a,b:a//b


number1=int(input("Input number 1:"))
number2=int(input("Input number 2:"))


operators=input("choose your operators +,-,*,/,//,% :")

if operators == '+':
    print(addition(number1,number2))
elif operators == '-':
    print(substruction(number1,number2))
elif operators == '*':
    print(multification(number1,number2))
elif operators == '/':
    print(division(number1,number2))
elif operators == '%':
    print(modulals(number1,number2))
elif operators == '//':
    print(floorDivision(number1,number2))
else:
    print("choose the correct opertors !")

