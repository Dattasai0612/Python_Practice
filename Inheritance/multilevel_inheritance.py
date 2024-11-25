class Grandparent:
    def greet_grandparent(self):
        print("Grandparent")

class Parent(Grandparent):
    def greet_parent(self):
        print("Parent")

class Child(Parent):
    def greet_child(self):
        print("Child")

c=Child()
c.greet_grandparent()
c.greet_parent()
c.greet_child()