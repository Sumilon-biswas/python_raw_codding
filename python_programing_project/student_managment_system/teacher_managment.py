
# create a teacher

class Teacher():
    def __init__(self,Tech_ID,Teach_name,Tech_address,Tech_department):
        self.Tech_ID=Tech_ID
        self.Tech_name=Teach_name
        self.Tech_address=Tech_address
        self.Tech_department=Tech_department

    def add_teacher(self,t_id,t_name,t_address,t_department):
        tech=Teacher(t_id,t_name,t_address,t_department)
        teacher_list.append(tech)

    #display teacher information

    def display_info(self,op):
        print("display all student information :")
        print("\n")
        print("Teacher Id:",op.Tech_ID)
        print("Teacher name :",op.Tech_name)
        print("Teacher address :",op.Tech_address)
        print("Teacher department :",op.Tech_department)

    # craete a function seaching()

    def seaching(self,ID):
        for i in range(len(teacher_list)):
            if (teacher_list[i].Tech_ID) ==ID:
                return  i

     #create a delect function()
    def delect(self,id):
        i=tech.seaching(id)
        del teacher_list[i]

    #create a update function

    def update(self, rn, new_rn):
        i = tech.seaching(rn)
        new_roll = new_rn
        teacher_list[i].Tech_ID = new_roll





teacher_list=[]

tech=Teacher(0,'','','')

print("call add function")
tech.add_teacher(1,"sakib sir ","green road dhaka","cse")
tech.add_teacher(2,"anupom mujandar","Barguna","computer")
tech.add_teacher(3,"sale sir","ban","EEE")
print("\n")


# print("display all information ")
# for i in range(len(teacher_list)):
#     tech.display_info(teacher_list[i])
#     print("\n")

 #searching

# print("searching the teacher list  ")
# s=tech.seaching(1)
# tech.display_info(teacher_list[s])

# delect item

# print("delect a item ")
# tech.delect(2)
# print(teacher_list.__len__())
# print("after delecting a student list ")
# for i  in range(teacher_list.__len__()):
#     tech.display_info(teacher_list[i])

tech.update(1,5)
print(teacher_list.__len__())
print("update list values of student list ")
for i in range(teacher_list.__len__()):
    tech.display_info(teacher_list[i])



