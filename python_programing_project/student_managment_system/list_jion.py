# my_list = ['p', 'q']
# new=[]
# n=5
# for i in range(1,n+1):
#     p=str(my_list[0]+str(i))
#     q=str(my_list[1]+str(i))
#
#     new.extend([p,q])
# print(new)

# my_list=['p','q']
# new=[]
# n=5
# for i in range(1,n+1):
#     p=str(my_list[0]+str(i))
#     q=str(my_list[1]+str(i))
#
#     new.extend([p,q])
#
# print(new)
#
# mylist=['p','q']
# new=[]
# n=7
# for i in range(1,n+1):
#     p=str(mylist[0]+str(i))
#     q=str(mylist[1]+str(i))
#     new.extend([p,q])
# print(new)

# string="hello world"
# list1=slice(3)
# list2=slice(1,9,2)
# print(string[list1])
# print(string[list2]

# letter="Bangladesh"
# print("postive index")
# print(letter[0])
# print(letter[2])
# print("negative index ")
# print(letter[-1])

#Exercise 1: Calculate the multiplication and sum of two numbers

# number1=20
# number2=30
# print(number1 * number2)
#
# num1=40
# num2=30
# print(num1+num2)

#problem 2

# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number  0  Sum:  0
# Current Number 1 Previous Number  0  Sum:  1
# Current Number 2 Previous Number  1  Sum:  3
# Current Number 3 Previous Number  2  Sum:  5
# Current Number 4 Previous Number  3  Sum:  7
# Current Number 5 Previous Number  4  Sum:  9
# Current Number 6 Previous Number  5  Sum:  11
# Current Number 7 Previous Number  6  Sum:  13
# Current Number 8 Previous Number  7  Sum:  15
# Current Number 9 Previous Number  8  Sum:  17
#
# previous_num=0
#
# for i  in range(1,11):
#     x_sum=previous_num+1
#     print(f"current number {i} previous number :{previous_num} sum :{x_sum}")
#     previous_num=i

# previous_num=0
# for i in range(1,11):
#     sum=previous_num+1
#     print(f" current number :{i} previous number :{previous_num} sum :{sum}")
#     previous_num=i

#problem :-3

# str="pynative"
#
# for i in str:
#     print(i)

# iven list: [10, 20, 30, 40, 10]
# result is True
#
# numbers_y = [75, 65, 35, 75, 30]
# result is False
#
# def  boolean_checaking(numberlist):
#     print("Give sume number list",numberlist)
#
#     frist_number=numberlist[0]
#     second_number=numberlist[-1]
#
#     if frist_number == second_number:
#         return  True
#     else:
#         return  False
#
# list1=[10, 20, 30, 40, 10]
# result =boolean_checaking(list1)
# print(result)
#
# list2=[75, 65, 35, 75, 30]
# res=boolean_checaking(list2)
# print(res)

# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55

# list1=[10,20,33,46,55]
# print("Give list",list1)
# print("Divisible by 5")
#
# for i in list1:
#     if i % 5 == 0:
#         print(i)

# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5 not equal zero

# mylist=[10,20,33,46,55]
# print("result is divide not equal zero ")
#
# for i in  mylist:
#     if i % 5 !=0:
#         print(i)

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

# rows=int(input("Input rows values :"))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("\t")

# def palindrome(number):
#     print("original number", number)
#     original_num = number
#
#     # reverse the given number
#     reverse_num = 0
#     while number > 0:
#         reminder = number % 10
#         reverse_num = (reverse_num * 10) + reminder
#         number = number // 10
#
#
#     # check numbers
#     if original_num == reverse_num:
#         print("Given number palindrome")
#     else:
#         print("Given number is not palindrome")
#
#
# palindrome(121)
# palindrome(125)
# palindrome(121)
# palindrome(125)

#
# def palidrom()