
#static method

class officer:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"officer name {self.name}")
        print(f"officer age {self.age}")

    @classmethod
    def manger(cls,M_name):
        print(f"Manger name {M_name}")
        print("\n")

    @staticmethod
    def case_officer():
        print("cash officer is an honest person .....")
        print("\n")

# obj=officer("joya bain",35)
# obj.show()
# officer.manger("sumilon biswas anik")
# officer.case_officer()

class Circle:
    circle_list = []
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
        # add the instance to the circle list
        self.circle_list.append(self)

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius


c1 = Circle(10)
c2 = Circle(20)

print(len(Circle.circle_list))  # 2
