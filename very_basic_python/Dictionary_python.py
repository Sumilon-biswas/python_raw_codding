
#syntax of dictonary
# a ={
#     key :value
# }

# Example-01

# a={
#     "cartoon1":"Daremon",
#     "cartoon2":"shinchar",
#     "cartoon3":"tom and jerry",
#     "cartoon4":"meina"
# }
#
# print(type(a))
#
# print(a)

# b={
#     1:"sumilon biswas",
#     2:"Rakib vai",
#     3:"Rashied"
# }
# #access the keys value
# print(b.get(2))
# print(b.get(1))
#
# #access the values
# print(b.values())

# c={
#     "name":"python programing languages",
#     "relase": 1990,
#      3 : "version",
#     "demand":"height demand"
# }
# print(c)

# dictionary data inserting constructor method

# e=dict({"name":"sumilon","age":21,"department":"CES(computer secience and engineering)","study":"Dhaka international university"})
# print(e)


#nested Dictirinary

# student ={
#     1:{"name":"Rakib hossan","age":24,"sex":"male"},
#     2:{"name":"sumilon biswas","age":21,"sex":"female"},
#     3:{"name":"marie","age":34,"sex":"female"},
#     4:{"name":"moushumie","age":35,"sex":"female"}
# }
#
# # Accessing values :
# print(student[4])
# print(student[3])
# print(student[4]["name"])
# print(student[2]["name"])
# print(student.get(1))

#add value:: and change value

# a={
#     "name1":"Rakib",
#     "name2":"Hassan",
#     "name3":"Ratul"
# }
# # a["name4"]="sumiya Rahman"
# print(a)
# #
# # a[2].pop()
# # print(a)
# a.popitem()
# print(a)
# a.popitem()
# print(a)

# access the dictonary value using loop

# a={"name":"Rakib","age":34,"place":"Dhaka"}
#
# # for i in a:
# #     print(i)
# #
# # print("=================")
# #
# # for j in a:
# #      print(a[j])
#
# for i in a.values():
#     print(i)
#
# information={"name":"sumilon biswas ","age":23,"department":"CSE(computer secience and engireening","study":"dhaka international university"}
#
# for i in information:
#     print(i)
# print("================")
# for i in information.values():
#     print(i)

# department=["English","CSE","EEE","Meciale","sociology","social secinence"]
#
# for i in department:
#     print(i)
# information={"name":"sumilon biswas ","age":23,"department":"CSE(computer secience and engireening","study":"dhaka international university"}
#
# for i ,j in information.items():
#     print(i,"=",j)

# languaged={"python":"server languages","html":"markerup","css":"case cadding style sheet","javasecript":"html dynamic maniuplation"}
#
# for i,j in languaged.items():
#     print(i ,"=",j)

# employee={
#     "ID_100":{"name":"Rakib","age":23,"salary":20000},
#     ""
# }

# people={
#     1:{"name":"john","age":"12","sex":"male"},
#     2:{"name":"marie","age":33,"sex":"male"}
#
# }
#
# # print(people[1]["name"])
# # print(people[1]["age"])
# # print(people[1]["sex"])
# # print(people[2]["name"])
# # print(people[2]["age"])
# # print(people[2]["sex"])
#
# people[3]["name"]="sumilon biswas"
# people[3]["age"]=23
# people[3]["sex"]="male"
#
# print(people)
#
# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
#
# people[3] = {}
#
# people[3]['name'] = 'Luna'
# people[3]['age'] = '24'
# people[3]['sex'] = 'Female'
# people[3]['married'] = 'No'
#
# print(people[3])


# people={
#     1:{"name":"john","age":23,"sex":"male"},
#     2:{"name":"marie","age":24,"sex":"female"}
#
# }
#
# people[3]={}
#
# people[3]["name"]="sumilon biswas anik"
# people[3]["age"]=24
# people[3]["sex"]="male"
#
# print(people)

# friend_dict={
#     1:{"name":"sagor sikder","age":23,"Department":"CSE","Roll":"27"},
#     2:{"name":"joya bain","age":24,"Department":"CSE","Roll":"12"},
#     3:{"name":"tohain","age":25,"Department":"CSE","Roll":23},
# }
# friend_dict[4]={}
#
# friend_dict[4]["name"]="tanbir islam"
# friend_dict[4]["age"]=33
# friend_dict[4]["department"]="CSE"
# friend_dict[4]["Roll"]=34
# print(friend_dict)

# employee={
#     "ID_100":{"name":"Rakib","age":24,"salary":3000},
#     "ID_102":["Hassan",24,34000],
#     "ID_103":("Ratul",45,22000),
#     "ID_104":"Rashied"
# }
#
# for  i ,j in  employee.items():
#     if type(j) is list:
#         print("liste :")
#         for i in j:
#             print(i)
#
#     elif type(j) is tuple:
#         print("tuple :")
#         for i in j :
#             print(i)
#
#     elif type(j) is dict:
#         print("Dict")
#         for i in j:
#             print(i)
#     else:
#         print(i,"=",j)


#take user input

person={}

for i in  range(0,5):
    keys=input("please! Input keys :")
    values=input("Please! Input values :")
    person.update({keys:values})
print(person)
