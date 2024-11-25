class Test:
    a=10 #static variable

    def __init__(self):
        print("Inside Constructor")
        print(self.a)
        print(Test.a)

    def m1(self):
        print("Inside Instance Method")
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print("Inside Class Method")
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
        print("Inside Static Method")
        print(Test.a)

t=Test()
t.m1()
t.m2()
t.m3()
print("Outside Class")
print(Test.a)
print(t.a)