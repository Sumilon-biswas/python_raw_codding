
# craete a class payrol

class Payrol():

    def __init__(self):
        self.employe_list =[]

    def add(self,employee):
        self.employe_list.append(employee)

    def printed(self):

         for e in self.employe_list:
             print(f"{e.getfullinfo} \t $ {e.getfullsalary()}")