
# # write a program to create a function and  two agrument 1st agr is name and second agr is age an print it
#
# def  fun(name,age):
#     print(f"name is ={name} and age= {age}")
#
# fun("sumilon biswas",21)

#write a program a create a funch and multipla agrument pass in function and print it

# def fumct1(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#
# fumct1(20,30,40,50)

# write a prprogram a create a function a multpail value pass one argument

# def  myfunction(*args):
#     for item in args:
#         print(item)
#
# myfunction(20,30,40)

# write a program a create function a multipal name pase the  argument

# def myfunction(*args):
#     for item in args:
#         print(item)
#
# myfunction("sumilon","naiem",'joya',"Tanbir islam","mona","software Engineeringer","likhon")

# def showEmployee(name,salary=9000):
#     print(f"name :{name} and salary ={salary}")
#
#
# showEmployee("sumilon biswas ",14000)
# showEmployee("anika",)
# showEmployee("Ahona Rehman",53563)


#  create a inner_function and calulated addition a,b

# def outer_fun(a,b):
#     squard=a**2
#
#     def innerfun(x,y):
#         return  a + b
#
#     add=innerfun(a,b)
#
#     return add
#
# result=outer_fun(10,20)
# print("Result :",result)
#
# def outerfunc(operator,a,b):
#     if operator == '+':
#         def addition(x,y):
#             return x+y
#     elif operator == '-':
#          def substraction(x,y):
#              return  x-y
#     elif operator == '*':
#         def multipaliction(x,y):
#             return  x * y
#     elif operator == "/":
#         def division(x,y):
#             return  x/ y
#     elif operator == "%":
#         def modulas(x,y):
#             return x % y
#     else:
#         print("please ! select the operator ")
#
#     print(addition(a,b))
#     print(substraction(a,b))
#     print(multipaliction(a,b))
#     print(division(a,b))
#     print(modulas(a,b))
#
#
#
# op=input("Input operator :")
#
#
# result = outerfunc(op,10,5)
# print(result)

#Rescurive function

# def RescursiveFun(num):
#     if num:
#         return  num + RescursiveFun(num-1)
#
#     else:
#         return 0
#
#
# res=RescursiveFun(10)
# print("Rescursive Result ",res)
#
# def Rescurivefun(num):
#     if num:
#         return  num + Rescurivefun(num-1)
#     else:
#         return 0
#
# res=Rescurivefun(10)
# print("Rescurive result is",res)



result=list(range(4,30,2))
print(result)