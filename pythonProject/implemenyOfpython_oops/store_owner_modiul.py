
from  store_page_modiul import  merchant

#create the owner modiule

class Owner(merchant):

    def __init__(self,c_name,c_address,c_phone,item1,item2,item3,item4,today_statuse,prices):
        super().__init__(c_name,c_address,c_phone,today_statuse,prices)

    def Owner_info(self):
        print("Owner information  ")
        print("MD:shajhan mia")
        print("age:55")