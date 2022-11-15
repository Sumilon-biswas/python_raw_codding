# import  random
# import math
#
# guss_input=int(input("guses the value 1 between 5 :"))
#
# print("guess value of ")
# guss_vaue=random.randint(1,5)
# print(guss_vaue)
# print(guss_vaue)
#
# if guss_input == guss_vaue:
#     print("You win the game!")
#     print(guss_vaue ,"and ",guss_input)
# else:
#     print("you loss the Game")
#
# num1=int(input("Input a num1 :"))
# num2= int(input("Input a num2 :"))
#
# if num1 > num2:
#     print("num1 is greater then num2")
# else:
#     print("num2 is greater then num1")

#short hand if__else and ternary operator

# num1=int(input("Input a num1 :"))
# num2= int(input("Input a num2 :"))
#
# Result= "num1 is greater then num2" if num1 > num2 else "num2 is greater then num1"
# print(Result)

# a=int(input("Enter the value of a :"))
# b=int(input("Enter the value of b :"))
#
# Result = "a is the greater then b" if a > b else "b is greater then a " if a < b else "both a and b is equal "
# print(Result)
#
# import  random
# import  math
#
# upper_bound=int(input("Input a uppor bound :"))
# lower_bound=int(input("Input a lower bound"))
#
# x=random.randint(lower_bound,upper_bound)
#
# count = 0
# while count <5:
#     count +=1
#     guess=int(input("Input a guess value :"))
#
#     if x == guess:
#         print("Congratulations you did it in  random =",x)
#
#     elif x > guess:
#         print("The guess value low or small")
#         print("guess value =",x)
#     elif x < guess:
#         print("the guess value hight or big ")
#         print("guess value =",x)
#     else:
#         print("both are known value....")
