# num = int(input("Input a num value :"))
# num1 = int(input("Input a num1 value :"))
#
# #addition operators sign +
# # add = num + num1
# # print("summation of  :",add)
#
# #substracts operators sign -
# # sub = num - num1
# # print("sub :",sub)
#
# #multiplication operation sign *
#
#
# # mult = num * num1
# # print("multipulation =",mult)
#
# #Division operators division /
#
# # Div = num / num1
# # print("Division =",Div)
#
# # # Modulus operators sign %
# # mod = num %  num1
# # print("modulus =",mod)
# #
# # # Exponentiation operators
# #
# # Exportant = num ** num1
# # print("Exportanted =",Exportant)
# # print(4*4)
#
# # # 	Floor division
# #
# #
# # FloodDiv = num // num1
# # print("flood divison :",FloodDiv)
#
# # Arthimatic operation
#
# num = 10
# num2 = 3
#
# # # addition of
# # add = num + num2 # 10 +3 = 13
# # print("addition :",add)
#
# # substraction
# sub = num - num2 # num=10 - num2=3 = 7
# print("substraction :",sub)
#
# # multiplication
#
# mult = num * num2 # num=10 * num=3 multiplication = 30
# print("multiplication =",mult)
#
# # division
#
# Div = num / num2 # num= 10 # / num2 = 3 = division = 3.33
# print("Division =",Div)
#
# # Modulus operator
#
# modul = num % num2 #num=10 % num2 =3 modulse = 1
# print("modulse =",modul)
#
# #Exponentiation operation
#
# Expention = num ** num2 # num =10 ** num2=3 = Expention =10 * 10 * 10 =1000
# print("Expontiation =",Expention)
#
# # floor division
#
# fDiv = num // num2 # num=10 // num2 =3 floor division = 3
# print("floor division =",fDiv)

#Python Assignment Operators
# print("python assignment Operators")
# #equal operator
# x = 5
# print(x)
# # assigment operators addition equale
# x += 6
# print("addition equale =", x)

x = 9
# #assigment substract perator
# x -= 4
# print("assigment substract Result =",x) # result is = 5

# # assigment multiplication operators
# x  *= 3
# print(" assigment multiplication operators = ",x) # result = 27

# # assignment Division operator
# x /= 3
# print("Assigment Division operators =",x) # assimgment division operator = 3.0

# assigment modulals operators
#
# x %= 2
# print("Assigment modulalse operators =",x)

# # assigment flood division operators
# x //= 5
# print("assigment floor division =",x)

# x = 5
#
# x//=3
#
# print("floor division operators =",x)

# assigment Extinable offers
#
# x=7
# x **= 5
# print("Exptentiable opertaor =",x)

#Comparison Operators in Python
# a = 13
# b = 33

# # a = 33
# # b=13
# a = 20
# b = 30
#
# # a = 13 > b = 33 = False
# # a =33 > b = 13 =True
# # a =5 > b = 5 = False
# print(a > b)
#
# # a =13 < b = 33 = True
# # a =33 < b =13 = false
# # a=5 < bv =5 = false
# print( a < b)
#
# # a=13 == b=33 == False
# # a =33 == b=13 = false
# # a=5 == b== 5 = true
# print(a == b)
#
# #a =13 >= b =33 = False
# # a = 33 >= b ==13 =True
# # a= 5  >= b =5 = true
# print(a >= b)
#
# # a=13 <= b=33 = True
# # a=33 <= b=13 = False
# # a = 5 <= b=5 = true
# print(a <= b)
#
# # a = 5 != b=5 = False
# # a = 20 != b = 5 = True
#
# print( a != b)


# logical operator use python

   #Exmple of logical operator

# a =True
# b = False
# a=True
# b =True
# a = False
# b= False
# a=False
# b = True
#
# # a =true and b = false = false
# # a = True and b = True = True
# # a =False  and b = False = False
#
# print(a and  b)
#
# # a = true or b = false = true
# # a = true or b = True =True
# # a = false or b = false = false
#
# print(a or b)
#
# # a =true = false
# # b = false = true
# print(not a)
# print(not b)

# Bitwise Operators in Python
# a =32
# b= 12
# print(a & b)


# a= 10
# b= 8
# # print(a & b)
# print(a|b)
#
# x=15
# y = 13
# print(x|y)
#
# aa = 25
# bb=17
# print(aa | bb)

# a= 10
# print(a>>2) # 10 /2= 5 and 5 / 2 =2
# print("+++++++++++++++")
# print(a<<2) # 10*2= 20 and 20 * 2=40
#
# print("============")
# b =15
# right shift
# print(b >>2)  # output genarator 15 /2 = 7 and 7 /2 = 3
# left shift
# print(b << 3) # output genarator 15*2 = 30 and 30 * 2 =60 and 60 * 2= 120

# a = int(input("Input a value :"))
#
# c = a << 2
# print("Result is :",c)
# d = a >> 2
# print("Result is ",d)

#Identity operators

a = 20
b = 30
c = a
 # a=20 and b=30 between separted value
print( a is not  b)
print(a is c )

# x =20
# list=[10,30,40,60,70,20]
#
# # if x in list:
# #     print("yes! value of present.")
# # else:
# #     print("No value is not paresent !")
#
# # if x not in list:
# #     print("yes ! this values is not insert !")
# # else:
# #     print("NO! value is include of list!")

# fname ="summon"
# name_list=["sumilon", "anik","tanbir","joya","sagor"]
# if fname in name_list:
#     print("Yes !")
# else:
#     print("NO!")

#Operator Precedence

Expr = 10 + 30 * 20
print("result is :",Expr)

print(10- 4 * 2)
print((10-7)*2)  # answr = 6
