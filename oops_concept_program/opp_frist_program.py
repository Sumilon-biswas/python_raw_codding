
# init propertices

class cartoon:
    series="tv serices"

    def __init__(self,name,age):
        self.name=name
        self.age =age

obj=cartoon("mina",10)
obj1=cartoon("Dorimion",12)
print(obj.series)

print("====================")
print(obj.name)
print(obj.age)
print("===========")
print(obj1.name)
print(obj1.age)
print(obj1.series)