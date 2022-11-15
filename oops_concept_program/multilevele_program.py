
# meultilivele inhertaince program

class offices:

    def status(self):
        print("Today our offices  is  open")

    def employee(self):
        print("Total employee = 15")


    def case_status(self):
         print("total transaction = 17000 core")

class managere(offices):

    def leader(self):
        print("He is leader of my offices...")

class senior_officer(managere):

    def second_officer(self):
        print("He is senior officer in our offices")

obj=offices()
obj1=managere()
senior_officer=senior_officer()
senior_officer.status()
senior_officer.employee()
senior_officer.case_status()
senior_officer.leader()
senior_officer.second_officer()


