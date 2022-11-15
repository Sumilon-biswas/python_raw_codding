
#Dictionary is nothing but key values pairs
#
# d1 = [] this is  list of python
# d1 = () this is tuple of python
# d1 = {} #this is Dictonary of python
#
# print(type(d1))

# d1 ={"name":"sumilon biswas","age":20,"profession":"student","study in":"Dhaka international university of Dhaka(DIU)"}
#
# print(type(d1))
#
# # name ="sumilion biswas"
# # if d1["name"]== name:
# #     print("this name include of dict")
# # else:
# #     print("this name is  not include of dict")
#
# print(d1["study in"])
# print(d1["age"])
# print(d1["name"])

# pro ="Doctor"
# if d1["profession"] == pro:
#     print("yes")
# else:
#     print("No")

# like_food ={"sumilon":"Barinie","monta":"cholate","tanbir":"lollpop","titu":"junk food","litu":"chiken ries"}
#
# like_food["joya"] = "mask user"
# print(like_food)

# pointof ={"sumilon":"student","tanbir":"khalour","joy":"play boy","sagor":"hard working","summon":"criketer"}
# print(pointof)
# pointof["aniketed"]= "motu boy"
# print(pointof)

# pointof ={"sumilon":"student","tanbir":"khalour","joy":"play boy","sagor":"hard working","summon":"criketer"}
#
# # d1 = pointof.copy()
# # print(type(d1))
# del  pointof["sumilon"]
# print(pointof)
#
# d1 = {"Herry":"programer","sumilon":"learne","Rakib":"suggester","shipu":"trainer"}
# # # # del d1["sumilon"]
# # # # del  d1["Rakib"]
# # # del  d1["Herry"]
# # d3= d1.copy()
# # print(d3)
# # # print(d1)


# # d1 = {"Herry":"programer","sumilon":"learne","Rakib":"suggester","shipu":"trainer"}
# # print(d1.get("Herry"))
# # print(d1.get("Rakib"))
# # print(d1.get("sumilon"))
# #
# # print(d1)
#
# d1 = {"Herry":"programer","sumilon":"learne","Rakib":"suggester","shipu":"trainer"}
# print(d1.update({"Tahsan":"singer"}))
# print(d1)

# d1= {}
# d1.update({"sumilon":"student"})
# d1.update({"tahsan khan":"singer"})
# d1.update({"Ridoy khan":"singer"})
# d1.update({"jibon sarker":"pujare"})
# print(d1)

# person={}
# person.update({"sumilon":"student"})
# person.update({"anik":"software enginerring"})
# person.update({"Asif":"markter"})
# person.update({"lipu":"market anlizera"})
# person.update({"shipun":"sell man"})
# print(person)
# print(person["sumilon"])
# print(person.get("anik"))
# person.pop("sumilon")
# print(person)
# print(person.items())
# print("key values====")
# print(person.keys())
# print("paire of value")
# print(person.values())
#
# print(person.clear())

#  problem  solve
# create a dictornary  and user input return value of pass a dictonary

# employees = {}
#
# for i in range(3):
#     name = input("Enter employee's name: ")
#     salary = input("Enter employee's salary: ")
#
#     employees[name] = salary
#
#
# # 👇️ {'Alice': '100', 'Bob': '100', 'Carl': '100'}
# print(employees)

# n = int(input("Input a N value"))
#
# employee = {}
#
# for i in range(n+1):
#     name =input("Enter the employee Name :")
#     salary = int(input("Enter employee salary :"))
#     employee[name]=salary
#
# print(employee)

# n = int(input("Enter a value of n :"))
# employee={}
# for i in range(n+1):
#     name = (input("Employee name here :"))
#     salary =int(input("Employee salary here :"))
#     employee.update({name : salary})
#
# print(employee)

# profession = {
#     "sumilon":"student",
#     "Dulal biswas":"Teacher",
#     "Ripon":"employee",
#     "Asim":"engineering",
#     "tanbir":"Bussiness man",
#     "Raton":"Julary",
#     "liton":"trainer"
# }
#
# name=input("Enter name :")
#
# print(profession[name])

# salary_sit={
#     "john":29999,
#     "sukanto":75676,
#     "nupor":15000,
#     "sholie":30000,
#     "monile":40000
#
# }
#
# name = input("person name input :").lower()
#
# print(salary_sit[name])

# #
# # dict ={}
# # name =input("Input you name :")
# # salary = input("Input salary :")
# #
# # dict[name]=salary
# # print(dict)
#
# # input = input("Input a single alphabet :").upper()
# #
# # Alpha ={"H":"hello","A":"amazing","G":"good","N":"news","R":"red"}
# #
# # if input in Alpha:
# #     print(Alpha["H"])
# # else:
# #     print("try ")
#
# dict = {
#         "variable": "Temporary stored memory location",
#         "constant": "Immutable variable",
#         "datatype": "Type of Data",
#         "keywords": "Reseerved Words"
#     }
# print("Enter word meaning")
# word=input()
# print(dict[word])

# dict1 ={"Herry":"programer python","naimul":"programer php","Ripon":"self employee","anik":"teacher","susmita":"Doctor"}
#
# d=input("Enput choose value :")
#
# for key ,values in dict1.items():
#
#     if key == d:
#         print(dict1[d])
#         break

# dict1={"sakib":"structred program","sumilon":"learn programer","anu":"php developer","Neyonm":"larbel developer","nazmul":"font_desginer"}
#
# name = input("Input a value:").lower()
#
# for key,values  in dict1.items():
#     if key == name:
#         print(dict1[name])
#         break

# dict2={"trouble":"problem","c++":"computer programing langauges","update":"a new change","code with herry":"youtube cahnnel"}
#
# try:
#     #input form here user
#     word =input("word =")
#     lowerInput=word.lower()
#
#     for keys in dict2:
#         resultkeys = keys.find(lowerInput)
#         if resultkeys != -1:
#             print(keys + " maining is "+dict2[keys])
#
# except:
#     print("not found them !")
#
# new_dict ={"sumilon":"student","sabkib":"teacher","jibon":"pujare","shipu":"saler"}
#
# try:
#     word=input("your value :")
#     resultWord=word.lower()
#     for keys in new_dict:
#         resultkeys = keys.find(resultWord)
#         if resultkeys != -1:
#             print(keys + " meaning is "+new_dict[keys])
# except:
#     print("not found")

add_dict={}

for i in range(4):
    name=input("Enter your name :")
    salary = int(input("Input salary :"))
    add_dict.update({name : salary})

print(add_dict)


