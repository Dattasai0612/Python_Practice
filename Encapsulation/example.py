class Parent:
    x=10
    _y=20
    __z=30

class Child(Parent):
    print(Parent.x)
    print(Parent._y)
    # print(Parent.__z) #Error