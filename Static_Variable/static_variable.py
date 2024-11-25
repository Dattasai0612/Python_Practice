class Student:
    m1=10

    def __init__(self):
        self.m2=20

s1=Student()
s2=Student()
print("s1:",s1.m1,s1.m2)
print("s2:",s2.m1,s2.m2)
Student.m1=100
s2.m2=200
print("s1:",s1.m1,s1.m2)
print("s2:",s2.m1,s2.m2)
