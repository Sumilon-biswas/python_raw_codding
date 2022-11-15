import random

# print("Hello, programig laguages")
# print("sumilio biswas anik")
# x=9
# print(x)
# print(type(x))

# y=8
# y="salary"
# print(y)
# x=str(7)
# y=int(6)
# z=float(3)
# print(x)
# print(y)
# print(z)
# number=7;
# print(type(number))
# name="sumilo";
# print(type(name))

#multopal variable assccesig

# x,y,z="Orage","Banana","cherry"
# print(x)
# print(y)
# print(z)

# x=y=z="orage"
# print(x)
# print(y)
# print(z)

# fruits=["apple", "banana", "cherry"];
# x,y,z=fruits
# print(x)
# print(y)
# print(z)

# output variable

# x="python is awasome programig laguages"
# print(x)
# x="python"
# y="is"
# z="awasome"
# a="programig"
# b="laguages"
# print("Languages :"+ x,y,z,a,b)
# print(x+y+a+z+b)
#
# print(10+78)

# x = 5
# y = "John"
# print(x, y)

#Global variable && local variable
# x="python programig lg"; #this is global variable
#
# def myfunc():
#     x="sumilon"  #this is local variable
#     print(x)
# myfunc()
#
# print(x)

#date type of python

# x=str("summon")
# print(x)
# #display of type
# print(type(x))
# t=str('kabir')
# print(type(t))
# print(t)
#
# b=20
# print(b)
# print(type(b))

# x=complex(4j)
# print(x)
# print(type(x))

#number type

# x=2;
# y=2.7
# z=7j
# print(type(x))
# print(type(y))
# print(type(z))
#
# a=3+7j
# print(a)
# print(type(a))


# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

#convert to float
# a=float(x);
# print(a)
# b=complex(x)
# print(b)
#
# h=int(y)
# print(h)

# print(random.randrange(1,10))

# casting of value

# a=int(7.6)
# print(a)
# z=int("7")
# print(type(z))
# print(z+8)
# print(z)
# a=float(10.00)
# print(type(a))
# print(a)

#string method

# a="hello world"
# print(a[1])
# print(a[3])
# print(a[8])
#
# #looping thorught of
#
# for x in "Bangladeesh":
#     print(x)
#
# print("Aother ==============")
#
# for y in  "Banana":
#     print(y)


# a="hello world"
# print(len(a))
# name="sumilon biswas aink"
# print(len(name))
#
# # txt = "The best things in life are free!"
# # print("best" in txt)
#
# name="sumilon biswas anik"
# if "hello" in name:
#     print("yes ")
# else:
#    print("No")
#
# # not in string array
#
# p="Bangladesh is small conutry"
#
# if "jumpa"not  in p:
#     print("yes")
# else:
#     print("no")
# print("jumpa" not in p)

# h="hello world"
# print(h[2:5])
# print(h[3:])
# print(h[:7])
# print(h[-5:-2])

#string modife

# a="python programig languages"
#
# print(a.upper())
# h="BANGLADESH"
# print(h.lower())

# h=" Hello , world "
# print(h)
# print(h.strip())
#
# n="sumilon"
# print(n.replace('s' ,'A'))
#
# a=" Hello , world  "
# print(a.split(','))

a="Bangladesh"
b="criket"
print(a+b)

#string formate

# age = 36
# txt = "My name is John, I am {}"
# print(txt.format(age))
#
# number=1
# name="sakibe all Hasan is world number {}  allround player  "
# print(name.format(number));
#
# quitity=800
# item=500
# price=7000
# myorder="I want {} prices {} prices of item {} for dollars"
# print(myorder.format(quitity,item,price))
#
#
# sm="small"
# con="Bangladesh is {} conutry"
# print(con.format(sm))

#string method
# txt = "hello, and welcome to my world."
#
# x = txt.capitalize()
#
# print (x)
#
# x="python programing languages"
# show=x.capitalize()
# print(show)

# txt = "Hello, And Welcome To My World!"
# x=txt.casefold()
# print(x)
#
# cap="sumilon "
# print(cap.center(60))
# print(cap.count("um"))

# txt = "I love apples, apple are my favorite fruit"
# print(txt.count("apple"))
# print(txt.count("fruit"))

# p="Best programing languages"
# print(p.endswith("languages"))

# p="Sakibal all hasan is number on cricketer in world criket"
# print(p.find("hasan"))
# print(p.find("world"))
# print(p.index("s"))
# print(p.index("c"))

# fname="sumilon"
# lname="biswas"
# print(fname.join(lname))
# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
# x=mySeparator.join(myDict)
# print(x)

#boolearn value

# print(9>8)
# print(1==1)
# print(7<5)
# print(10==9)

# a=200
# b=33
# if a>b:
#     print("a is the greater then b")
# else:
#     print("b is greater then a ")
# print(bool("hello"))
# print(bool(90))
# print(bool())
# print(bool())

#Assignment Operators

# # x=5
# # x +=7
# # print(x)
# # x -=3
# # print(x)
# # x *=2
# # x //=3
# # x **=6
# # print(x)
# x=4
# # x &=7
# x |=3
# print(x)

# x=7
# print( x<5 & x<10)
# print(x<3 | x<4)

#python identity operator

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z=x;
# print(x is z)
# print(x is y)
# print(x is not  y)
# print(x is not z)
# print(x==z)

txt="Dhaka is big city of Bangladesh"
print("Dhaka" in txt)
print("big" in txt)
print("player" not in txt)
print("city" not  in txt)