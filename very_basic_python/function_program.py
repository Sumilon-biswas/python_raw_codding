
"""
function is a code of block when use function just call

syntax of function

use key=def
1)def full from defination of function
2) function name
5:()
4:parameter
3)colon
4)block

5) function calling


def  function_name(paramater):
     block of code

then calling function

function_name()

"""
#
# def greeting_fun():
#     print("Hi!")
#
# greeting_fun()
# greeting_fun()

# def languagesName(name):
#     print(name)
#
# languagesName("python programing languages")
# languagesName("pHp programing languages ")
# languagesName("javascript languages ")

"""
function to types 
1)none return function
2)returen function
"""

# def myfunction(name):
#     return name
# print(myfunction("hello! john Doie"))

# def function_info(neme):
#     return neme
# print(function_info("programing best languages pythons!"))

# multipal data paramater passing in function
#
# def sum(a,b):
#     return  a + b
#
# num1=int(input("Input number1 :"))
# num2=int(input("Input number 2:"))
# result=sum(num1,num2)
# print("total summation =",result)

#defualt parametera function

# def greeta(name,messages="Hi!"):
#     print(name,messages)
#
# greeta("john Doie")


# python keyword arguments

# def get_prices_net(prices,discount):
#     return  prices *(1-discount)
#
# price=int(input("prices values :"))
# discount=0.1
#
# net_price=get_prices_net(price,discount)
# print("net prices values :",net_price)

#net discount

# def get_net_discount(price,discount):
#     return (price*discount)/100
#
# result =get_net_discount(200,10)
# print(result)
#
# def get_prices_net(prices,discount):
#     return  prices *(1-(discount/100))
#
# price=int(input("prices values :"))
# discount=float(input("Input discount :"))
# print(discount)
#
# net_price=get_prices_net(price,discount)
# print("net prices values :",net_price)


#keyword function

def get_net_prices(prices,tex=0.07,discount=0.09):
    return  prices * (1+tex-discount)

result=get_net_prices(200)
print(result)


print(" ")


res=get_net_prices(100)
print(res)

