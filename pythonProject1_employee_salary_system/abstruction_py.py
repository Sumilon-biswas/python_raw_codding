#
# #abstructoion
#
# from  abc import ABC,abstractmethod
#
# class shape(ABC):
#     def __init__(self,dim1,dim2):
#         self.dim1=dim1
#         self.dim2=dim2
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class triangle(shape):
#
#     def area(self):
#         area=0.5 * self.dim1 * self.dim2
#         print("Triangle Result =",area)
#
# class Rectangle(shape):
#
#     def area(self):
#         area=self.dim1 * self.dim2
#         print("Rectangle area =",area)
#
#
# # tri_1=triangle(10,20)
# # tri_1.area()
# #
# # print("Rectangle area")
# # Re=Rectangle(5,6)
# # Re.area()
# #
#
# from  abc import  ABC,abstractmethod
#
# class twoNumber(ABC):
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#
#     @abstractmethod
#     def getResult(self):
# #         pass
# #
# # class addition(twoNumber):
# #
# #     def getResult(self):
# #         res=self.num1 + self.num2
# #         print("addition result =",res)
# #
# # class substraction(twoNumber):
# #
# #     def getResult(self):
# #         res=self.num1 - self.num2
# #         print("substraction result =",res)
# #
# # class multification(twoNumber):
# #     def getResult(self):
# #         res=self.num1 * self.num2
# #         print("multification Result =",res)
# #
# # class division(twoNumber):
# #
# #     def getResult(self):
# #         res=self.num1 /self.num2
# #         print("division result =",res)
# #
# # add=addition(20,10)
# # add.getResult()
# #
# # sub=substraction(20,10)
# # sub.getResult()
# #
# # modul=multification(5,6)
# # modul.getResult()
# #
# # div=division(50,10)
# # div.getResult()
#
#
# #Example-3:
#
# from  abc import  ABC,abstractmethod
#
# class animal(ABC):
#
#     @abstractmethod
#     def move(self):
#         pass
#     @abstractmethod
#     def sound(self):
#         pass
#     def eat(self):
#         pass
#
# class Human(animal):
#
#     def move(self):
#         print("Human can walk and run")
#
#     def sound(self):
#         print("Hemen can talk")
#
#     def eat(self):
#         print("Humen can eat rice and vegtable,meat")
#
#
# class sanake(animal):
#        def move(self):
#          print("sanak can crawl..")
#
#        def sound(self):
#            print("snake can not sound..")
#
#        def eat(self):
#            print("snake can eate little bit of animales")
#
# class Dog(animal):
#
#     def move(self):
#         print("Dog can walk and run very fast.")
#     def sound(self):
#         print("Dog can Barking")
#     def eat(self):
#         print("Dog  eate many food ")
#
# class lion(animal):
#
#     def move(self):
#
#         print("lion walking  very fast..!")
#     def sound(self):
#         print("Lion can roars")
#
#     def eat(self):
#         print("lion eat meat")
#
#
# print("Human class")
# Hu=Human()
# Hu.move()
# Hu.sound()
# Hu.eat()
#
# print("snake class")
# sn=sanake()
# sn.move()
# sn.sound()
# sn.eat()
#
# print("Dog class")
# dog=Dog()
# dog.move()
# dog.sound()
# dog.eat()
#
# print("lion class")
#
# li=lion()
# li.move()
# li.sound()
# li.eat()