class Test:
    def __init__(self):
        print("No Arg Constructor")

    def __init__(self,a):
        print("One Arg Constructor")

    def __init__(self,a,b):
        print("Two Arg Constructor")

# t=Test()
# t=Test(10)
t=Test(10,20)