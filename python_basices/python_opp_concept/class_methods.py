# from datetime import date
#
#
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age = age
#
#     @classmethod
#     def fromBirthyearOF(cls,name,dateofbirthyear):
#         return cls(name,date.today().year - dateofbirthyear)
#
#     def displayShow(self):
#         print(f"person name is {self.name} and age {self.age}")
#
#
# person=person("john",19)
# person.displayShow()
#
# person1=person.fromBirthyearOF("Adnan",1990)
# print(person1.displayShow())


class employee:
    no_a_leaves= 8
    def __init__(self,name,salary,post):
        self.Emp_name=name
        self.Emp_salary=salary
        self.Emp_post =post
    def dislpayShowing(self):
        print(f"Employee Name {self.Emp_name} salary {self.Emp_salary} post {self.Emp_post} and ")

    @classmethod
    def create_class_method(cls,new_on_leaves):
         cls.no_a_leaves=new_on_leaves


emp=employee("joya bain",30000,"python programer")
print(emp.no_a_leaves)

emp1=employee.create_class_method(89)
