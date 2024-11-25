class Test:
    def m1(self):
        print("No Arg Method")

    def m1(self,a):
        print("One Arg Method")

    def m1(self,a,b):
        print("Two Arg Method")

t=Test()
# t.m1()
# t.m1(10)
t.m1(10,20)