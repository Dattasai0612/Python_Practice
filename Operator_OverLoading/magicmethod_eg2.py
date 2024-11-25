class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __mul__(self, other):
        return self.salary*other.days

class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days

e=Employee("Datta", 500)
t=Timesheet("Datta", 25)
print("Salary:",e*t)