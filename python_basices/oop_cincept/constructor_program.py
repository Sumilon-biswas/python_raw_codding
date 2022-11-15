
#python constructor intlization

class cartoon:
    serise="TV serise"

    def __init__(self,name,age):

        self.name = name
        self.age = age

    def display(self):
        print("cartoon name is {} benganing years {}".format(self.name,self.age))


obj1=cartoon("mina",20)
obj2=cartoon("shincharn",12)


print("++++++======")
print(obj1.name)
print(obj1.age)
print(obj1.serise)
obj1.display()


print("second object accessing")
print("\n")
print("\n")

print(obj2.name)
print(obj2.age)
print(obj2.serise)
obj2.display()