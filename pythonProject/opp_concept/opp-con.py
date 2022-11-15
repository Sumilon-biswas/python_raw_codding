# value = 45
#
# # format the integer to binary
# binary_value = format(value, 'b')
# print(binary_value)
#
# l="python programing languages"
# has_value=hash(l)
# print(has_value)
# print("Hash for the 181 values",hash(181))
# print("Hash for float valueof ",hash(181.23))
# print("=========")
# print("hash value of python",hash("python"))
#
# vowels=('a','e','i','o','u')
# print(hash(vowels))

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)

# class person:
#   def  __init__(self,name,ages):
#     self.name=name
#     self.age=ages
# p1=person("sumilon",56)
# print(p1.name)
# print(p1.age)

# class person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
# p1=person("jibon roy",888)
# print(p1.name)
# print(p1.age)

# class myclass:
#
#   attra="mammale"
#   def __init__(self,name):
#     self.name=name


# Driver code
# Object instantiation
# Rodger = myclass("Rodger")
# Tommy = myclass("Tommy")
#
# # Accessing class attributes
# print("Rodger is a {}".format(Rodger.__class__.attra))
# print("Tommy is also a {}".format(Tommy.__class__.attra))
#
# print("my name is {}".format(Rodger.name))
# print("my name is {}".format(Tommy.name))

# class Dog:
#   attr1="aimale"
#   def __init__(self,name):
#     self.name=name
#   def speak(self):
#     print("my name is {}".format(self.name))
# p1=Dog("piku")
# p2=Dog("Lipu")
# p1.speak()
# p2.speak()

# class summation:
#
#   def __init__(self,a,b):
#     self.a=a
#     self.b=b
#   def sum(self):
#     print(self.a+self.b)
#
# s=summation(10,20)
# print( s.sum())

# def unorganized(a,b):
#   for x in range(a,b):
#     print(x,x**2,x**3,x**4)
#
# def organized(a,b):
#   for a in range(a,b):
#     print("{:6d} {:6d} {:6d} {:6d}".format(a,a**2,a**3,a**4))
#
#
# num1=int(input("Enter your value"))
# num2=int(input("Enter your second value"))
#
# unorganized(num1,num2)
# print("after organized")
# organized(num1,num2)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfun(self):
#         print(self.name)
#         print(self.age)
#
#
# p1=Person("jhon",53)
# p1.myfun()
# class Person:
#   def __init__(mysillobject, name, age):
#     mysillobject.name = name
#     mysillobject.age = age
#
#   def myfunc(abc):
#     print("Hello my name is " + abc.name)
#
# p1 = Person("anika", 36)
#
# p1.myfunc()
#
# class person:
#     def __init__(self,fname,lname):
#         self.fristname=fname
#         self.lastname=lname
#     def printerName(self):
#         print(self.fristname+" "+self.lastname)
#
# class student(person):
#     pass
#
# std=student("sumilon biswas","anik")
# std.printerName()



# class Parrot:
#
#     # class attribute
#     species = "bird"
#
#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)
#
# # access the class attributes
# print("Blu is a {}".format(blu.__class__.species))
# print("Woo is also a {}".format(woo.__class__.species))
#
# # access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print("{} is {} years old".format( woo.name, woo.age))

# class parrot:
#
#     #class attributes
#     sepices="bird"
#
#     #instance attributes
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# # instantiate the Parrot class
# blu=parrot("blu",100)
# woo=parrot("woo",40)
#
# #access the class attributes
# print("blue is a {}".format(blu.__class__.sepices))
# print("woo is alco a ".format(woo.__class__.sepices))
#
# print("{}  is {} years old".format(blu.name,blu.age))
# print("{} is {} years old".format(woo.name,woo.age))

#create a class
# class parrot:
#
#       #instances attributes
#     def __init__(self,name,age):
#         self.name=name
#         self.ages=age
#
#     def song(self,song):
#         return  "{} sings {}".format(self.name,song)
#     def dance(self):
#         return "{} is dancing now".format(self.name)
#
# #class istances of objects
# blu=parrot("Blue",10)
#
# #class our instances method
# print(blu.song('Happy'))
# print(blu.dance())


#python inhertainces
#parents class
# class birds:
#     def __init__(self):
#         print("Birds of flying")
#     def whoisthis(self):
#         print("birds flying sky")
#     def swim(self):
#         print("the boys swim in the river")
#
# #child class
#
# class Penguin(birds):
#
#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("Penguin is ready")
#
#     def whoisThis(self):
#         print("Penguin")
#
#     def run(self):
#         print("Run faster")
#
#
# peggy =Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()


# # parent class
# class Bird:
#
#     def __init__(self):
#         print("Bird is ready")
#
#     def whoisThis(self):
#         print("Bird")
#
#     def swim(self):
#         print("Swim faster")
#
#
# # child class
# class Penguin(Bird):
#
#     def __init__(self):
#         # call super() function
#         super().__init__()
#         print("Penguin is ready")
#
#     def whoisThis(self):
#         print("Penguin")
#
#     def run(self):
#         print("Run faster")
#
#
# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()

#parents class
# class student:
#
#     def __init__(self,fame,lname):
#         self.name=fame
#         self.lname=lname
#
#     def std_detalie(self):
#         print(self.name+" "+self.lname)
#
# class studentinfo(student):
#
#     def __init__(self,fame,lname):
#         student().__init__(self,fame,lname)
#         print("this is student iformation")
#
#     def sumation(self, a, b):
#         Result =(a + b)
#         print(Result)
#
# std= studentinfo("sumilon","biswas ")
# std.std_detalie()
# std.sumation(10,20)

# Python code to demonstrate how parent constructors
# are called.

# parent class
# class Person(object):
#
#     # __init__ is known as the constructor
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
#
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#
#
# # child class
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
#
#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
#
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Post: {}".format(self.post))
#
#
# # creation of an object variable or an instance
# a = Employee('Rahul', 886012, 200000, "Intern")
#
# # calling a function of the class Person using
# # its instance
# a.display()
# a.details()

# class person(object):
#
#     def __init__(self,name,idnumber):
#         self.name=name
#         self.idnumber=idnumber
#
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#     def details(self):
#         print("my name is {}".format(self.name))
#         print("idnumber {}".format(self.idnumber))
#
# class employee(person):
#
#     def __init__(self,name,idnumber,salary,post):
#         self.salary=salary
#         self.post=post
#         # invoking the __init__ of the parent class
#         person.__init__(self,name,idnumber)
#
#     def details(self):
#         print("Id number {} ".format(self.idnumber))
#         print("my name is {} ".format(self.name))
#         print("salary {} ".format(self.salary))
#         print("post {} ".format(self.post))
#
# a = employee('Rahul', 886012, 200000, "Intern")
# a.display()
# a.details()
#
# print("============")
#
# aa=employee("sumilon",998877,50000,"Intern")
# a.display()
# a.details()
#
#
# class Bird:
#
#     def intro(self):
#         print("There are many types of birds.")
#
#     def flight(self):
#         print("Most of the birds can fly but some cannot.")
#
#
# class sparrow(Bird):
#
#     def flight(self):
#         print("Sparrows can fly.")
#
#
# class ostrich(Bird):
#
#     def flight(self):
#         print("Ostriches cannot fly.")
#
#
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()
#
# obj_bird.intro()
# obj_bird.flight()
#
# obj_spr.intro()
# obj_spr.flight()
#
# obj_ost.intro()
# obj_ost.flight()

# class Base:
#     def __init__(self):
#         self.a="geeksforgreeks"
#         self.__c="sumilo biswas"
#
# class driveclas(Base):
#
#     def __init__(self):
#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling private member of base class: ")
#         print(self.__c)
#
# b=Base()
# # print(b.a)

# number=int(input("Enter your value :"))
#
# class student:
#     def check_pass_fail(self):
#         if self.marks>50:
#             return  True
#         else:
#             return False
#
#
# std1=student()
# std1.name="sumilon"
# std1.marks=number
#
# pas_marks=std1.check_pass_fail()
# print(pas_marks)

# marks=int(input("Enter your marks"))
#
# class student:
#
#     def check_pass_fail(self):
#
#         if self.marks>40:
#             return True
#         else:
#             return  False



# std=student()
# std.name="sumilon"
# std.marks=marks
# Result=std.check_pass_fail()
# print(Result)
#
# student1=student()
# student1.name="anik"
# student1.marks=30
# dib_pass=student1.check_pass_fail()
# print(dib_pass)
#
# class student:
#
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#
#     def display(self):
#         print("this name is {}".format(self.name))
#         print("marks is {}".format(self.marks))
#
#         #check the marks pass or fail
#     def check_it_pass_or_fail(self):
#         if self.marks>40:
#             return True
#         else:
#             return  False
#
#
# marks=int(input("Enter your marks :"))
#
# student=student("sumilon",marks)
# student.display()
# bib_pass=student.check_it_pass_or_fail()
# print(bib_pass)

# class complex:
#     def __init__(self,real,imag):
#         self.real=real
#         self.imag=imag
#
#     def add(self,number):
#         real=self.real+number.real
#         imag=self.imag+number.imag
#         result=complex(real,imag)
#         return  result
#
# n1=complex(5,6)
# n2=complex(-4,2)
# Result=n1.add(n2)
# print("Real number is ",Result.real)
# print("imag number is ",Result.imag)

class complex:

    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def sumartion(self,number):
        real=self.real+number.real
        imag=self.imag+number.imag
        Result=complex(real,imag)
        return  Result
n1=complex(9,7)
n2=complex(-5,6)
Result=n1.sumartion(n2)
print("real number is {}".format(Result.real))
print("imag number is {}".format(Result.imag))



