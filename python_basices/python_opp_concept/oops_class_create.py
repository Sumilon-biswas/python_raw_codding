
# #class created
#
# # created a new class
# class Dog():
#     # class attributes
#     attri="animals"
#
#     #instances attributes of class
#     def __init__(self,name):
#         self.name =name
#
# # # create  object
# # obj=Dog()
#
# # object instantiation
# Rodger=Dog("Rodger")
# Tommy=Dog("Tommy")
#
# #Access the class attributies
# print("Rodger is a {}".format(Rodger.__class__.attri))
# print("Tommy is a {}".format(Tommy.__class__.attri))
#
# # accsess the class instainces methods
# print("this is name{}".format(Rodger.name))
# print("this is name {}".format(Tommy.name))
#

# class Dog():
#
#     attri="animals"
#     def __init__(self,name):
#         self.name=name
#
# #create of object
# Rodger=Dog("Rodger")
# Tommy=Dog("Tommy")
#
# #access the class attributes
# print("Rodger is a {}".format(Rodger.__class__.attri))
# print("Tommy is a {}".format(Tommy.__class__.attri))
#
# #access th class instances
# print("this name is ".format(Rodger.name))
# print("this name is ".format(Tommy.name))


# class Dog:
#
#     attri="animals"
#     def __init__(self,name):
#         self.name = name
#     def called(self):
#         print("this name is {}".format(self.name))
#
# #created new object
# obj=Dog("Radger")
# obj1=Dog("Tommy")
#
# # accessing the class method
# obj.called()
# obj1.called()

# inhertainces

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

#
# class person:
#     def __init__(self,Idnumber,name):
#         self.id=Idnumber
#         self.name=name
#     def display(self):
#         print(self.id)
#         print(self.name)
#     def  detalise(self):
#         print(" Sl No {}".format(self.id))
#         print("my neme is ".format(self.name))
#
# class employee(person):
#     def __init__(self,Idnumber,name,salary,post):
#         self.salary =salary
#         self.post=post
#         person.__init__(self,Idnumber,name)
#
#     def detalis(self):
#         print("Employee Id {}.".format(self.id))
#         print("Employee name {}".format(self.name))
#         print("employee salary {}".format(self.salary))
#         print("Employee post {}".format(self.post))
#
# emp=employee("01","sumilon biseas",300000,"python programer")
# emp.display()
# print("========================")
# emp.detalis()
#
# emp1=employee("01","Rahule",300000,"java developer")
# emp1.display()
# print("=======================")
# emp.detalis()

class employee:
    pass

emp=employee()
emp.name="sumilon biswas"
emp.salary=30000
emp.role="python programer"
print(emp.__dict__)

emp1=employee()
emp1.name="mono software architecture"
emp1.salary=7777777
emp1.role="c# developer"


print(emp1.name)
print(emp1.role)
print(emp1.__dict__)