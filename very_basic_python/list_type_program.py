
# my_list=["python","html","css","javascript","j-quriye"]
# print(my_list)
# print(type(my_list))

# constructor list that data store it

# bb=list(("sumilon","anik","jibon","Raton","mallick","shepa"))
# print(bb)

#nested list

# a=["shajajan",["python",'c#',"java","php"],"Billa","Rakib","Nazrin"]
# print(a)

# user input date add a list

# lise=[]
# for i in range(0,5):
#     a=input("Input a name valu :")
#     lise.append(a)
#
# print(lise)
#
# str=[]
# for i in range(0,7):
#     bb = int(input("Enter your number  :"))
#     str.append(bb)
#
# print(str)
#
# sum=0
# for i in str:
#     sum=sum+i
#
# # print("total summation of :",sum)
#
# # list positive/index or postion
#
# a=["shahjahan","Billal","jamal","Nazir","faruk"]
#
# print(a[2])
# print(a[1])
# print(a[3])
#index of negatie program
# a=["shahjahan","Billal","jamal","Nazir","faruk"]
# print(a[-1])
# print(a[-3])
#range//slice
# a=["shahjahan","Billal","jamal","Nazir","faruk"]
# print(a[2:4])

# list add/insert data
# fr_name=["shajhan","sokale","Ripon"]
# print(fr_name)
# fr_name.append("joya bain")
# print(fr_name)
# fr_name.append("tanbir islam")
# print(fr_name)
#
# fr_name=["shajhan","sokale","Ripon"]
# #insert() method
# fr_name.insert(3,"shipon dak")
# print(fr_name)

# list extend of
# list1=["tanbir islam","joya","jerry","kolie"]
# list2=["sherry","Ritu","milon","Raniku","joe ","Battaler"]
# # list1.extend(list2)
# finall_lis=list2+list1
# print(finall_lis)

#list data asscess using loop


# a=["apple","jerry","cherry","orange"]
# for i in a:
#     print(i)

#nested list
#
# a=["apple","Banana",["watermelon","orange","jakfruites"],"pineapple"]
#
# for i in a:
#     if type(i) is list:
#         for j in a:
#             print(j)
#     else:
#         print(i)

fruits1=["apple","Banana","orange"]
fruits2=["watermelon","orange","pineapple"]
fru=fruits2.copy()
print(fru)