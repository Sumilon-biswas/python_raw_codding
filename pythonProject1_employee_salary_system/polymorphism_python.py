
# write a program polymorphism

# class tomato():
#     def type(self):
#         print("vegetable")
#
#     def color(self):
#         print("Red")
#
# class apple():
#     def type(self):
#         print("fruits")
#     def color(self):
#         print("green")
#
# def fun(obj):
#     obj.type()
#     obj.color()
#
#
# obj_tomato=tomato()
# obj_apple=apple()
#
# fun(obj_tomato)
# fun(obj_apple)

# class Bangladesh:
#
#     def captails(self):
#         print("Dhaka")
#     def langugaes(self):
#         print("frist:Bangla second:English")
#
# class USA:
#     def captails(self):
#         print("washington ,D.C")
#     def langugaes(self):
#         print("England")
# class India:
#     def captails(self):
#         print("New Delhi")
#
#
#     def langugaes(self):
#         print("Bangal ,English ,Hindie")
#
# obj_ban=Bangladesh()
# obj_USA=USA()
# obj_India=India()
#
#
# for country in (obj_ban,obj_USA,obj_India):
#     country.captails()
#     country.langugaes()

class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"cat name is {self.name} and age {self.age}")

    def make_sound(self):
        print("meow")

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"Dog name is {self.name} and age {self.age}")

    def make_sound(self):
        print("Bark")

cat1=cat("kitta",21)
dog=Dog("fluffy",4)

for animal in (cat1,dog):
    animal.info()
    animal.make_sound()


