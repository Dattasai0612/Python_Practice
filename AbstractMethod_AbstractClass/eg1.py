from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        pass

    def engine(self):
        print("B6 Engine")
    @abstractmethod
    def color(self):
        pass

class Car(Vehicle):
    def wheels(self):
        print("Car Wheels: 4")

    def color(self):
        print("Car Color: Red")

class Bike(Vehicle):
    def wheels(self):
        print("Bike Wheels: 2")

    def color(self):
        print("Bike Color: Black")

c=Car()
c.wheels()
c.engine()
c.color()

b=Bike()
b.wheels()
b.engine()
b.color()