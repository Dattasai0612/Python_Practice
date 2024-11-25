class Parent:
    def __init__(self):
        print("Parent Class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Class")

c=Child()
