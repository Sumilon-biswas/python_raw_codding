#loop using in python
#
# mylist =["Herry","Larry","Carry","marie"]
# print(mylist[0])
# print(mylist[1])
#
# for item in  mylist:
#     print(item)

# mytuple=("Herry","larry","carry","marie")
#
# for item in mytuple:
#     print(item)

# student =[["sumilon",1],
#           ["joya",2],
#           ["tanbir",4],
#           ["nayaimu",7],
#           ["shipon",98],
#           ["likhon",78]
#         ]
# for item in student:
#     print(item)

# profession =[["sumilon","student"],
#              ["sakib","teacher"],
#              ["tanbir islam","bussiness man"],
#              ["joya bain","singer"],
#              ["Ritu","Dancer"],
#              ["kolie","trainer"]]
# # for item in profession:
# #     print(item)
# for item ,lollypop in profession:
#     print(item,"and profession ",lollypop)

# languages=[["Html","hypertext markup languages"],
#            ["CSS","case casding languages"],
#            ["javascript","javascript"],
#            ["j-query","javascript libary"],
#            ["python","I love python"]]

# dict1=dict(languages)
# print(dict1)
# for keys,value in dict1.items():
#     print(keys ,"meanin form ",value)
# print("-==================")
# for keys , values in languages:
#     print(keys ,"full name ",values)

# mylist =["html","python","herry",2,3,4,5,6,78,98,34,56,45,66]
#
# for item in mylist:
#     if str(item).isnumeric() and item >= 6:
#         print(item)

lower_value = int(input("Please, Enter the Lowest Range Value: "))
upper_value = int(input("Please, Enter the Upper Range Value: "))
count=0

print("The Prime Numbers in the range are: ")
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            count +=1
            print(number)
print("prime number count  ")
print(count)