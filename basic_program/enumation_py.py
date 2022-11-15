# name_list=["sumilon","joya bain","likhu","tanbir","sagor ","looypop"]
#
# i = 1
# for item in name_list:
#     if i % 2 is not 0:
#         print(item)
#     i +=1

# i = 1
# for item in name_list:
#     if i % 2 == 0:
#         print(item)
#     i +=1

# student_list=["sumilon","anik","akash","Ripon","shipon","nikor","limu"]
#
# for item , value in enumerate(student_list):
#      if item % 2 == 0:
#          print(f"this is student list {value}")
#

# teacher_list=["sakib","anu","john","Robin","kalsare","apu","sham lala Roy","nipon"]
#
# for index, value in enumerate(teacher_list):
#     if index % 2 == 0:
#         print(f"teacher list is {value}")


# # Python program to illustrate
# # enumerate function
# l1 = ["eat", "sleep", "repeat"]
# s1 = "geek"
#
#
# # type showing
# # print(enumerate(s1))
# # print(enumerate(l1))
#
# print(list(enumerate(s1)))
# print(list(enumerate(l1)))

work=["Eat","sleep","reate","reste"]

for item in enumerate(work):
    print(item)

print("=================")
for item in enumerate(work,100):
    print(item)
print(" ===============")
for count,value in enumerate(work):
    print(count)
    print(value)
print("===========")

programing_languages =["python","javascript","C#","Rube"]

enumate_prime=enumerate(programing_languages)
print(list(enumate_prime))


