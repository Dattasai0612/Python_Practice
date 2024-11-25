class Parent1:
    def greet_parent1(self):
        print("Parent1")

class Parent2:
    def greet_parent2(self):
        print("Parent2")

class Child(Parent1,Parent2):
    def greet_child(self):
        print("Child")

c=Child()
c.greet_parent1()
c.greet_parent2()
c.greet_child()