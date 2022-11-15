# print("good morning !")
#
# """ this is python coding ....."""
#
# print("sumilon is good boy. \n He study in Dhaka international university.")
# #secence character of python
# print("Manually Added  space in string Guru   99")
#
# print(" Manually \t added  \t speace \t in \t string \t guru \t")
#
# print(" differents of it ")
#
# print("Manually \n added \n speases \n in  \n string \n guru \n 99")
#
# text = "guru \n 99"
# print(text)
#
# print("line1\t line2\t line3")
#
# print("Hello \n world ")
#
# var1 ="Dhaka internationa  university"
# var2 = 23
# var3 = 23.60
# var4 = 8j
# print(var1)
# print(var2)
# print(var3)
#
# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))

# name ="sumilon"
# age = 20
# var1 = 30.00
# var2 = 4j
# print(type(name))
# print(type(age))
# print(type(var1))
# print(type(var2))

# var1 = "hello world"
# var2 ="sumilon biswas"
# var3 =7
# var4 = 36.90

# print(var1 + var2)  #output : hello world sumilon biswas
# # print(var1 + var3) # output : Error
# print(var3 + var4) # output : 42.90

# var1 = "45"
# var2 = "66"
# print(var1 + var2)
# #casting the variable
# res = int(var1) + int(var2)
# print(res)
#
# var1 = "55"
# var2 = "55"
# print(int(var1)+int(var2))

# print(10 * "hello world \n")
# print(20 * " sumilon biswas anik \n")
#
# var1 = "67"
# var2 = "70"
#
# result = int(var1) + int(var2)
# show_str = str(result), 677
# print(result)
# print(type(result))
# print(type(show_str))
# print(show_str)

# number1 =input("Enter you fristnumber:")
# number2 = input("Enter you secod number :")
# # print(number1 + int(number2))
# print(int(number1)+int(number2))

# print("Enter you frist number :")
# n1 = input()
# print("Enter second number :")
# n2= input()
#
# result = int(n1) + int(n2)
# print("number ={} and  number 2 ={} result ={}",n1,n2,result)

# make a calculator in pyrthon


# result = 0
# print("Enter number1 :")
# number=int(input())
#
# print("Input any operator :")
# operator= input()
#
# print("Enter number2")
# number2 = int(input())
#
# if operator == '+':
#     result = number + number2
# elif operator == '-':
#     result = number - number2
# elif operator == '*':
#     result = number * number2
# elif operator == '/':
#     result = number /number2
# elif  operator == '//':
#     result =number // number2
# elif operator == '%' :
#     result = number % number2
#
# else:
#     print("not select of any operator")
#
# print("the result is  =",result)

print("Input a frist value :")
number1 =int(input())
print("Input any operator :")
operator = input()
print("Input a second value :")
number2 =int(input())

result = 0

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result =number1 * number2
elif operator == '/':
    result = number1 / number2
elif operator == '//':
    result = number1 // number2
elif operator == '%':
    result = number1 % number2
elif operator == '**':
    result = number1 ** number2
else:
    print("not select any operator :")
print("result is ",result)



