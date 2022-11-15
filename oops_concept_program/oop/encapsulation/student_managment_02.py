#student management system python use on class
# class student:
#      def __init__(self,name,rollno,m1,m2):
#          self.name=name
#          self.rollno=rollno
#          self.m1=m1
#          self.m2=m2
#
#      # adding student data
#      def inserted(self,name,RollNo,mark1,mark2):
#
#          ob=student(name,RollNo,mark1,mark2)
#          ls.append(ob)
#
#      def display(self,ob):
#          print("\n")
#          print("Student name :",ob.name)
#          print(" student Roll :",ob.rollno)
#          print(" student mark1 :",ob.m1)
#          print("student mark2 :",ob.m2)
#          print("\n")
#
# ls=[]
#
# ob=student('',0,0,0)
#
# print("\nOperations used, ")
# print("Inserted operation ")
#
# ob.inserted("sumilon biswas",21,50,60)
# ob.inserted("Rupok Das",23,60,70)
# ob.inserted("summon khan",24,70,90)
# ob.inserted("Ripon sarker",26,80,90)
#
# print("\n")
#
# print("display student list =")
#
# for i in range(ls.__len__()):
#     ob.display(ls[i])

class student():

    def __init__(self,name,rollno,m1,m2):
        self.name=name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2

    def accept(self,name,Rollno,mark1,mark2):

        ob=student(name,Rollno,mark1,mark2)
        mylist.append(ob)

    def display(self,ob):
        print("\n")
        print("student name :",ob.name)
        print(" student Roll :",ob.rollno)
        print(" mark_1 :",ob.m1)
        print("mark_2 :",ob.m2)
        print("\n")
    #searchin data a
    #search function
    def search(self,rn):
        for i in range(mylist.__len__()):
            if (mylist[i].rollno == rn):
                return  i


    #delect function()
    def delect(self,rn):
        i=std.search(rn)
        del mylist[i]

    # update class
    def update(self,rn,RollNO):
        i=std.search(rn)
        new_roll=RollNO
        mylist[i].rollno=new_roll




mylist=[]

std=student('',0,0,0)

print(" insert method class ")
std.accept("sumilon biswas",21,60,50)
std.accept("Ripon sarker",26,90,70)

print(" \n")

print("\n Student Found, ")
s = std.search(21)
std.display(mylist[s])

print("==============")
ss=std.search(21)
std.display(mylist[ss])

print("delect data a student list ")
std.delect(26)
print(mylist.__len__())
print("List after deletion")
for i in range(mylist.__len__()):
    std.display(mylist[i])

print("update student roll")
std.update(21,27)
print(mylist.__len__())
print("afer list update")
for i in range(mylist.__len__()):
    std.display(mylist[i])
print("thanks program!")