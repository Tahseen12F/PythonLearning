# Inheritance in Python allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Different types of Python Inheritance
"""There are 5 different types of inheritance in Python. They are as follows:
1. Single inheritance: When a child class inherits from only one parent class, it is called single inheritance.
2. Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances.
3. Multilevel inheritance: When we have a child and grandchild relationship.
This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class
4. Hierarchical inheritance More than one derived class can be created from a single base.
5. Hybrid inheritance: This form combines more than one form of inheritance.
Basically, it is a blend of more than one type of inheritance"""


# Single Inheritance related program

class Father:
    gold = "1kg"
    __private_villa = "Goa"

    def his_car(self):
        print("Lambo")

    def threeBHKFlat(self):
        print("3 BHK Flat")

    def private_villa_access(self, is_my_son):
        print(self.__private_villa)


class Son(Father):
    pass


print("Son...........")
Jack = Son()
print(Jack.gold)
Jack.his_car()
Jack.threeBHKFlat()
# Jack.__private_villa - Not allowed to access private member but with the help of Encapsulation will get.
Jack.private_villa_access(True)
print("Father..........")
mmd = Father()
print(mmd.gold)
mmd.his_car()
mmd.threeBHKFlat()
