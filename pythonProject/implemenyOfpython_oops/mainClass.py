from  store_page_modiul import  merchant
from  store_page_modiul import  customer
from  store_page_modiul import  Delivery_boy

import  store_modiul as sm
import  store_owner_modiul as som


customer_1=customer("Rakib","Dhanmondie","043746763","apple","Banana","orange","lemon","open","670")
customer_1.customer_info()
customer_1.plase_order()
customer_1.case()
print("\n \n")

customer_2=customer(
    "Hassain","lalbag","948988476875","Guava","watermelon","Banana","orange","open","6799"
)

customer_2.customer_info()
customer_2.plase_order()
customer_2.case()
print("\n \n")

print("======================")
print("===========================")

deliveryBoy_1=Delivery_boy(
    "Rakib","dhanmondie","838646734","apple","Banana","orange","lemon","open","450","Delivered"
)
deliveryBoy_1.plase_order()
deliveryBoy_1.delivery_status
print("\n \n")