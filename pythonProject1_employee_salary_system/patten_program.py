
"""

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

# rows=int(input("input rosws ="))
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("\r")

"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

"""
# rows=int(input("Inputs rows values ="))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")

# rows=int(input("Input rows values ="))
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")

"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

# """
# rows=int(input("Input a rows values ="))
# b=0
# for i in range(rows,0,-1):
#     b +=1
#     for j in range(i,0,-1):
#         print(b,end=" ")
#     print(" ")

"""
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
"""
# rows=int(input("Inputs rows values :"))
#
# num=rows
#
#
# for i in range(rows,0,-1):
#     for j in range(i,0,-1):
#         print(num,end=" ")
#     print(" ")


"""
5 5 5 5 5  
6 6 6 6  
7 7 7  
8 8  
9  
"""
#
# rows=int(input("Inputs rows values :"))
# num=rows
# for i in range(rows,0,-1):
#     for j in range(i,0,-1):
#         print(num,end=' ')
#     num +=1
#     print(" ")

"""
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
"""

# rows=int(input("Inputs value of rows ="))

# for i in range(rows,0,-1):
#     for j in range(0,i+1):
#         print(j,end=" ")
#     print(" \r")

"""
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
"""
# rows=5
# i=1
# while i <= rows:
#     j =1
#     while j <= i:
#         print(i*2-1,end=" ")
#         j+=1
#     i+=1
#     print(" ")

# rows=5
# i=1
# while i <=rows:
#     j = 1
#     while j <= i:
#         print(i*2-1,end=" ")
#         j +=1
#     i +=1
#     print(" ")

#Example:-07

"""
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
"""
# rows=int(input("Input rows values :"))
#
# for i in range(rows,0,-1):
#     num=i
#     for j in range(0,i):
#         print(num,end=' ')
#     print(" ")

# rows=int(input("Inputs rows values :"))
# for i in range(rows,0,-1):
#     num=i
#     for j in range(0,i):
#         print(num,end=" ")
#     print(' ')


#example:-04

"""
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1

"""

# rows=int(input("Inputs rows values = "))
#
# for i in range(1,rows+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print(" ")


#example :-06

"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

"""

# rows=int(input("Input rows values = "))

# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")

# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")

#Example :-08

"""
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
"""

# row=5
# for i in range(1,row):
#     num=1
#     for j in range(row,0,-1):
#         if j>i:
#             print(" ",end=" ")
#         else:
#             print(num,end=" ")
#             num +=1
#     print(" ")
"""
        1  
      1 2  
    1 2 3  
  1 2 3 4  
"""

# rows=int(input("Inputs rows values ="))
#
# for  i in range(1,rows):
#     num=1
#     for j in range(rows,0,-1):
#         if j > i:
#             print(" ",end=" ")
#         else:
#             print(num,end=" ")
#             num +=1
#     print(' ')

#Example:-07 squared
"""
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5

"""
# rows=int(input("Inputs rows values :"))

# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if j <= i:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#     print(" ")

# rows=int(input("Inputs rows values ="))
#
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if j <=i:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#     print(" ")

"""
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
"""

rows=int(input("Inputs rows values :"))


for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print(" ")