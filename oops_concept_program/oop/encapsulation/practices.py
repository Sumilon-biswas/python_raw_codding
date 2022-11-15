
# # create a class employee
#
# class Employee:
#
#     #declare a constructor /instances/ensliazer
#     def __init__(self,Emp_name,Emp_salary,project):
#         self.Emp_name=Emp_name
#         self.Emp_salary=Emp_salary
#         self.project=project
#
#     #create a method employee information show
#     def Emp_show(self):
#         print(f"Employee name is {self.Emp_name} and salary {self.Emp_salary}")
#
#     #create  a method project
#
#     def work(self):
#         print(self.Emp_name ," is workin on ",self.project)
#
#
# Emp=Employee("jessa",6000,"NLP")
#
# Emp.Emp_show()
# Emp.work()
#

class Employee():


    def __init__(self,emp_name,emp_salary,project):
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.project=project

    def emp_info(self):
        print(f"employe name is{self.emp_name} and salary {self.emp_salary}")

    def work(self):
        print(self.emp_name ," is working on",self.project)


emp=Employee("jerry",456876,'NIP')

emp.emp_info()
emp.work()