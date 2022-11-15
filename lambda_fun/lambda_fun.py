
# x=(lambda a,b:a*b+2*a*b+b*b)(2,3)
# print(x)
#
# print((lambda a,b:a*a+2*a*b+b*b)(4,5))
#
# str1="GreekforGreeks"
#
# rev_upper = lambda string: string.upper()[::-1]
# print(rev_upper(str1))

# str="sumilon biswas anik"
# rev_uppor= lambda string:string.upper()[::-1]
# print(rev_uppor(str))

# str="python is awasome languages "
#
# rev_upppor=lambda  string:string.upper()[::-1]
# print(rev_upppor(str))

# lambda_cube=lambda y:y*y*y
# print(lambda_cube(5))

# series_number=[lambda age=i:age*10 for i in range(1,6)]
#
# for x in series_number:
#     print(x())

# series_num=[lambda x=i:x*10 for i in range(1,5)]
#
# for item in series_num:
#     print(item())

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# #
# # odd_num=list(filter(lambda a :(a  % 2 !=0),li))
# # print(odd_num)
# even_num=list(filter(lambda a:(a%2 ==0),li),)
# print(even_num)


# # Python 3 code to people above 18 yrs
# ages = [13, 90, 17, 59, 21, 60, 5]
#
#
# adults=list(filter(lambda ages:ages >=18,ages))
# print(adults)
#
# nonAdults=list(filter(lambda ages:ages < 18,ages))
# print(nonAdults)



# Python code to illustrate
# map() with lambda()
# # to get double of a list.
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#
# double_list=list(map(lambda x:x*2,li))
# print(double_list)
#
# mul_list=list(map(lambda x:x*3,li))
# print(mul_list)

# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']

uppor_case=list(map(lambda animals:animals.upper(),animals))
print(uppor_case)

lower_case=list(map(lambda animals:animals.lower(),animals))
print(lower_case)

friend_nam=["sumilon","anik","Rubie","Ratin","Rahul","likhon"]

upper_conv=list(map(lambda up:up.upper(),friend_nam))
print(upper_conv)