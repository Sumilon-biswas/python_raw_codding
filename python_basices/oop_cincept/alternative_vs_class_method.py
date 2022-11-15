
# Example of inhertainces

class Customer:

    def __init__(self,c_name,c_address,c_phone):
        self.c_name=c_name
        self.c_address=c_address
        self.c_phone=c_phone

    def customer_inforamtion(self):
        print("Customer name {} \n Customer Address {} \n Customer phone {}".format(self.c_name,self.c_address,self.c_phone))

class office(Customer):

    def __init__(self,c_name,c_address,c_phone,office_name,today_status):
        super().__init__(c_name,c_address,c_phone)
        self.office_name=office_name
        self.today_status=today_status

    def officeStatuse(self):
        print("Today our offices is ".format(self.today_status))

    def officeName(self):
        print("Our offices name is ".format(self.office_name))

    def case_offices(self):
        print("Total transaction = 123000 BDT ")

class Manger(office,Customer):
    def __init__(self,c_name,c_address,c_phone,office_name,today_status,manger_status):
        super().__init__(c_name,c_address,c_phone,office_name,today_status)
        self.manger_status=manger_status

    def leader(self):
        if self.manger_status == "sick":
            print("Senior officer lead the offices")
        else:
            print("Manger lead Our offices")




#create a object customer classs
# customer=Customer("Dankar pille","Landon","74674656743")
# print("Customer name ",customer.c_name)
# print("Customer Address ",customer.c_address)
# print("Customer Phone ",customer.c_phone)
# customer.customer_inforamtion()

# create a object office class

# office=office("Rahul","India","876766","ABC Bank","open")
# # print("Customer name ",office.c_name)
# # print("Customer Address ",office.c_address)
# # print("Customer Phone ",office.c_phone)
# print(" Our company name is ".format(office.office_name))
# print("Our company status ".format(office.today_status))
#
# office.officeStatuse()
# office.officeName()
# office.case_offices()
# print("\n accses the customer class ")
# office.customer_inforamtion()

#create a object Manger class

manger=Manger("liton Das","Dhaka","8784573465","BCB(Bangladesh cricket Board)","open","find")
manger.leader()
print("\n access the officer classs")
manger.officeStatuse()
manger.officeName()
manger.case_offices()
print("\n acces the customer class")
manger.customer_inforamtion()
