
'''
  A Decorators  is a design patten in python
  that  allow a user to add new functionality to on existing object without modifying it structure taka

'''

# def fristName(lastname):
#     print("Rakib hossain")
#     lastName()
#
#
# def lastName():
#     print("Hossan")
#
#
# fristName(lastName)

#
# def fristName(lastName):
#     print("sumilon")
#     lastName()
#
#
# def lastName():
#     print("biswas anik")
#
# fristName(lastName)

# def string_uppper_case(function):
#
#     def make_uppor():
#         str=function()
#         return  str.upper()
#     return  make_uppor
#
# def printstring():
#     return "sumilon biswas anik"
#
# result=string_uppper_case(printstring)
# print(result())

# def string_lower_cas(function):
#      def make_lower():
#          str =function()
#          return  str.lower()
#      return  make_lower
#
# def myfunction():
#     return "SUMILON BISWAS ANIK"
#
#
# result=string_lower_cas(myfunction)
# print("printer lower case letter ",result())

#
# def Div_decortator(fun):
#     def inner_fun(x,y):
#         if  y == 0:
#             return "please give the proper values!"
#         return fun(x,y)
#     return  inner_fun
#
# @Div_decortator
#
# def div(a,b):
#     return a/b
# #
# # res=div(4,0)
# res=div(6,3)
# print(res)


# def div_vovels(fun):
#     def inner_fun(vowels):
#         if vowels == "a" or vowels == "e" or vowels =="i" or vowels =="o" or vowels =="u":
#             print("this letter is vowels !")
#         else:
#             print("consante letter")
#
#
#         return  fun(vowels)
#     return  inner_fun
#
#
# @div_vovels
# def vowels_check(letter):
#     return  letter
#
# result=vowels_check('b')
# print(result)

# def div_vowels(fun):
#     def inner_function(letters):
#         if letters == "a" or letters =="e" or letters =="i" or letters =="o" or letters == "u":
#             print(" letter is vowels ..!")
#         else:
#             print("Letter,s is consents.....")
#         return fun(letters)
#     return inner_function
#
#
# @div_vowels
# def vowels_checker(letter):
#     return letter
#
# display=vowels_checker('a')
# print(display)

# number validation check of use dect

#
# def Div_decortator(fun):
#     def inner_fun(x,y):
#         if  y == 0:
#             return "please give the proper values!"
#         return fun(x,y)
#     return  inner_fun
#
# @Div_decortator
#
# def div(a,b):
#     return a/b
# #
# # res=div(4,0)
# res=div(6,3)
# print(res)
#
# @Div_decortator
# def chk_cheak(a,b):
#     return  a /b
#
# result=chk_cheak(10,0)
# print(result)


# create a new Dectore function

# def Div_dectorator(fun):
#     def inner_functon(x,y):
#         if y == 0:
#             print("please ! give the proper values.....")
#         return fun(x,y)
#     return  inner_functon

# def Div_decortator(fun):
#     def inner_fun(x,y):
#         if  y == 0:
#             return "please give the proper values!"
#         return fun(x,y)
#     return  inner_fun
#
# @Div_decortator
# def check_valied(x,y):
#     return x / y
# result = check_valied(10,0)
# print(result)


# def create_deactor(fun):
#     def inner(x,y):
#         if y == 0:
#             print("please! proper values input ......")
#         return fun(x,y)
#
#     return inner
#
# @create_deactor
# def chk_number(x,y):
#     return x / y
# res=chk_number(10,2)
# print(res)

def decortor_chk(fun):
    def inner(x,y):
        if y == 0:
            return "please! give proper values !"
        return fun(x,y)
    return  inner

@decortor_chk
def division(a,b):
    return  a / b

res=division(10,0)
res1=division(10,2)
print(res)
print("==========")
print(res1)