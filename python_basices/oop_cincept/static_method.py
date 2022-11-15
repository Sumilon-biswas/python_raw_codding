
# static method

class office:

    def __init__(self,name,age):
        self.name=name
        self.age = age

    def display(self):
        print("employee name :",self.name)
        print("employee age :",self.age)


    @classmethod
    def manger(cls,M_name):
        print("manger name :",M_name)

    @staticmethod

    def case_officer():
        print("our case officer is dishonest person")

obj=office("sumilon",21)
obj.display()

office.manger("Rakib")

obj.case_officer()