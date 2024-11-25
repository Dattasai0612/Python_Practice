class Parent:
    def greet_parent(self):
        print("Parent")

class Child1(Parent):
    def greet_child1(self):
        print("Child1")

class Child2(Parent):
    def greet_child2(selfself):
        print("Child2")

c1=Child1()
c1.greet_parent()
c1.greet_child1()

c2=Child2()
c2.greet_parent()
c2.greet_child2()