
#multipile inhertainces

class customer:
    def customer_info(self):
        print("comuster name is Rahul ")
        print(" customer address Dhaka ")
        print("customer phone :0163533764")

class officer(customer):

    def status(self):
        print("today my offices is open")

    def employee(self):
        print("Total employee = 16")

    def case_officer(self):
        print("total transaction = 23 core ")

class manger(officer):
    def leader(self):
           print("He lead the offices")

class senior_fficer(manger,officer):
    def second_officer(self):
        print("Second officer lead the all  employeee")


#create of manger class

customer=customer()
officer=officer()

manger=manger()
manger.customer_info()
manger.status()
manger.employee()
manger.case_officer()
manger.leader()

print("senior officer object ")

print("===================================")

senior = senior_fficer()
senior.customer_info()
senior.status()
senior.employee()
senior.leader()
senior.case_officer()
senior.second_officer()



