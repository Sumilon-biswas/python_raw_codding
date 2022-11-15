#
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5
# rows = int(input("Input a rows value :"))
#
# #outer loop
# for i in range(rows+1):
#      for j in range(1,i+1):
#          print(i, end='')
#      print("  ")
 # this patten show alphabet letter

#  #outer loop and declare  rowas
# for i in range(5+1):
#     #inner loop
#     for j in  range(1,i+1):
#         print("A",end=" ")
#     print(" ")

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n = int(input("Enter value n :"))
#
# # number of spaces
# k = n - 1
#
# # outer loop to handle number of rows
# for i in range(0, n):
#
#     # inner loop to handle number spaces
#     # values changing acc. to requirement
#     for j in range(0, k):
#         print(end=" ")
#
#     # decrementing k after each loop
#     k = k - 1
#
#     # inner loop to handle number of columns
#     # values changing acc. to outer loop
#     for j in range(0, i + 1):
#         # printing stars
#         print("* ", end="")
#
#     # ending line after each row
#     print("\r")

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *

# #declar the rows
# n = int(input("Enter value n :"))
#
# #declar the speaces value
# k = n-1
#
# #decalre outer loop
# for i in  range(0,n):
#     # speases inner loop
#     for j in range(0,k):
#         print(end=" ")
#     k = k -1
#     for i in range(0,i+1):
#         print(" * " ,end="")
#
#     print("\r")

n = int(input("Enter value of n:"))
k= n-1
for i in range(0,n):

    for j in range(0,k):
        print(end=" ")

    k= k-1

    for g in range(0,i+1):
        print("* ",end="")

    print(" ")











