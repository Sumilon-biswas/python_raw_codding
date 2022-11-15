
#Hierarchical Inheritance

class officer:

    def status(self):
        print("Today  our office is open")

    def employee(self):
        print("Total employee == 12")

    def case_officer(self):
        print("today total transagation = 14 core")

class manager(officer):

    def leader(self):
        print("He is leader in my offices")


class senior_officer(officer):

    def second_officer(self):
        print("second senrion officer lead the employee")

manager=manager()
manager.status()
manager.employee()
manager.case_officer()
manager.leader()

print("++++++++++++++++++++++++++++++++++++")

senior_officer=senior_officer()
senior_officer.status()
senior_officer.employee()
senior_officer.case_officer()
senior_officer.second_officer()


