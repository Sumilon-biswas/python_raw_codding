
#class method

class opffice:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def show(self):
        print(self.name)
        print(self.age)


    @classmethod
    def manger(cls,M_name):
        print("Manger name:",M_name)

obj=opffice("Hassan",24)
obj.show()

opffice.manger("sumilon biswas")
