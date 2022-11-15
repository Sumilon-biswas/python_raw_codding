# num1 = int(input("Input value :"))
# num2 = input("Input value 2")
# print(num1+num2)


# # try:
# #     # num1 = int(input("Input value :"))
# #     # num2 = int(input("Input value 2"))
# #     # print(num1+num2)
# # except:
# #     print("result is not found!")
#
# # def divide(x, y):
# #     try:
# #         # Floor Division : Gives only Fractional Part as Answer
# #         result = x // y
# #         print("Yeah ! Your answer is :", result)
# #     except ZeroDivisionError:
# #         print("Sorry ! You are dividing by zero ")
# #
# #
# # # Look at parameters and note the working of Program
# # divide(0, 2)
#
# # def divide(x, y):
# #     try:
# #         # Floor Division : Gives only Fractional Part as Answer
# #         result = x // y
# #         print("Yeah ! Your answer is :", result)
# #     except ZeroDivisionError:
# #         print("Sorry ! You are dividing by zero ")
# #
# #
# # # Look at parameters and note the working of Program
# # divide(3, 0)
# def sumation(x,y):

    #
    # try:
    #     res = x // y
    #     print("Yeah ! Your answer is :", res)
    #
    # except ZeroDivisionError:
    #
    #     print("Sorry ! You are dividing by zero ")

# try:
# #     number1=int(input("Input 01 :"))
# #     number2=int(input("Input 02:"))
# #     result = number1 / number2
# #     print(result)
# #
# # except ZeroDivisionError:
# #     print("Number 01 not divide of number2 ")


# def divided(x , y):
#     try:
#         result = int(x) // int(y)
#         print(result)
#         print("thanks for python")
#
#     except ValueError:
#         print("please! valided data type Input....")
#     except ZeroDivisionError:
#         print("You are dividing by zero ")
#     finally:
#         print("program run succesfully!")
#
# x =input("number 01:")
# y= input("number 02 :")
# divided(x,y)
#
# def multipalication(x,y):
#     try:
#
#         result = ((x+y)//(x-y))
#         print("this multpalication Result =",result)
#         print("thanks you python...!")
#
#     except ValueError:
#         print("please ! input valaid data.")
#     except ZeroDivisionError:
#         print("since,...... you are not divding  Zero")
#
#     finally:
#         print("program done.....")
#
# x =int(input("X :"))
# y=int(input("y :"))
# multipalication(x,y)


try:
    k = 5//0
    print(k)
except ZeroDivisionError:
    print("Can't divide  by Zero")
finally:
    print("all everything executed!")

