
# #supper
#
# class parents:
#
#     def __init__(self,txt):
#         self.meassages = txt
#
#     def printmessages(self):
#         print(self.meassages)
#
# class child(parents):
#     def __init__(self,txt):
#      super().__init__(txt)
#
# obj=child("please don't sound my sond")
#
# obj.printmessages()

# super method use kora program



class customer:

    def __init__(self,c_name,c_address,c_phone):
        self.c_name=c_name
        self.c_address=c_address
        self.c_phone =c_phone
    def customer_info(self):
        print("customer name {} \n customer address {} \n customer phone {}".format(self.c_name,self.c_address,self.c_phone))


class office(customer):
    def __init__(self,c_name,c_address,c_phone,offices_name,today_status):
        super().__init__(c_name,c_address,c_phone)
        self.offices_name=offices_name
        self.today_status=today_status

    def status(self):
        print("Today our offices is",self.today_status)
    def officesName(self):
        print("our offices name is ",self.offices_name)
    def caseOffices(self):
        print("Total transaction = 23 core $")


class manger(office,customer):
    def __init__(self,c_name,c_address,c_phone,offices_name,today_status,mangerStatus):
        super().__init__(c_name,c_address,c_phone,offices_name,today_status)
        self.magerStatus = mangerStatus

    def leader(self):
        if self.magerStatus == "sick":
            print("Second officer lead the offices")
        else:
             print("offices lead the  office ")

#another class created second officerfmaily

class secondOfficerFmaily:
    def __init__(self,Father_name,Mother_name):
        self.Father_name=Father_name
        self.Monther_name=Mother_name
    def family_info(self):
        print("father name :{} \n  mother name :{} \n".format(self.Father_name,self.Monther_name))


class officerInformation(manger,secondOfficerFmaily):
    def __init__(self,c_name,c_address,c_phone,offices_name,today_status,mangerStatus,Father_name,Mother_name):
        manger.__init__(c_name,c_address,c_phone,offices_name,today_status,mangerStatus)
        secondOfficerFmaily.__init__(Father_name,Mother_name)



    def second_officer(self):
        print("second officer lead of alll side part development")



# class secondOfficerInformation():






# # frist  object create of class customer
#
# cus=customer("sumilon biswas","dhaka","03984978474")
# cus.customer_info()

# sceond class of office object create

# office=office("Rahule","Dhaka","944776346","ABC Bank ltd.","open")
# office.status()
# office.officesName()
# office.case_offices()
#
# office.customer_info()

# create a object manager

#   # v         c_name,       c_address, c_phone,  offices_name,today_status,mager_status
# manger=manger("jio","dhaka","937762373","LK ltd","open","sick")
# manger.leader()
# manger.customer_info()
# manger.status()
# manger.officesName()
# manger.caseOffices()

# print("=================")
#
# second_off=secondOfficerFmaily("Babale lee","Rinku lee")
# second_off.family_info()
#
information=officerInformation("Rahul", "Dhaka", "8378767", "ABC Bank", "open", "ok", "shajhan", "Rashida")
information.second_officer()

print("\ access the customer class methods")
information.customer_info()

print("\access the officer class method")
information.status()

print("\ access the manger class method")
information.leader()

print("\ access the second officer family method  ")
information.family_info()