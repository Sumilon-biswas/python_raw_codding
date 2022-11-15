

#create a merchant class

class merchant:

    def __init__(self,item1,item2,item3,item4,today_statuse,prices):
        self.item1=item1
        self.item2=item2
        self.item3=item3
        self.item4=item4
        self.today_statuse=today_statuse
        self.prices=prices

    def status(self):
        print("oday our store is :",self.today_statuse)

    def products(self):
        print("Our products display .....")
        print("{}".format(self.item1))
        print("{}".format(self.item2))
        print("{}".format(self.item3))
        print("{}".format(self.item4))

    def case(self):
        print("Total prices  = {} BDT".format(self.prices))

#create a class customer

class customer(merchant):
    def __init__(self,c_name,c_address,c_phone,item1,item2,item3,item4,today_statuse,prices):
        super().__init__(item1,item2,item3,item4,today_statuse,prices)

        self.c_name=c_name
        self.c_address=c_address
        self.c_phone=c_phone

    def customer_info(self):
        print("Customer name = {} \n customer address ={} \n customer phone ={}".format(self.c_name,self.c_address,self.c_phone))

    def plase_order(self):
        print("print plase order ::{},{},{},{}".format(self.item1,self.item2,self.item3,self.item4))

# create a class Delivery_boy
class Delivery_boy(customer,merchant):
    def __init__(self,c_name,c_address,c_phone,item1,item2,item3,item4,today_statuse,prices,delivery_status):
        super().__init__(c_name,c_address,c_phone,item1,item2,item3,item4,today_statuse,prices)
        merchant.__init__(item1,item2,item3,item4,today_statuse,prices)

        self.delivery_status=delivery_status

    def dlivery_status(self):
        if self.delivery_status == "Delivered":
            print("ALl product have been delivered")
        else:
            print("product deliver soon")