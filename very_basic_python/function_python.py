
# structured : function
"""
def=define
"""
#
# def math(opa,a,b):
#
#     if opa =="+":
#         return (f"addition ={a}+{b}={a+b}")
#     elif opa == "-":
#         return (f"substraction ={a}-{b}={a-b}")
#     elif opa == "*":
#         return (f"multipalication ={a}*{b} ={a*b}")
#     elif opa == "/":
#         return (f"division = {a}+{b}={a/b}")
#     elif opa == "%":
#         return (f"modulation ={a}%{b}={a%b}")
#     elif opa=="//":
#         return (f"intger foolor {a}//{b}={a//b}")
#
#     else:
#         return ("Please ! create operator selected !")
#
#
# while True:
#     num1 = int(input("Input value a="))
#     operator = input("Inputa a  operator =")
#     num2 = int(input("Input value b="))
#
#     if operator == '':
#         break
#     else:
#        print(math(operator,num1,num2))


def math(*number):
    print(number)

# math(34,34,44,5,66,77)
print(type(math(23,5,5,6,8)))


