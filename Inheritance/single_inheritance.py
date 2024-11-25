class Parent:
    def greet(self):
        print("Parent Class")

class Child(Parent):
    def greet_child(self):
        print("Child Class")

c=Child()
c.greet()
c.greet_child()