class office:
    def status(self):
        print("today our offices is open")

    def employee(self):
        print("total employee =15")

    def Manger(self):
        print("total Transaction =2500000BDT")

class heardofiices(office):

    def leader(self):
        print("He lead in the offices....")


obj=heardofiices()
obj.status()
obj.employee()
obj.Manger()
obj.leader()