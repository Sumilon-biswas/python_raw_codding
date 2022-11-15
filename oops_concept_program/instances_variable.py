
class officer:

    total_employee=10

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("officer name is ",self.name)
        print("officer age",self.age)
        print("total employee",self.total_employee)

    @classmethod
    def manager(cls,m_name):
        print("manager name :",m_name)
        print("total employee :",cls.total_employee)
        print("\n")

    @staticmethod
    def status():
        print("our office is open today...")
        print("\n")

obj=officer("Rakib",25)
obj.display()

officer.manager("sumilon  biswas ")

obj.status()