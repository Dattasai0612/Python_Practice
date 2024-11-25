class Student:
    def __init__(self):
        self.id=1
        self.name="Datta"

    def details(self):
        print("Inside of Class")
        print(self.id)
        print(self.name)

s1=Student()
s1.details()
print("Outside of Class")
print(s1.id)
print(s1.name)