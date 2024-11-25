class Student:
    def __init__(self):
        self.a=10

    def mark(self):
        self.b=20

s1=Student()
s1.mark()
s1.c=30
print(s1.__dict__)