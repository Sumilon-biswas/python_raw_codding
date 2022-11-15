
# creata a clss  employee
from  abc import ABC,abstractmethod


class Employee():

    def __init__(self,emp_name,emp_addres,emp_contact):
        self.emp_name=emp_name
        self.emp_address=emp_addres
        self.emp_contact=emp_contact

    @property
    def full_info(self):
        return f"employee name {self.emp_name} address :{self.emp_address} contact:{self.emp_contact}"

    @abstractmethod
    def getfullSalary(self):
        pass