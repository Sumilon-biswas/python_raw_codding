
# recursive function  is a function thats it self call .

"""

syntex of function

def recursive_fun_name():

      if condition():
          stop the recursive function condition

       else:

       recursivre function

"""
#
# def factorial(n):
#
#     if n == 1:
#         return 1
#     else:
#         return  n * factorial(n-1)
#
# print(factorial(5))

def count_down(starte):

    if starte == 1:
        return 1

    else:
        return  starte + count_down(starte-1)

print(count_down(4))




