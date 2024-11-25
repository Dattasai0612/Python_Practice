class Student:
    def __init__(self,x,y,z):
        self.sid=x
        self.sname=y
        self.saddress=z

    def display(self):
        print("Student Id:",self.sid)
        print("Student Name:",self.sname)
        print("Student Address:",self.saddress)

s1=Student(1,"Datta","Hyd")
s1.display()
        