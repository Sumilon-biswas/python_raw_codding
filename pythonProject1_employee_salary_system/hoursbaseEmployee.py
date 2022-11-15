
from employee import  Employee

#create a class hours base employee

class  HoursBaseEmployee(Employee):

    def __init__(self,emp_name,emp_address,emp_contact,base_pay,working_hours):
        super().__init__(emp_name,emp_address,emp_contact)

        self.base_pay=base_pay
        self.working_hours=working_hours

    def getfullSalary(self):
        return  self.base_pay * self.working_hours