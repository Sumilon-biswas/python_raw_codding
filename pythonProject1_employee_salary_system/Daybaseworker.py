
from  employee import Employee

#create a day base worker class

class Day_base_worker(Employee):

    def  __init__(self,emp_name,emp_address,emp_contact,pay,days):
        super().__init__(emp_name,emp_address,emp_contact)
        self.pay=pay
        self.days=days

    def getfullSalary(self):

        return  self.pay * self.days