
# def Country(**info):
#     DataBase = {}
#     for key, value in info.items():
#         DataBase[key] = value
#
#     # print(DataBase)
#
#     def NID(DataBase):
#         print(DataBase["Name"])
#         print(f"NID info: {DataBase}")
#
#     def Birthregistration(DataBase):
#         print(DataBase["Name"])
#         print(f"BirthRegistretion info: {DataBase}")
#
#     if DataBase["Age"] >= 18:
#         NID(DataBase)
#     else:
#         Birthregistration(DataBase)
#
#
# # Driven Code------------------------------------
# Country(Name="Rakib", Age=25, Location="Dhaka", Place_Of_Birth="Chandpur")
# print("\n")
# Country(Name="Hassan", Age=15, Location="Dhaka", Place_Of_Birth="Cummila")
# print("\n")
# Country(Name="Sumilon", Age=22, Location="Dhanmondi", Place_Of_Birth="Borisal")
# print("\n")
# Country(Name="Tanin", Age=17, Location="Kamrangirchar", Place_Of_Birth="Chandpur")
# print("\n")
# Country(Name="Nanin", Age=18, Location="Lalbag", Place_Of_Birth="Noakhali")
# print("\n")
# Country(Name="Sefali", Age=21, Location="Rajbari", Place_Of_Birth="Rajbari")


def country(**info):
    Database=dict()

    for keys,item in info.items():
        Database[keys]=item
    print(Database)


country(name="sumilon biswas",age=21,Rol=21,department="cse",major="computer programing")




