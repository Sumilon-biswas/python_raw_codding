
#encapsulation

class Bank:
    def __init__(self,transection):
        self.B_name="Bangladesh Banks"
        self.address="motijheel"
        self.case=190948
        self.transection=transection

    def Bank_info(self):
        print("Bank name :",self.B_name)
        print("Address :",self.address)

    def Account(self):
        print("Total case ",self.case)
        print("transection ",self.transection)

class customer(Bank):

    def __init__(self,transection,c_Name,c_AccountNumber):
        super().__init__(transection)
        self.c_name=c_Name
        self.c_AccountNumber=c_AccountNumber

    def customer_info(self):
        print("customer  info :",self.c_name)
        print(" Account number :",self.c_AccountNumber)

    def customer_Acc_info(self):
        print("Total cash :",self.case)
        print("transation :",self.transection)

class Bank_employee(Bank):

    def __init__(self,transection):
        super().__init__(transection)

    def employeecheakAccount(self):
        print("total cash ",self.case)
        print("transection ",self.transection)


print("customer")

cus1=customer(50000,"rakib",434444)
cus1.customer_info()
print("\n")
cus1.customer_Acc_info()