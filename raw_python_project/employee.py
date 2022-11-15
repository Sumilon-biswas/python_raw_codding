
"""
Suppose that you need to develop a payroll program for a company.

The company has two groups of employees: full-time employees and hourly employees. The full-time employees get a fixed salary while the hourly employees get paid by hourly wages for their services.

The payroll program needs to print out a payroll that includes employee names and their monthly salaries.
"""
from  abc import  ABC,abstractmethod
class employee(ABC):

    def __init__(self,frist_name,last_name):
        self.frist_name=frist_name
        self.last_name=last_name



    @property
    def getfullinfo(self):
        return f"employee name: {self.frist_name} {self.last_name}"


    @abstractmethod

    def  getfullsalary(self):
        pass
