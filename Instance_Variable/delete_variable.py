class Student:
    def __init__(self):
        self.id=1
        self.name="Datta"

    def details(self):
        print("Student Id:",self.id)
        print("Student Name:",self.name)

s1=Student()
s1.details()
print(s1.__dict__)
del s1.id
print(s1.__dict__)