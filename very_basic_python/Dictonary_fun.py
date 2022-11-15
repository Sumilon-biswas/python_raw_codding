
# python collection dictonary

a={
      "name":"sumilon biswas",
      "age":21,
      "department":"B.S.C in CSE",
      "university":"Dhaka international university"
}

# print(type(a))
# print(a)
# print(a.keys())
# print(a.values())
# print(len(a))

# print(type(a))
# print(a)
# print("dictonary keys show kora janno")
# print(a.keys())
# print("===========")
# print(a.values())
# print("==============")
# print(a.items())

# constructors declare kora value inserted

# a=dict({
#       "name":"sumilon biswas anik",
#       "age":23,
#       "GPA":3.75,
#       "height":"5.5 heights"
#
# })


# print(a)
# print(a.keys())
# print(a.values())
# print(a.items())


#nested Dictonary

# student={
#       1:{"name":"sumilon","age":21,"sex":"male"},
#       2:{"name":"Anu","age":32,"sex":"female"},
#       3:{"name":"tanbir","age":22,"sex":"female"},
#       4:{"name":"joya bain","age":23,"sex":"male"}}
# #
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())

#Accessing values
# print(student[3])
# # print(student["name"])
# print(student[3]["name"])
# print(student[3]["age"])
# print(student[3]["sex"])
#
# print(student.get(1))
# print(student.get(2))
# print(student.get(3))
# print(student.p)

# a={
#       "name1":"sumilon bisws",
#       "name2":"pantu"
#
# }
#
# a["name3"]="sumi"
# a["name4"]="jerry"
# a["name5"]="hera"
# print(a)

# student={
#       1:{"name":"sumilon","age":21,"sex":"male"},
#       2:{"name":"Anu","age":32,"sex":"female"},
#       3:{"name":"tanbir","age":22,"sex":"female"},
#       4:{"name":"joya bain","age":23,"sex":"male"}}
#
# student[1].pop("age")
# print(student)
# student[3].pop("name")
# print(student)

# copy dicontary past another dicontary


# a={"name":"Rakib",'age':23}
# b=a.copy()
# print(b)

# looping use kora dictonary
#
# a={"name":"Sumilon biswas","age":21,"live":"Dhaka"}
# for i in a:
#       print(i)
# for i in a:
#       print(a[i])
#
#
# fname_Show={"fname_1":"sagor","fname_2":"dipa","fname3":"Root"}
#
# for i in fname_Show:
#       print(i)
# for i in fname_Show:
#
#       print(fname_Show[i])

# user take input


# n=int(input("How many personal information do you want to add :"))
#
# for i in range(n):
#       key=input("plese enter a key :")
#       values=input("please enter values")
#       person.update({key:values})
# print(person)
# person={}
# while True:
#       keys=input("please enter a key :")
#       values=input("please enter a values :")
#       if keys =='' and values =='':
#             break
#
#       person.update({keys:values})
#
# print(person)
#
# a={
#       "name":"sumilon biswas",
#       "age":21,
#       "habbit":"learing programming"
# }
#
# print(a)
# a.clear()
# print(a)

person={
      1:{"name":"sumilon","age":23,"profession":"student"},
      2: {"name": "anik", "age": 21, "profession": "student"},
      3: {"name": "nikor", "age": 25, "profession": "Teacher"},
      4:{"name":"sagor sikder","age":21,"profession":"job holder"}

}
print(person.keys())
# print("   ")
# print(person.values())
# print(person.items())
#
# def count(number):
#       if number == 3:
#             return 3
#       else:
#             return count(number+1)+1
#
# print(count(1))
#
# def factorial(n):
#
#       if n == 1:
#             return 1
#       else:
#             return  n * factorial(n-1)
#
# result=factorial(5)
# print("total factorial values =",result)
