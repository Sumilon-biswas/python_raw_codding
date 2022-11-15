
#problem should below and decribes

# input = interger n
# input(boolean) value =True or false
#
# if boolean =True
# *
# **
# ***
# ****
# *****
#
# or boolean =False
# *****
# ****
# ***
# **
# *

# rows=int(input("Input a rows values :"))
#
# bool_value=input("Input a boolean value :")
#
# if bool_value == "true":
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print("* ", end=" ")
#
#         print(" ")
# else:
#     for i in range(rows, 0, -1):
#         for j in range(i, 0, -1):
#             print("* ", end=" ")
#
#         print("\r")

# print("Enter no. of rows of your choice")
# n = int(input(""))
# print("Enter 1 for increasing pattern and 0 for decreasing pattern of stars")
# m = bool(int(input("")))
# if m == True:
#     for i in range(1,n+1):
#         print("*" * i)
#
# else:
#     for i in range(0,n):
#         print("*" * (n-i))

#problem should below and decribes

# input = interger n
# input(boolean) value =True or false
#
# if boolean =True
# *
# **
# ***
# ****
# *****
#
# or boolean =False
# *****
# ****
# ***
# **
# *

# rows=int(input("Enter you of rows of you choose :"))
# print("Input boolean value ,press 1=true or 0 =false :")
# m=bool(int(input()))
# if m == True:
#     for i in range(1,rows+1):
#         for j in range(1,i+1):
#             print("* ",end=" ")
#
#         print("\r")
# # when Input false value display below"
# else:
#     for i in range(rows,0,-1):
#         for j in  range(i,0,-1):
#             print("* ",end=" ")
#         print(" ")

# this patten program solve
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# rows=int(input("Input the rows value :"))
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print(" ")
#
# r = int(input("Input the rows value :"))
#
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print(" ")

# again pattren problem below
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# rows=int(input("Input a rows value :"))
#
# for i in range(1,rows+1):
#     for j in  range(1,i+1):
#         print(j,end=" ")
#     print(" ")
# #pattren problem solve
#
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# row = int(input("Input  rows value :"))
# b= 0
# for i in range(row,0,-1):
#     b +=1
#     for j in range(i,0,-1):
#         print(b, end=" ")
#
#     print(" ")

# rows=int(input("input rows value :"))
# b = 0
# for i in range(rows,0,-1):
#     b +=1
#     for j in range(i,0,-1):
#         print(b,end=" ")
#     print(" ")

# another pattren problem

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

rows=int(input("Enter number of rows :"))

for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print(" ")









