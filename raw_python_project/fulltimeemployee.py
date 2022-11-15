
from  employee import  employee

# creata a class full time imployee

class FulltimeEmployee(employee):

    def __init__(self,frist_name,last_name,salary):
        super().__init__(frist_name,last_name)
        self.salary=salary


    def getfullsalary(self):
        return  self.salary
