
#create a store class
class storage:
    def __init__(self,amount_apple):
        self.amount_apple=amount_apple

    def apple(self):
        print("apple={}Kg".format(self.amount_apple))

#create a shop recent
class  shop_recent:

    def __init__(self,rent):
        self.rent=rent

    def Rent(self):
        print("shop Rent ={} BDT".format(self.rent))

