
class cartoon:
    serices="tv serices"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)
        print(self.serices)

obj1=cartoon("Doremon",5)
obj1.display()

obj2=cartoon("shincharn",7)
obj2.display()

obj3=cartoon("Nobita",12)
obj3.display()

print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)