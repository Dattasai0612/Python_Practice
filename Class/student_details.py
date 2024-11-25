class Student:
    def __init__(self):
        self.sname = "datta"
        self.sroll = 12
        self.saddress = "hyd"

    def display(self):
        print("Student Name is:", self.sname)
        print("Student Rollno is:", self.sroll)
        print("Student Address is:", self.saddress)


s1 = Student()
s1.display()
