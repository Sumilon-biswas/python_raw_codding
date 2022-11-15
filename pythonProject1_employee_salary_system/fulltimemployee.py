
from  employee import Employee

#create a fulltimeemployee

class FullTimeemployee(Employee):
    def __init__(self,emp_name,emp_addres,emp_contact,salary):
        super().__init__(emp_name,emp_addres,emp_contact)
        self.salary=salary

    def getfullSalary(self):
        return  self.salary

