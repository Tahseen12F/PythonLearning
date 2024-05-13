# Hierarchical Inheritance
class Vehicle:
    def Info(self):
        return "This is a vehicle"


class Car(Vehicle):
    def Info(self):
       return "This is a Car"


class Bicycle(Vehicle):
    def Info(self):
        return "This is a Bicycle"


car = Car()
bicycle = Bicycle()
print(car.Info())
