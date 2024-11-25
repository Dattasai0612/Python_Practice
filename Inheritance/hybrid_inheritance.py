class Base:
    def greet_base(self):
        print("Base")

class Derived1(Base):
    def greet_derived1(self):
        print("Derived1")

class Derived2(Base):
    def greet_derived2(self):
        print("Derived2")

class Child(Derived1, Derived2):
    def greet_child(self):
        print("Child")

c=Child()
c.greet_base()
c.greet_derived1()
c.greet_derived2()
c.greet_child()