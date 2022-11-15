
# Base class
#
class company():

    def __init__(self,name,address,project):
        self._name=name
        self._address=address
        self._project="NPN"
    def show(self):
        print(f"company name :{self._name} address :{self._address} project :{self._project}")

com=company("ABCX ltd.","Dhanmondie","NIM")
print("company name :",com._name)
print("company address :",com._address)
com._c_name="hello Bank"
com.show()


# class employe(company):
#     def __init__(self,name):
#         self.name=name
#         company.__init__(self)
#
#     def  show(self):
#         print("employee name is ",self.name)
#
#         print("\n")
#         print("working project :",self._project)
#
