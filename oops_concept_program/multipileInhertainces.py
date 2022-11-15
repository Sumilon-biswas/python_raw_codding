
# multipile_Inhertainces

class customer:

    def customer_info(self):
        print("Customer name:: Rahule ")
        print("Customer address:: Green Road panthopath-123,Dhaka")
        print("Customer Phone :: 0172535344")
class office(customer):

    def status(self):
        print("Today our offices is open")

    def employee(self):
        print("total employee =20")

    def case_officer(self):
        print("total transation =23 core")

class manager(office,customer):

    def laeader(self):
        print("He is leader  the officer")

class senior_officer(manager,office,customer):

    def senior_officer(self):
        print("sebior officer lead of offices")

manager=manager()
manager.customer_info()
manager.status()
manager.employee()
manager.case_officer()
manager.laeader()

print("\n")


print("=======================")


senior_officer=senior_officer()
senior_officer.customer_info()
senior_officer.status()
senior_officer.employee()
senior_officer.case_officer()
senior_officer.laeader()
senior_officer.senior_officer()
