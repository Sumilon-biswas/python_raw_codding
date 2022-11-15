
#method using in class

class cartoon:
    '''

       **** this is class will be created by sumilon biswas anik ******
       *** this is python  programin **** world


    '''

    series="tv series"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)
        print(self.series)

obj=cartoon("Doremion",29)
obj.display()
print("=======================")
obj1=cartoon("mina",40)
obj1.display()

print(cartoon.__doc__)
