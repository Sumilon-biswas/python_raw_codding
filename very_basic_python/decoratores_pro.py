

# #Decirators
#
# def full_name(lastName):
#     print("sumilon")
#     lastName()
#
# def lastName():
#     print("biswas anik")
#
# full_name(lastName)


# def full_name_information(funch1,funch2):
#
#
#     funch1()
#     funch2()
#     print("dislpaye the full name .....")
#
#
# def frist_name():
#    print("sumilon")
#
#
# def lastName():
#    print("biswas ")
#
# full_name_information(frist_name,lastName)

#
# def full_name_information(funch1,funch2):
#
#
#     print(funch1())
#     print(funch2())
#     print("dislpaye the full name .....")
#
#
# def frist_name():
#    return "sumilon"
#
#
# def lastName():
#    return "biswas "
#
# full_name_information(frist_name,lastName)


#Example of Decirtore function
# def shout(text):
#     return text.upper()
#
# print(shout("sumilon biswas"))
#
# def shout(text):
#     return  text.upper()
#
# print(shout("Bangladesh"))

# def txt_uppper(txt):
#     return  txt.upper()
#
# def whisper(text):
#     return text.lower()
#
# def information(funch1):
#     # res=funch1("Bngladesh cricket team!")
#     res1=funch1("SAKIBAL ALL HASAN IS GOOD PLAYER OF BANGLADSH CRICKET TEAM")
#     # print("Result is ",res)
#     print(res1)
# #information(txt_uppper)
# information(whisper)

# def text_uppor(txt):
#     return  txt.upper()
# # print(text_uppor("sumilon"))
# def text_lower(txt):
#     return  txt.lower()
#
# # print(text_lower("DHAKA IS  A CAPTAIL OF BANGLADESH"))
#
# def case_value_info(funct):
#
#     res=funct("Dhaka international univeesity!")
#     print(res)
#
# case_value_info(text_uppor)
# print("casting the lower value")
# case_value_info(text_lower)

# def ordinary():
#     print("I am ordinary boys !")
#
# def make_pretty(funch):
#     def inner_fun():
#         print("I am got Dectorated !")
#     funch()
#     return  inner_fun()
#
#
# make_pretty(ordinary)

# def di__Decatorte(funch):
#     def inner(x,y):
#         if y==0:
#             return "Give proper values"
#         return funch(x,y)
#     return  inner
#
# # @di__Decatorte
# def div(a,b):
#     return a / b
# result=di__Decatorte(div)
# result=div(4,2)
# print(result)
#
# result1=div(4,2)
# print(result1)

# def div___decatore(funch):
#     def innerfun(x,y):
#         if y==0:
#             return "please! give a proper values ."
#         return funch(x,y)
#     return innerfun
#
# @div___decatore
# def div(a,b):
#     return  a // b
#
# resultt=div(4,3)
# print(resultt)
