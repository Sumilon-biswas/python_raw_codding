# import random
# from  random import  Random

# list=["sumilon","nikor","jibon","tanbir","joya","sagor"]
# choose =random.choice(list)
# print(choose)

# list1 = [1,2,3,4,5,6,7,8]
# chose = random.choice(list1)
# print(chose)

# program =["python","Html","css","javascript","j-query","php"]
#
# chose=random.choice(program)
# print(chose)

# random.seed(6)
# # print(random.random())
#
# random.seed(5)
# print(random.random())
# print(random.random())
# print(random.random())

# print(random())

# from random import random
#
# # Prints random item
# print(random())

# string  ="sumilon biswas"
# chose =random.choice(string)
# print(chose)

# simple_list=[1,2,3,4,5]
#
# # orginals list show
# print("orginal frist list show :",simple_list)
#
# random.shuffle(simple_list)
# print("change the frist shuffle function")
# print(simple_list)
# random.shuffle(simple_list)
# print("change to 2nd list")
# print(simple_list)


# sample_list = [1, 2, 3, 4, 5]
#
# print("Original list : ")
# print(sample_list)
#
# # first shuffle
# random.shuffle(sample_list)
# print("\nAfter the first shuffle : ")
# print(sample_list)
#
# # second shuffle
# random.shuffle(sample_list)
# print("\nAfter the second shuffle : ")
# print(sample_list)


# print(random.sample(range(20), k = 10))

# print(random.sample(range(10),k=5))
# print(random.sample(range(20),k=3))
# print(random.sample(range(10),k=9))
# print(random.sample(range(7),k=5))

# using the triangular() method

# height=20
# width = 30
# mode = 100
# print(random.triangular(height,width,mode))

# reiangular law
# AC^2 = AB^2 + BC^2

# height = 20
# width = 30
# mode = 100
# print(random.triangular(height,width,mode))

# using  loop traigular
#
# low = 10
# high = 100
# mode = 20
#
# # running the triangular method with the
# # same parameters multiple times
# for i in range(10):
#     print(random.triangular(low, high, mode))

# low = 20
# heigh =100
# mode = 20
# for i in range(10):
#     print(random.triangular(low,heigh,mode))


# import the required libraries
# import the required libraries
# import random
# import mat as plt
#
# # store the random numbers in a list
# nums = []
# low = 10
# high = 100
# mode = 20
#
# for i in range(10000):
#     temp = random.triangular(low, high, mode)
#     nums.append(temp)
#
# # plotting a graph
# plt.hist(nums, bins=200)
# plt.show()


import  random

rand=random.random()*100
print(rand)

