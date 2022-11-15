
#frist question

p=[]
q=[]
n=int(input("Input values n:"))

for i in range(n):
    a=input("Input value p :")
    b=input("Input value q :")
    p.append(a)
    q.append(b)

# res = [p, q]
# print(res)

for i in p:
    q.append(i)
print(q)

# #second question

color1={"Red","green","orange","white"}
color2={"Black","green","white","pink"}

color3=color1 & color2
print(color3)

#thired question

list1=[1,2,3,0]
list2=["Red",'green',"black"]

for i in list1:
    list2.append(i)

print(list2)

#quetion :04

#orignial array
i=[1,3,5,7,9]
print(i)
index=2
# #remove a item  array
i.pop(index)
#printe a new array
print(i)


#example :5
string="1234abcd"
result=string[::-1]
print(result)

#example :-06

#create tuple
a={"sumilon","tanbir","joy","miraj"}
a.remove("tanbir")
print(a)

