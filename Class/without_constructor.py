class Student:
    def getdata(self):
        self.id=int(input("Enter Id:"))
        self.name=input("Enter Name:")
        self.address=input("Enter Adress:")

    def display(self):
        print("Student Id:",self.id)
        print("Student Name:",self.name)
        print("Student Address:",self.address)

s1=Student()
s1.getdata()
s1.display()