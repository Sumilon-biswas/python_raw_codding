import keyword

# frist function captlization
#
# name="I LOVE PYTHON"
# print(name.capitalize())
# print("=================")
# name1="i love python"
# print(name1.capitalize())

# sentence = "Python is awesome"
#
# # returns the centered padded string of length 24
# new_string = sentence.center(24, '*')
#
# print(new_string)

# sentence = "Python is awesome"
#
# # returns the centered padded string of length 20
# new_string = sentence.center(20, '$')
#
# print(new_string)

# sentence ="Python is awasome."
# new_string=sentence.center(20,'$')
# print(new_string)
#
# person_name=" sumilon biswas anik"
#
# new_person =person_name.center(26,'&')
# print(new_person)

# txt = "pyTHon"
# new_txt = txt.casefold()
# print(new_txt)

# per_name ="suMIloN BISwas AnIK"
# new_person =per_name.casefold()
# print(new_person)

# count function

# messages="python is mostly populare languages in the world"
# new_msg=messages.count('p')
# print("number of characters count :",new_msg)
# myName="sumilon biswas anik"
# print("number of character count :",myName.count('s'))
# print("number of character count :",myName.count('o'))
# print("number of character  count :",myName.count('i'))
# print("number of character count :",myName.count('n'))

# string ="python is awasome program languages"
# mystring ="is"
# print("number of character of substring",string.count(mystring))
#
# string="python best programing languages. python is mostly popular languages.python way to easy learn"
# substring="python"
# substring1="languages"
# print("number of python is:",string.count(substring))
# print("number of pythons is :",string.count(substring1))

# myExap="xyz\t7876\t @gmail.com\t 657Dd"
# print(myExap.expandtabs())

# myname="sumilon \t biswas \t anik \t"
# print(myname.expandtabs())

#python find method

# messages="python is a fun programing languages"
# result=messages.find('fun')
# print(result)
# print(messages.find('languages'))
# print(messages.find("python"))
# print(messages.find("programming"))

# programing="python programing languages"
# relases=1981
# Authore="Guido van resuim"
#
# print("full resut is",programing,relases,Authore)
#
# print(f"name of programing languages :{programing} relases time {relases},Authorites :{Authore}")
#
# print("name of programing languages {} relases time {} Authorites {}".format(programing,relases,Authore))
#
# name =input("Enter you name:")
# age=int(input("Input of age :"))
# profession =input("Input your profession :")
#
# print(name,age,profession)
# print(f"person name is :{name} age :{age} profession :{profession}")
# print("========================")
# print("person name is {} ages is :{} profession :{}".format(name,age,profession))
#
# print("===================")

# print("Hello {} , your balances of:{}$".format("adnam","48365"))
# print("hello {name} your balances {balances}$".format(name="sumilon biswas anik",balances=56465.87))
# print("hello {}, you are balances {}".format("anika Rahman",63553.65))

#python isidentity method

# string ="python"
# print(string.isidentifier())
# string1=" py thon"
# print(string1.isidentifier())
#
# string2="3python is "
# print(string2.isidentifier())
#
# nme="sumilon biswas anik"
# print(nme.isidentifier())
# name="sumilonbiswasanik"
# print(name.isidentifier())

# str ="sumilon123"
# if str.isidentifier()== True:
#     print("this is valid identifer")
# else:
#     print("this is not identifier")
#
# str1="45sumilon"
#
# if str1.isidentifier()== True:
#     print("this is valide identifer")
# else:
#     print("this is not valid indentifer ")

print(keyword.iskeyword("break"))
print(keyword.iskeyword("False"))
print(keyword.iskeyword("sumilon"))
print(keyword.iskeyword("if"))


