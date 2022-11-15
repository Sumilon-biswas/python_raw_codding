
#multiple Inheritances

class customer:

    def customer_info(self):
        print("customar name : Rakib islam")
        print("customer address :Dhaka")
        print("customar phone :0387673463")

class officer(customer):

    def status(self):
        print("Today our offices is open")

    def employee(self):
        print("Total employee =10 ")


    def case_office(self):
        print("Total transaction = 2000000 BDT ")

class manger(officer,customer):

    def leader(self):
        print("He is lead the offices")


class senior_offices(manger,customer):
      def second_officer(self):
          print("senior officer lead all the Employee ....!")



officer=officer()
officer.status()
officer.employee()
officer.case_office()
officer.customer_info()

print("=================\n \n")




manger=manger()

manger.leader()
manger.status()
manger.employee()
manger.case_office()

print("===================\n \n")

senior_offices=senior_offices()

senior_offices.second_officer()
senior_offices.leader()
senior_offices.status()
senior_offices.employee()
senior_offices.case_office()


