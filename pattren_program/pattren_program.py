

#output

# *
# * *
# * * *
# * * * *
# * * * * *

# rows= int(input("Enter you rows values :"))
#
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*", end=" ")
#     print("\r")


#pattern -02

# output
#        *
#       * *
#     * * *
#   * * * *
# * * * * *

# rows=int(input("enter your rows values :"))
#
# k= 2 * rows -2
#
# for i in range(0,rows):
#
#     for j in range(0,k):
#
#         print(end=" ")
#
#     k=k-2
#
#     for j in range(0,i+1):
#         print("*",end=" ")
#
#     print("\r")

# pattren = 03

# * * * * *
# * * * *
# * * *
# * *
# *

# rows=int(input("Enter your rows :"))
#
# for i in range(rows+1,0,-1):
#     for j in  range(i,0,-1):
#         print("*",end=" ")
#     print("\r")

# pattren = 04
#
#         * * * * * *
#          * * * * *
#           * * * *
#            * * *
#             * *
#              *

# rows=int(input("Enter you rows values :"))
# k= 2 * rows -2
#
# for i in range(rows,-1,-1):
#
#     for j in range(k,0,-1):
#         print(end=" ")
#
#     k=k+1
#     for j in range(i,-1,-1):
#         print("*",end=" ")
#
#     print("\r")

#patteren=04

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *


# Rows=int(input("Enter your rows value :"))
#
# k=(2*Rows)-2
#
# for i in range(0,Rows):
#     for j in  range(0,k):
#         print(end=" ")
#     k=k-1
#     for a in range(0,i):
#         print("*",end=" ")
#
#     print("\r")
#
# rows=int(input("enter your Rows value :"))
# k=(2*rows)-2
#
# for i in range(rows,0,-1):
#     for j in range(0,k):
#         print(end=" ")
#     k=k-1
#     for a in range(0,i):
#         print("*",end=" ")
#
#     print("\r")


# patteren program

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
#
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# rows=int(input("Enter your rows number "))
#
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print("\r")
#
# print("")
# for i in range(rows,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print("\r")

# pattren

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# rows=int(input("Input a rows values"))
#
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print("\r")
# for i in range(rows,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print("\r")

#pattren program another

#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
# #     * *
#         *


# rows = 5
# i = 1
# while i <= rows:
#     j = i
#     while j < rows:
#         print(' ',end=' ')
#         j=j+1
#     k=1
#     while k <= i:
#         print("*",end=" ")
#         k=k+1
#     print("\r")
#     i += 1
# i = rows
# while i >= 1:
#     j = i
#     while j <= rows:
#         print(' ', end=' ')
#         j += 1
#     k = 1
#     while k < i:
#         print('*', end=' ')
#         k += 1
#     print('')
#     i -= 1


# rows = 5
# i = 1
# while i <= rows:
#     j = i
#     while j < rows:
#         print(' ',end=' ')
#         j=j+1
#     k=1
#     while k <= i:
#         print("*",end=" ")
#         k=k+1
#     print("\r")
#     i += 1

# row = 5
# i = 1
# while i <= row:
#     j =i
#     while j < rows:
#         print(' ',end=' ')
#         j+=1
#     k = 1
#     while k <= i:
#         print("*",end=" ")
#         k=k+1
#     print("\r")
#     i +=1
#
# i=row
# while i >= 1:
#     j=i
#     while j < row:
#         print(" ",end=" ")
#         j +=1
#     k=1
#     while k <= i:
#         print("*",end=" ")
#         k +=1
#
#     print(" ")
#     i -=1

'''

        *
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *

# '''
#
# rows=5
# i=1
# while i <=rows:
#     j = i
#     while j < rows:
#         print(' ',end= ' ')
#         j +=1
#     k=1
#     while k <= i:
#         print("*",end=" ")
#         k +=1
#     print(" ")
#     i +=1
# i=rows
# while i >= 1:
#     j=i
#     while j < rows:
#         print(" ",end=" ")
#         j +=1
#     k=1
#     while k <= i:
#         print("*",end=" ")
#         k +=1
#
#     print(" ")
#     i -=1


#pattren program
'''
 * * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

'''
#
# rows = 5
# i = 0
# while i <= rows - 1:
#     j = 0
#     while j < i:
#         # display space
#         print('', end=' ')
#         j += 1
#     k = i
#     while k <= rows - 1:
#         print('*', end=' ')
#         k += 1
#     print()
#     i += 1
# i = rows - 1
# while i >= 0:
#     j = 0
#     while j < i:
#         print('', end=' ')
#         j += 1
#     k = i
#     while k <= rows - 1:
#         print('*', end=' ')
#         k += 1
#     print('')
#     i -= 1

'''
 * * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

'''

# rows = 5
# i = 0
# while i <= rows - 1:
#     j = 0
#     while j < i:
#         # display space
#         print('', end=' ')
#         j += 1
#     k = i
#     while k <= rows - 1:
#         print('*', end=' ')
#         k += 1
#     print()
#     i += 1



# rows=10
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j*i,end=" ")
#     print()
#

'''
  
  Output

Enter number 10
Sum of first  10 numbers is:  55
Average of  10 numbers is:  5.5

'''

# n = int(input("Enter input n valueds"))
#
# sum=0
# avg=0
# for i in range(1,n+1,1):
#     sum=sum+i
# print("Total summation of ",sum)
# avg=sum/n
# print("Total avgarages :",avg)


# n=10
# res=sum(range(1,n+1,1))
# print("Result is",res)

# num_list = [10, 20.5, 30, 45.5, 50]
#
# result=sum(num_list)
# print("list of summation of ",result)
# avg=result/len(num_list)
# print("avager age :",avg)

# my_list=[20,40,60,70,78,80]
#
# res=sum(my_list)
# print("result is ",res)
# avg=res/len(my_list)
# print("avagerages",avg)



