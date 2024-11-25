class Student:
    a="Dattasai" #static variable

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        print((self.m1+self.m2+self.m3)/3)

    @classmethod
    def m1(cls):
        print(cls.a)

    @staticmethod
    def add(a,b):
        print("Sum is:",a+b)

    @staticmethod
    def f1():
        print("Hello")

s1=Student(70,88,92)
s2=Student(80,86,94)
s1.avg()
s2.avg()

Student.m1()

s1.add(10,20)

s1.f1()