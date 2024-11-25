class Student:
    def __init__(self,a,b,c):
        self.id=a
        self.name=b
        self.address=c
s1=Student(1,"Datta","Hyd")
print(s1.__dict__)