#
# grocery=["Harpic","vimbar bar","doderant","Bandhie","lollpop"]
#
# print(grocery)
# print(type(grocery))
#
# student_list =["sumo","lipun","liton","lipe","joharo"]
# print(student_list)
# print(type(student_list))
#
# #index output
#
# tecaher =["nujmul sakib",1234,"dhaka","cse","teacher","gamilon@gmail"]
# print(tecaher[0])
# print(tecaher[1])
# print(tecaher[2])
# print(tecaher[5])
# print(tecaher[4])

# numbers=[1,4,6,7,89,9,10]
# print(numbers[6])
# print(numbers[3])
# print(numbers[2])
# numbers =[2,7,3,9,5,10,6,6]
# numbers.sort()
# print(numbers)
# number =[10,3,12,7,19,12,50,4,5,22]
# number.sort()
# print(number)
# print(number.count(12))

# number =[10,3,12,7,19,12,50,4,5,22]
# number.reverse()
# print(number)

# seriral_num =[29,4,50,6,40,7,90,1]
# # seriral_num.sort()
# # seriral_num.reverse()
# # print(seriral_num)
#
# seriral_num = [29,1,5,30,50,6,40,50]
# seriral_num.sort()
# seriral_num.reverse()
# print(seriral_num)
# numbers =[2,7,12,6,18,7,9,4]
# print(numbers[3])
# print(numbers[3:6])
# print(numbers[4:6])
# print(numbers[:5])
# print(numbers[3:])
# print(numbers[2:])
# print(numbers[:])
# print(numbers[2:6 :2])
# print(numbers[::2])
# print(numbers[::3])
# print(numbers[::4])
# print(numbers[::-2])
# print(numbers[::-3])
# print(numbers[1:5:2])

#++++list max and min value print

# numbers =[2,7,12,6,18,7,9,4]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))

# # list update or modife
#
# numbers =[2,7,15,6,7,8,9]
# numbers.append(10)
# numbers.append(3)
# numbers.append(1)
#
# print(numbers)

# programming_lang = []
# programming_lang.append("python")
# programming_lang.append("c#")
# programming_lang.append("Html")
# programming_lang.append("PHP")
# programming_lang.append("javascript")
# print(programming_lang)

# man_name = []
#
# man_name.append("sumilon biswas")
# man_name.append("Dulal biswas")
# man_name.append("jihon")
# man_name.append("liku")
# man_name.append("Rangepure")
# man_name.append("shala")
# print(man_name)

# list index value insert
# numbers =[2,7,12,5]
# numbers.insert(2,10)
# numbers.insert(1,100)
# numbers.insert(0,200)
# print(numbers)

# list delect

# number = [2,7,19,20,15,25]
# # number.remove(7)
# # print(number)
# # number.pop()
# # print(number)
# number[2]=100
# number[1]=120
# print(number)

#mutable =can change the value
# unmutable  = can not change the value

# # tuple
# num =(1,2,3)
# print(type(num))
# print(num)
# num[1]=23
# print(num)

# swapping with thired variable

# a = 2
# b = 6
# temp = a
# a = b
# b = temp
# print(f"value of a:{a} and value of b:{b}")

# a = int(input("Input value of a :"))
# b= int(input("Input value of b : "))
#
# temp = a
# a = b
# b = temp
# print(f" a ={a} ,\n b={b}")

# swapping without thride variable

# a =6
# b =7
# a = a + b
# b = a-b
# a = a-b
# print(f"a={a},b ={b}")

# a =7
# b=9
# a,b =b,a
# print(f"a ={a}, b={b}")

# vowel list

# vowel_list =['a','e','i','o','u']
# print(vowel_list)
# vowel_list.clear()
# print(vowel_list)

#vowel tuple
#
# vowel_tuple =('a','e','i','o','u')
# print(vowel_tuple)
# vowel_tuple

# user input add a list

# r = int(input("INput a range value :"))
# mylist =[]
#
# for i in range(r+1):
#     name = input("Enter serial name")
#     mylist.append(name)
#
# print(mylist)

# n = int(input(" Input a range value :"))
#
# mylist =[]
#
# for i in range(n):
#     name =input("Enter a input value :")
#     mylist.append(name)
#
# print(mylist)
#
# employees = {}
#
# max_length = 3
#
# while len(employees) < max_length:
#     name = input("Enter employee's name: ")
#     salary = input("Enter employee's salary: ")
#
#     employees[name] = salary
#
#
# # 👇️ {'Alice': '100', 'Bob': '100', 'Carl': '100'}
# print(employees)


# employees = {}
#
# n = int(input("Enter a value n:"))
#
# for i in range(n+1):
#     name =input("Input employee name :")
#     salary =int(input("Input employee salary :"))
#     employees.update({name : salary})
# print(employees)

# grocery =["oil","onion","kihju","matku","hdjdhh"]
#
# print(grocery[0])


# # assigning elements to list
# list1 = []
# for i in range(0, 3):
#     list1.append(i)
#
# # accessing elements from a list
# for i in range(0, 3):
#     print(list1[i])

