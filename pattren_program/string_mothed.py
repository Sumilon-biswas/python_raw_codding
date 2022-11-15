
# help(print)
#
# def myfunction(a,b):
#     # two number addition of it's
#     return  a + b
#
# help(myfunction)
#
# # def add(a, b):
# #     "Return the sum of two arguments"
# #     return a + b
# # help(add)
#
# # def add(a, b):
# #     """ Add two arguments
# #     Arguments:
# #         a: an integer
# #         b: an integer
# #     Returns:
# #         The sum of the two arguments
# #     """
# #     return a + b
# #
# # add.__doc__
#
# # i=1
# # j=1
# # while i<=4:
# #     while j <= 3:
# #         print("i =",i,"j=",j,sep=" ")
# #         j +=1
# #     else:
# #         print("j is end ...!")
# #     i+=1
# #     j=1
#
# # i=1
# # j=1
# # while i <= 10:
# #     while j <= 10:
# #         print(f"{i}*{j}={i*j}")
# #         j+=1
# #     else:
# #         print("j is end...")
# #     i +=1
# #     j=1
#
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}*{j}= {i*j}",sep=" ")
#     print(f"name of namta is {i} ")
#     print(' ')

# for i in range(1,11,3):
#     print(i)
#
# print("printed of serial number")
#
#
# for i in range(5):
#     print(i)

# for i in range(2,5):
#     print(i)
#
# a="Bangladesh"
# for i in a:
#     print(i)


# martix Row and column display

# for i in range(5):
#     for j in range(4):
#         print("row =",i,"col =",j,end=" ")
#     print(' ')

# for i in range(5):
#     for j in range(4):
#         print("row =",i,"col=",j,end=" ")
#     print(" ")

# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col% 3 ==0)or (row-col==2) or (row+col==8):
#             print(" +",end=" ")
#         else:
#             print(" ",end=" ")
#     print(" ")

# for row  in range(6):
#     for col in range(7):
#         if (row ==0 and col % 3 !=0) or (row == 1 and col % 3 ==0) or (row -col ==2) or (row+col == 8):
#             print("+",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#
# for row in range(6):
#     for col in range(7):
#         if (row==0 and col % 3!=0) or (row==1 and col %3 ==0) or (row-col==2)or (row+col==8):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# row=int(input("Inputs rows values :"))
# k=2*row-2
#
# for i in range(row):
#     for j in range(0,row-i-1):
#         print(end=" ")
#     for l in range(0,i+1):
#         print("*",end=" ")
#     print(" ")


#continue ,Break ,pass

# i=1
# while i <= 5:
#     if i == 3:
#         continue
#     print(i)
#     i +=1

# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i)
#
# for k in  range(1,6):
#     if k==3:
#         continue
#     print(k)

# a = 10
# a = None
# print(a)
# b=None
# print(b)
# print(type(b))

# string type of data

# a="Dhaka"
# print(a)
# print(type(a))
#
# b="""
#   I love in dhaka .
#   it's a population city in the world,
#   majority of person student and job holder live in dhaka.
# """
# print(b)


#postive Index

# a="Bangladesh"
# print(a)
# print(a[7])
# print(a[:8])
# print(a[::2])
# print(a[2:6])
#
# #negative Index
#
# b="Bangladesh"
# print(b[-2])
# print(b[::3])

# a="Doremon is my favourite Cartoon"
# print(a.find("is"))
# print(a.find("Is"))
# print(a.find("a"))
# print(a.find("C"))

# a="Rakib"
# print(a.center(20))
# aa="Ban"
# print(a.center(20,"+"))
# mass="Ban"
# print(mass.center(30,"*"))

# a="mina is my favorite cartoon"
#
# print(a.partition("my"))
#
# b="sumilon biswas anik is good student of dhaka international"
# print(b.partition("is"))
#
# aa="Dhaka is big city"
# print(aa.partition("is"))

#swapecase

# a="mina IS my FavoRites"
# print(a.swapcase())

#endwith() and startewith()

# a="I live in Dhaka"
# print(a.endswith("Dhaka"))
# # print(a.endswith("dhaka"))
# a="I live in dhaka"
# print(a.startswith("I"))
# print(a.startswith("a"))

# replase

# fr="joya  is  good boy "
# print(fr.replace("bad","good"))

# fr="thanbir islam is bussunman "
# print(fr.replace("bussunman","student"))

