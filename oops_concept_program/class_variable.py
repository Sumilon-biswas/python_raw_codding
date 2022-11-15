class officer:
    #class variable
    total_employee=10

    #class constructore
    def __init__(self,emp_name,emp_age):
        self.name=emp_name
        self.age=emp_age

    # class method
    def display(self):
        print("Employee name ",self.name)
        print("Employee age ",self.age)
        print("total employee",self.total_employee)
        print("\n")

    @classmethod
    def manger(cls,m_name):
        print("maneger name is",m_name)

    @staticmethod
    def statuse():
        print("our office is today open")
        print("\n")

obj=officer("sumilon",34)
obj.display()

officer.manger("Tanbir islam")

obj.statuse()


