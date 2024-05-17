# Method Overriding - Same name in the parent and child,
# child always override the parent function
# super means call my Parent function
class Animal():
    def __init__(self, Name):
        self.Name = Name

    def sound(self):
        print("Animal sound")


class Cat(Animal):
    def sound(self):
        super().sound()   # using super() means calling parent func
        print("Meow sound")


cat = Cat("Kitty")
cat.sound()
