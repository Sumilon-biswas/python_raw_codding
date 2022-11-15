#
# def calculator_fun(operator,x,y):
#     result=0
#     if operator == '+':
#       result =x+y
#       return  result
#     elif operator == '-':
#         result =x-y
#         return result
#     elif operator == '*':
#         result = x * y
#         return result
#     elif operator == '/':
#         result = x / y
#         return result
#     elif operator == '//':
#         result = x  // y
#         return result
#     elif operator == '%':
#         result = x % y
#         return result
#     else:
#         result ="plesase ! select any operator "
#
#     print("Result is :",result)
#
# print(calculator_fun('',10,10))



# def calculator_fun(operator,x,y):
#
#     if operator == '+':
#       return  x+y
#     elif operator == '-':
#         return x-y
#     elif operator == '*':
#         return  x * y
#     elif operator == '/':
#         return  x / y
#     elif operator == '//':
#         return x  // y
#     elif operator == '%':
#         return x % y
#     else:
#         result ="plesase ! select any operator "
#
# print(calculator_fun('/',10,10))

#function create and function defination
def calculator_fun(operator,x,y):

    if operator == '+':
      return  x+y
    elif operator == '-':
        return x-y
    elif operator == '*':
        return  x * y
    elif operator == '/':
        return  x / y
    elif operator == '//':
        return x  // y
    elif operator == '%':
        return x % y
    else:
        result ="plesase ! select any operator "

# user input
operator=input("Input a arithmatices opearator like +,-,*,/,//,% :")
number_1=int(input("Input number_1 values :"))
numbewr_2=int(input("Input number_2 values :"))

# function calling
print(calculator_fun(operator,number_1,numbewr_2))

