# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

 #Number=01 pattern

# rows=int(input("Input number of rows :"))
#
# for i in range(rows+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("\r")

#number 02 :
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# rows= int(input("INput number of rows :"))
# for i in range(0,rows):
#
#     for j in range(1,i+1):
#         print(j,end=" ")
#
#     print("\r")

#number 03

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# row=int(input("Input number of  row : "))
#
# b= 0
#
# for i in range(row,0,-1):
#     b +=1
#     for j in range(1,i+1):
#         print(b , end=" ")
#     print("\r")

# rows=int(input("Input number of rows :"))
# b = 0
#
# for i in range(rows,0,-1):
#     b += 1
#     for j in range(1,i+1):
#         print(b,end=" ")
#
#     print("\r")

#patten no :03
#
# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5

# rows=5
# num =rows
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#
#     print("\r")

# parrten number =03

# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1

# rows=int(input("Input number of rose :"))
#
# for i in range(rows,0,-1):
#
#     for j in range(0,i+1):
#         print(j ,end=" ")
#
#     print(" ")

# rows=int(input("Input number of  rows :"))


# for i in range( rows,0,-1):
#
#     for j in range(0,i+1):
#         print(j,end=" ")
#     print("\r")

# pattern : 04 using loop while

# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9

#using while loop

# rows=int(input("Input number of rows"))
#
# i=1
# while i <= rows:
#     j =1
#     while j <= i:
#         print((i * 2 -1),end=" ")
#         j+=1
#     i +=1
#     print("\r")

# rows=5
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print((i*2-1),end=" ")
#     print("\r")

# pattern :05
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# rows= int(input("Input number of rows :"))
# for i in range(rows,0,-1):
#     num=i
#     for i in range(1,i+1):
#         print(num,end=" ")
#     print(" ")

# rows=int(input("Input number of rows:"))
#
# for i in range(rows,0,-1):
#     num=i
#     for j in range(1,i+1):
#         print(num,end=" ")
#
#     print("\r")

#Reverse Pyramid of Numbers

# rows=int(input("Enter number of rows"))
#
# for i in range(1,rows):
#     for j in range(i,0 ,-1):
#         print(j,end=" ")
#     print("\r")

# rows= int(input("Input number of rows values"))
#
# for i in range(1,rows):
#     for j in range(i,0,-1):
#         print(j,end= " ")
#     print("\r")


#pattren program
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# rows=int(input("Input a number of rows  :"))
#
# for i in range(0,rows):
#     for j in  range(1,i+1):
#         print(i, end=" ")
#
#     print(" ")

#Example 02

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# rows=int(input("Input a number of rows : "))
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print(" ")
#
# Example  03:
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# rows=int(input("Input number of rows :"))
# b=0
# for i in range(rows,0,-1):
#     b +=1
#     for j in range(1,i+1,1):
#         print(b, end=" ")
#     print("  ")

#Example :03

# 5 5 5 5 5
# # 5 5 5 5
# # 5 5 5
# # 5 5
# # 5

# rows=int(input("Input number of rows :"))
# num = rows
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#print(" ")

#Example  :04

# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

# rows=int(input("Input number of rows :"))
#
# for i in range(0,rows):
#     for  j in range(0,i+1):
#         print(j, end=" ")
#     print(" ")
#
# print("==================")
# #Example :04
#
# #
# # 0 1 2 3 4 5
# # 0 1 2 3 4
# # 0 1 2 3
# # 0 1 2
# # 0 1
#
# row=int(input("Input number of rows :"))
#
# for i in range(row,0,-1):
#     for j in  range(0,i):
#         print(j, end=" ")
#     print(" ")


# Example =05
#
# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9

#  for loop use kora

# rows=int(input("Input number of rows :"))
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(i * 2 -1,end=" ")
#     print(" ")

# while loop use kora
# various program
# rows = int(input("number of rows :"))
# i = 1
# while i <= rows:
#     j = 1
#     while j <= i:
#         print((i * 2-1),end=" ")
#        j +=1
# i+=1
# print(" ")

# rows = int(input("number of rows :"))
# i = 1
# while i <= rows:
#      j = 1
#      while j <= i:
#         print((i * 2-1),end=" ")
#         j +=1
#      i+=1
#      print(" ")

# rows=int(input("Input number of rows :"))
# i=1
# while i <= rows:
#     j = 1
#     while j <= i:
#         print((i*2-1),end=" ")
#         j +=1
#     i +=1
#     print(" ")

#example :06
#Reverse number pattern
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# rows=int(input("Number of raws:"))
# for i in range(rows,0,-1):
#     num=i
#     for j in  range(0,i):
#         print(num,end=" ")
#     print(" ")

#example 0f  :04
#Reverse Pyramid of Numbers
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
#
# rows=int(input("number of rows :"))
# for i in range(1,rows+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print(" ")

#example of :06
#Reverse Pyramid of Numbers
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
#
# rows=int(input("number pf rows :"))
# for i in range(0,rows):
#     for j in range(rows-i, 0,-1):
#         print(j,end=" ")
#     print(" ")

#example of:10
#Print reverse number from 10 to 1

# 1
# 3 2
# 6 5 4
# 10 9 8 7

# start =1
# stop = 2
# current_num=stop
#
# for rows in range(2,6):
#     for col in range(start,stop):
#         current_num -= 1
#         print(current_num,end=" ")
#     print(" ")
#     start = stop
#     stop +=rows
#     current_num = stop

#
# start = 1
# stop = 2
# current_num = stop
#
# for rows in range(2,6):
#     for col in range(start,stop):
#         current_num -= 1
#         print(current_num,end=" ")
#     print(" ")
#     start =stop
#     stop +=rows
#     current_num =stop

#wxample of:11
#Number triangle pattern Right
#output:
#           1
#         1 2
#       1 2 3
#     1 2 3 4
#   1 2 3 4 5
# Program: –

# rows=int(input("Input number value :"))
#
# for i in range(1,rows):
#     num = 1
#     for j in range(rows,0,-1):
#         if j > i:
#             print(" ",end=" ")
#         else:
#             print(num,end=" ")
#             num +=1
#     print(" ")

#output:
#           1
#         1 2
#       1 2 3
#     1 2 3 4
#   1 2 3 4 5

# for i in range(1,rows+1):
#     num=1
#     for j in range(rows,0,-1):
#         if j > i :
#             print(" ",end=" ")
#         else:
#             print(num,end=" ")
#             num +=1
#     print(" ")


#Example 11

#squard program

#output
# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

# rows=int(input("Input number value :"))
# for i in range(1, rows+1):
#     for j in range(1,rows+1):
#         if j <= i:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#     print("\r")

# rows=int(input("Input number value :"))
# for i in range(1,rows +1):
#     for j in range(1,rows+1,):
#         if j <= i:
#             print(i,end=" ")
#         else:
#             print(j ,end=" ")
#     print(" ")

#example of = 12
#Multiplication table pattern
# below output::
# 1
# 2  4
# 3  6  9
# 4  8  12  16
# 5  10  15  20  25
# 6  12  18  24  30  36
# 7  14  21  28  35  42  49
# 8  16  24  32  40  48  56  64

# rows=int(input("Number of colmun :"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         squard = i * j
#         print(squard,end=" ")
#
#     print(" ")

rows=int(input("number of rows Input :"))

for i in range(1,rows+1):
    for j in range(1,i+1):
        squard=i * j
        print(squard,end=" ")
    print(" ")


