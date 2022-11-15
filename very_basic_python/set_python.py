
# set is unordered, unindexed,no duplicate value

# a={"Rakib","Hassan","topu"}
# print(a)
# print(type(a))
#
#
# set=({"sumilon","Tanbir islam","Rakib","shipon"})
# print(set)
#
#
# # set print korla ar vator sob data alomalo vaba print hoy
#
# myset={"Rakib","Hassan","Hassan","topu","topu","Ratul"}
# print(myset)

# myset={"sumilon",21,"CSE",3.50}
# print(myset)
#
# #constructor use data pase
#
# a=set(("sumilon","anik","Ripon","lemion","likhon"))
# print(a)

# a={"Rakib","Hassan",23,4.24,"Rikhon",("tanbir islam","cse","computer")}
#
# for i in a:
#     if type(i) is tuple:
#         for j in i :
#             print(j)
#     else:
#         print(i)
#
# b={"sumilon","anik","mou"}
# b.add("joya bain")
# b.add("tanbir islam")
# b.add("shipon Rahman")
# print(b)
#set update
# b={"sumilon","anik","mou"}
# b.update(["biswas","pianapple"])
# print(b)

a ={"shincharn","Doremon","tom and jerry","meerra","mina"}
#
# del a
# print(a)
# a.remove("tom and jerry")
# a.remove("mina")
# print(a)

# #pop
# a.pop()
# a.pop()
# print(a)
#
# a.discard("tom and jerry")
# # print(a)
# print(a)
# a.clear()
# print(a)

# a={1,2,3,5,8}
# b={2,4,6,7,8}
# c=a|b
# print(c)

# name_1={"sumilon","Dibakar","Dipankar","milton"}
# name_2={"mou","Dipa","pitul","karion"}
# fullname=name_1 | name_2
# print(fullname)

# num_1={1,2,3,4,5,6}
# num_2={"one","two","three","four","five","six"}
#
# result=num_1 | num_2
# print(result)

# set1=set()
# set2=set()
#
# for i in range(1, 6):
#     set1.add(i)
#
# print(set1)
#
# for i in range(3,8):
#      set2.add(i)
# print(set2)

# set4=set1 == set2
# print(set4)
# set5=set1 !=set2
# print(set5)
#
# Aset1=set()
# Aset2=set()
#
#
# for i in range(1,6):
#     Aset1.add(i)
# print(Aset1)
#
# for i in range(1,6):
#     Aset2.add(i)
# print(Aset2)
# res=Aset1 == Aset2
# print(res)

# Aset1=set()
# Aset2=set()
#
#
# for i in range(1,6):
#     Aset1.add(i)
# print(Aset1)
# for i in range(1,8):
#    Aset2.add(i)
#
# print(Aset2)
#
#
# # r

# set_1=set()
# set_2=set()
# for i in range(1,6):
#     set_1.add(i)
# print(set_1)
#
# for i in range(3,8):
#     set_2.add(i)
# print(set_2)
#
# res=set_1 & set_2
# print(res)
#
# name_1={"sumilon","manik","tanbir","sofikul"}
# name_2={"sumilon","anik","tubal islam","tanbir"}
#
# res=name_1 & name_2
# print(res)
#
# set1=set()
# set2=set()
#
# for i in range(1,6):
#     set1.add(i)
# print(set1)
# for i in range(3,8):
#     set2.add(i)
# print(set2)
#
# res=set1 ^ set2
# print(res)
#
# name_1={"sumilon","manik","tanbir","sofikul"}
# name_2={"sumilon","anik","tubal islam","tanbir"}
#
# res1=name_1 ^ name_2
# print(res1)

# special method

# a={1,2,3,4,5,6}
# print(sum(a))

# a={34,77,99,55}
# print(sum(a))

# b={23,5,99,66,40,44}
# print(max(b))
# print("minmum values")
# print(min(b))
#
# a={2,8,3,5,10}
# # print(sorted(a,reverse=True))
# print(sorted(a,reverse=True))
