class Old_Exception(Exception):
    def __init__(self,arg):
        self.arg=arg

class Young_Exception(Exception):
    def __init__(self,arg):
        self.arg=arg

age=int(input("Enter Age:"))
if age>60:
    raise Old_Exception("Age exceed 60")
elif age<16:
    raise  Young_Exception("Age under 16")
else:
    print("Eligible for Policy")