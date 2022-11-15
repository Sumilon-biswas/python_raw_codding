
class emloyee():

    #constructor
    def __init__(self,name,salary):
        #public data member
        self.name=name
        self.salary=salary

    # instante method
    def show(self):
        #accessing the public data
        print(f"Employee name {self.name} and salary {self.salary}")


#create a employee class object

emp=emloyee("sumilon",2300)

#access the public data member variable
print("name :",emp.name,",","salary :",emp.salary)

# access the public data methods
emp.show()