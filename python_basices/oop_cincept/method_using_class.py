class cartoon:

    serise="WEB serise"

    def  __init__(self,name,age):
        self.name = name
        self.age = age


    def display(self):
        print("name=",self.name)
        print("age =",self.age)
        print("serise",self.serise)

obj1=cartoon("Doremon",10)
obj2=cartoon("mina",12)

obj1.display()
print("=====================")
obj2.display()