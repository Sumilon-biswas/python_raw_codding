#
# n=int(input("Input enter your n :"))
# i=1
# while i <= n:
#     print(i)
#     i +=1
#
# print("wellocome program")

'''

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

'''

# rows=int(input("Enter your values n:"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(' ')


''''
 Enter number 10
Sum is:  55
'''

# n=int(input("Input user Input values :"))
# sum=0
# for i in range(1,n+1):
#     # sum=n*(n+1)/2
#     sum=sum+i
# avg=sum/n
# print("sum =",sum)
# print(avg)

'''
  Enter Number :10
  sum is: 55
'''

# sum=0
# n=int(input("Enter INput values :"))
#
# for i in range(1,n+1,1):
#     sum +=i
#
#
# print("sum =",sum)
#
#
# sum=0
# n=int(input("Enter your Input :"))
#
# for i in range(1,n+1,1):
#     sum +=i
#
# print("sum =",sum)


# '''
#  Even serise number printed
# '''
# for i in range(2,20+1,2):
#     print(i)


'''
numbers = [12, 75, 150, 180, 145, 525, 50]
# '''
# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for item in numbers:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     elif item % 5 ==0:
#         print(item)
#

'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''
# rows=int(input("Enter INoput vaues :"))
#
# for i in range(rows,1,-1):
#     for j in range(i+1,1,-1):
#         print(j,end=" ")
#     print(" ")
# rows=int(input("Enter Input values :"))
# for i in range(rows,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print(" ")


'''
list1 = [10, 20, 30, 40, 50]

output::
50
40
30
20
10

'''
# list1 = [10, 20, 30, 40, 50]
# new_list=reversed(list1)
#
# for i in new_list:
#     print(i)


# lsit_1=[20,4,80,55,23,9,1, 60,40,25]
#
# lsit_1.sort()
# print(lsit_1)

# numbers=[20,4,5,10,17,19,35,25,40,2,1,3]
#
# numbers.sort()
# print(numbers)

# # vowels list
# vowels = ['e', 'a', 'u', 'o', 'i']
#
# # sort the vowels
# vowels.sort(reverse=False)
# print("ascending or descending :",vowels)

# list_1=[9,10,6,20,80,40,11,40]
#
# list_1.sort(reverse=False)
# print("Ascending list =",list_1)
#
# list_1.sort(reverse=True)
# print("descending list =",list_1)

# sorting using custom key
# Employees = [
#     {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
#     {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
#     {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
#     {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
# ]

#
# def get_name(employee):
#     return  employee.get('Name')
#
# Employees.sort(key =get_name)
# print(Employees)

# def get_age(emp_age):
#     return  emp_age.get('age')
#
# Employees.sort(key=get_age)
# print(Employees)

'''
input
input values =6

output is
Current Number is : 1  and the cube is 1
Current Number is : 2  and the cube is 8
Current Number is : 3  and the cube is 27
Current Number is : 4  and the cube is 64
Current Number is : 5  and the cube is 125
Current Number is : 6  and the cube is 216
'''

# input_values=int(input("Input values :"))
# sum=0
# for i in range(1,input_values+1):
#     print(f"current number is :{i} and the cube is ={i*i*i} ")
#     sum=sum+i*i*i
#
# print("summation of :",sum)
# numbers=int(input("Input a number values :"))
# sum=0
#
# for i in range(1,numbers+1):
#     print(f"Current number is ={i}  and clube values ={i*i*i}")
#     sum=sum=i*i*i
#
# print("summation of :",sum)


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

'''

# rows =int(input("Input rows values :"))
#
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print(" ")
# for i in  range(rows,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=' ')
#     print(" ")

rows=int(input("Input rows values :"))
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print(" ")
