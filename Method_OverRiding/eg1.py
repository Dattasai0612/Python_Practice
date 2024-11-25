class Vehicle:
    def property(self):
        print("Details")

    def carname(self):
        print("Shift Car")

class Car(Vehicle):
    def carname(self):
        super().carname()
        print("WagnoR Car")

c=Car()
c.property()
c.carname()