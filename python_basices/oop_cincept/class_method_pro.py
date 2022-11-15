class  officer:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("employee Name :",self.name)
        print("employee age :",self.age)

    @classmethod
    def craete_manger(cls,M_name):
        print("manger name :",M_name)

obj=officer("Rakin",10)
obj.show()

officer.craete_manger("sumilon biswas")
