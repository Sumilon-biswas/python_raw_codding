
# creata class hourly basse employee

from  employee import  employee

class HourlybaseEmployee(employee):

    def __init__(self,frist_name,last_name,salary,working_hours):
        super().__init__(frist_name,last_name)
        self.salary=salary
        self.working_hour=working_hours

    def getfullsalary(self):
        return  self.salary * self.working_hour
