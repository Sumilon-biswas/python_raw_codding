
"""
list values pass a function arguments
"""

#create a function

def addition(mylist=[],*args):
    result=0
    for i in mylist:
        result +=i

    return result

def substraction(mylist=[],*args):
    result=mylist[0]
    n=len(mylist)
    for i in range(n-1):
        result =result-mylist[i+1]

    return  result

def multiplication(mylist=[],*args):
    result=1
    for i in mylist:
        result *=i
    return result

def division(mylist=[],*args):
    result=mylist[0]
    n=len(mylist)
    for  i in range(n-1):
        result =(result / mylist[i+1])
    return result


def intgerdivision(mylist=[],*args):
    result=mylist[0]
    n=len(mylist)
    for  i in range(n-1):
        result =(result // mylist[i+1])
    return result

mylist=[]
while True:
    user_input=input("Input values add list :")
    if user_input == '':
        break
    mylist.append(int(user_input))

print(mylist)
operators=input("choose any operators :")

if operators == '+':
    print("addition Result =",addition(mylist))
elif operators == '-':
    print("substraction result =",substraction(mylist))
elif operators == '*':
    print("multipication result =",multiplication(mylist))
elif operators == '//':
    print("division result =",division(mylist))
elif operators == '//':
    print("intager division result =",intgerdivision(mylist))
else:
    print("you seelect wrong operators !")


