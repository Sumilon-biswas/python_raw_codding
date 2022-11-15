# class office:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show(self):
#         print("Employee name  :",self.name)
#         print("Employee ages :",self.age)
#
#     @classmethod
#     def maneger(cls,M_name):
#         print("manger name:",M_name)
#
# obj=office("sumilon biswas anik",34)
# obj.show()
# office.maneger("sumiya sarker Bangladesh")

class teacher:
    def __init__(self,t_name,t_age,t_department):
        self.t_name=t_name
        self.t_age=t_age
        self.t_department=t_department

    def show(self):
        print(f"teacher name {self.t_name} age {self.t_age} and department{self.t_department}")

    @classmethod
    def student(cls,std_name,std_department):
        print(f"student name {std_name} and department {std_department}")

teach=teacher("sakib sir",38,"cse")
teach.show()

teacher.student("sumilon","cse")
