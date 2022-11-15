
# mathicale program  n * (n+1) / 2

# n=20
# res=n*(n+1)/2
# print(res)
# avg=(n*(n+1)/2)/n
# print("averahge",avg)

# number_list=input("Input number of list")
# number=number_list.split()
#
#
# for i in  range(len(number)):
#      number[i]=int(number[i])
#
#
# res=sum(number)
# print("summation :",res)
# print("\n")
# avages=res/len(number)
# print("avages :",avages)

# number_list=input("please! number of input values :")
# numbers=number_list.split()
#
# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])
#
# print("summation of :",sum(numbers))
# print("    ")
# print("avages :",sum(numbers)/len(numbers))


# # martix program
#
# matrixOne = [[6,9,11],
#     [2 ,3,8]]
#
# matrixTwo = [[15,18,11],
#     [26,16,19]]
#
# result = [[0,0,0],
#          [0,0,0]]
#
# # First iterate rows
# for i in range(len(matrixOne)):
#    # Second iterate columns
#    for j in range(len(matrixOne[0])):
#        result[i][j] = matrixOne[i][j] + matrixTwo[i][j]
# print("Addition of two Matrix In Python")
# for res in result:
#    print(res)



# print("matrix program in pythons")

# x=[[12,7,5],
#    [7,8,6,9],
#    [6,9,10],
#    [7,8,9,10]]
#
# # print(x[0])
# # print(x[3])
# number_list=input("Input number list :")
# numbers=number_list.split()
# x.append(numbers)
# print(x)

# xx=[[1,2,3],[4,5,6],[7,8,9]]
#
# number_lst=input("Input number list :")
# numbers=number_lst.split()
# xx.append(numbers)
# print(xx)

# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
#
# print(len(X))
# print(len(Y))
# print(len(result))
#
# #iterator rows values
# for i in range(len(X)):
#     #iterator column values
#     for j in range(len(X[0])):
#         result[i][j]=X[i][j]+Y[i][j]
#
# for res in result:
#     print(result)

# Program to add two matrices using nested loop

# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]

# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
#
# # iterate through rows
# for i in range(len(X)):
#    # iterate through columns
#    for j in range(len(X[0])):
#        result[i][j] = X[i][j] + Y[i][j]
#
# for r in result:
#    print(r)

# #matrix
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[i][j]=X[i][j]+Y[i][j]
#
#
#
# for res in result:
#     print(res)


# #martix values Import
#
# maxtrix_1=[[23,34,10],
#            [25,27,28],
#            [30,56,60]]
# maxtrix_2=[[9,8,10],
#            [67,90,50],
#            [44,30,34]]
# result=[[0,0,0],
#         [0,0,0],
#         [0,0,0]]
#
# print(len(maxtrix_1))
# print(len(maxtrix_2))

# for i  in range(len(maxtrix_1)):
#     for j in range(len(maxtrix_1[0])):
#         result[i][j]=maxtrix_1[i][j]+maxtrix_2[i][j]

# for i  in range(len(maxtrix_1)):
#     for j in range(len(maxtrix_1[0])):
#         result[i][j]=maxtrix_1[i][j]-maxtrix_2[i][j]
#
# print("access the martix")
# for res in result:
#     print(res)

# x=[[2,3,8],
#    [5,6,8]]
# y=[[2,3,4],
#    [4,5,6]]
# display=[[0,0,0],
#          [0,0,0]
#          ]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         display[i][j]=x[i][j]*y[i][j]
#
# for res in display:
#     print(res)


# Python program for transpose of a matrix

# A = [[5, 4, 3],
#     [2, 4, 6],
#     [4, 7, 9],
#     [8, 1, 3]]
# # Define an empty matrix of reverse order
# transResult = [[0, 0, 0, 0],
#                [0, 0, 0, 0],
#                 [0, 0, 0, 0]]
# # Use nested for loop on matrix A
# for a in range(len(A)):
#    for b in range(len(A[0])):
#           transResult[b][a] = A[a][b] # store transpose result on empty matrix
# # Printing result in the output
# print("The transpose of matrix A is: ")
# for res in transResult:
#    print(res)

A = [[5, 4, 3],
    [2, 4, 6],
    [4, 7, 9],
    [8, 1, 3]]
# Define an empty matrix of reverse order
transResult = [[0, 0, 0, 0],
               [0, 0, 0, 0],
                [0, 0, 0, 0]]

for a in range(len(A)):
   for b in range(len(A[0])):
          transResult[b][a] = A[a][b] # store transpose result on empty matrix

for res in transResult:
    print(res)
