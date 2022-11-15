class student:
    def __init__(self,id,name,marks,Department):
        self.std_id = id
        self.std_name=name
        self.std_marks=marks
        self.department=Department

    def get_gruad(self):
        if self.std_marks >= 40 and self.std_marks <= 49:
            return  'D'
        elif self.std_marks >= 50 and self.std_marks <= 59:
            return  'c'
        elif self.std_marks >= 60 and self.std_marks <=69:
            return  'B'
        elif self.std_marks >= 70 and self.std_marks <=79:
            return  'A'
        elif self.std_marks >= 80 and self.std_marks <= 100:
            return "A+"
        else:
            return "your not pass the exam"
    def display_all_information(self):
        print("student Id {}".format(self.std_id))
        print("student name {}".format(self.std_name))
        print("student marks {}".format(self.std_marks))
        print("student gruade {}".format(self.get_gruad()))

std=student("21","sumilon biswas",66,"Cse")
std.display_all_information()

std1=student("100","joya bain",80,"cse")
std1.display_all_information()