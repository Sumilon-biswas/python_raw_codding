
# class variable program

class offfice :
    # declare the class variable
    total_employee = 10

    def __init__(self,name,age):
        self.Name = name
        self.age = age

    def show(self):
        print("Employee name is ",self.Name)
        print("Employee age :",self.age)
        print("Total employee :",self.total_employee)

    @classmethod
    def manger(cls,M_name):
        print("Manger name  ",M_name)

    @staticmethod
    def status():
        print("today our offices is open ......")

obj=offfice("Rakib",34)
obj.show()

offfice.manger("sumilon")

obj.status()
offfice.status()


