#ternary operator

# a=int(input("Input value a :"))
# b= int(input("Input value b :"))
#
# result = a if a > b else b
# print("Result is ",result)
#
# age=int(input("input age :"))
#
# voter = "you are voted person!" if age >= 18 else "you are not voted person"
#
# print(voter)

#Ternary operator can be written as nested if-else:

# a =30
# b =30
# result = "both a and b is equal ==" if a == b else  "a is greater the b " if a > b else "b is the greater then a"
# print(result)

# friend_list =["sumilon","tanbir","sagor","summon","Ripon"]
# name_in=input("Input name list :")
#
#
# result = "sumilon is student of CSE" if name_in in friend_list else "Tanbir islam is bussiness man." if name_in in friend_list else "other name is included"
#
# print(result)

# person =["sumilon","tanbir","john","karim","Rahman"]
#
# In_name = input("Input a person name :")
#
# result = "person is in the list" if In_name == person else "person  name not included her"
# print(result)


a=9
b=7

result = (a,"a is the greater then b") if a > b else (b, "b is a greater then a")

print(result)