class officer:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)

    @classmethod
    def Manger(cls,m_name):
        print("our offic manager name is",m_name)

    @staticmethod
    def case_officer():
        print("case_officer is an honest person in our offices...")

obj=officer("Rakib",50)
obj.display()

officer.Manger("Sumilon")
obj.case_officer()