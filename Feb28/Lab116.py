# Polymorphism
"""polymorphism means the same function name (but different signatures) being used for different types.
The key difference is the data types and number of arguments used in function."""
# Two types of Polymorphism : Method overloading and Method Overriding
"""Method Overloading is an example of Compile time polymorphism. 
In this, more than one method of the same class shares the same method name having different signatures.
Method overloading is used to add more to the behavior of methods 
and there is no need of more than one class for method overloading.
Note: Python does not support method overloading. 
We may overload the methods but can only use the latest defined method."""
# .............................................................................
"""Method overriding is an example of run time polymorphism.
In this, the specific implementation of the method that is already provided by the parent class provided by child class.
It is used to change the behavior of existing methods and there is a need for at least 2 classes for method overriding
In method overriding,inheritance always required as it is done between parent class and child class methods."""


class Shape:
    def area(self):
        print("This is the area")


class Rect(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rect = Rect(22, 12)
print(rect.area())
ar = Shape()
ar.area()


