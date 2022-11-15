
# this following once :
# 45 * 3 =55 and 59+9 = 77 and  56 /6 = 4 and 50-30=40
#
# your problem take should operator and the two number as input the user and then return the result

print("\nWelcome Sir.")
print("Here you can do the any type of Math operation.")
print("Go ahead and try.")

# Given Below all code provide functionality to program

# number1=int(input("Input a numder1 :"))
# operator= input("Input any operator : +,-,/,* :")
#
# if operator == '+':
#     print("Inoput value number2 :")
#     number2 =int(input())
#     if number1 == 59 :
#         if number2 == 7:
#             print("Result is  : 77")
#         else:
#             print("Result is ",number1+number2)
#     else:
#         print("Result is = ",number1+number2)
#
#
# elif operator == '-':
#     print("Input second numder2")
#     number2=int(input())
#     if number1 == 50:
#         if number2 ==30:
#             print("Result is = 40")
#         else:
#             print("result is=",number1-number2)
#     else:
#         print("result is ",number1-number2)
#
# elif operator == "*":
#     print("Input second number :")
#     numder2=int(input())
#     if number1 == 45:
#         if numder2 == 3 :
#             print("Result is : 555")
#         else:
#             print("result is =",number1*numder2)
#     else:
#         print("result is =",number1*numder2)
# elif  operator == '/':
#     print("input a second number :")
#     number2=int(input())
#     if number1 == 65:
#         if number2 == 6:
#             print("Result is :6")
#         else:
#             print("result is :",number1/number2)
#     else:
#         print("result is :",number1/number2)
# else:
#     print("not found")

# this following once :
# 45 * 3 =55 and 59+9 = 77 and  56 /6 = 4 and 50-30=40
#
# your problem take should operator and the two number as input the user and then return the result

Input1 = int(input("Input value  frist :"))
operator =input("input any operator ,+,-,*,/,% :")
Input2 =int(input("Input value second :"))
result = 0

if operator == '+':
    if Input1 == 59:
        if Input2 == 9:
            result =77
        else:
            result = Input1+Input2
    else:
        result = Input1+Input2
elif operator == '*':
    if Input1 == 45:
        if Input2 == 3:
            result =555
        else:
            result = Input1*Input2
    else:
        result = Input1 * Input2
elif operator == '-':
    if Input1 == 50 :
        if Input2 == 30:
            result =40
        else:
            result= Input1 - Input2
    else:
        result= Input1 - Input2

elif operator =='/':
    if Input1 == 56:
        if Input2 ==6:
           result=4
        else:
            result = Input1 / Input2
    else:
        result = Input1 / Input2
elif operator =='%':
    if Input1 == 44:
        if Input2 == 9:
            result = 12
        else:
            result = Input1 % Input2
    else:
        result = Input1 % Input2
else:
    result="Result is not found !"

print(result)

#coppy



# Exercise 2 Faulty Calculator
"""design the calculator which will correctly solve all the problems except the following ones:
                                        45*3=555,56+9=77,56/6=4
Your program should take operator and the two numbers as input from the user and then return the result"""
print("WELCOME TO KAIF'S FAULTY CALCULATOR")
print("Enter your first number")
num1 = int(input())
print("Enter your second number")
num2 = int(input())
print("Enter operator:")
op = input()
if op=='+'and num1==56 and num2==9:
    print("Your faulty ans is 77")
elif op=='+':
    print("Your Sum is:",num1+num2)
if op == '-' and num1 == 56 and num2 == 9:
    print("Your faulty ans is 108")
elif op == '+':
    print("Your difference is:", num1 - num2)
if op == '*' and num1 == 45 and num2 == 3:
    print("Your faulty ans is 555")
elif op == '+':
    print("Your product is:", num1*num2)
if op == '/' and num1 == 56 and num2 == 6:
    print("Your faulty ans is 4")
elif op == '/':
    print("Your quotient is:", num1/num2)
else:
    print("INVALID INPUT")




