
#HIgrarchical inheritances


class officer:
    def ststus(self):
        print("Today our offices is open")

    def employee(self):
        print("Total  employee = 10")

    def  case_officer(self):
        print("Total transaction = 1500000 BDT")
class manger(officer):

    def leader(self):
        print("He lead the offices ")

class senior_officer(officer):
    def senior_officer(self):
        print("senior officer lead the Employee")

# object created manger class


obj=manger()

obj.ststus()
obj.employee()
obj.case_officer()
obj.leader()

print("===========================")

obj1=senior_officer()
obj1.ststus()
obj1.employee()
obj1.case_officer()
obj1.senior_officer()