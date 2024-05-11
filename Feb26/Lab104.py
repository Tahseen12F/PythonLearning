# Encapsulation: Binds the data, methods, Data members and Class variables.
# It acts as a protective shield that puts restrictions on accessing variables and methods directly.
# And can prevent accidental or unauthorized modification of data.
# Wrapping or binding the data variables with the methods.
"""Access modifiers limit access to the variables and functions of a class.
 Python uses three types of access modifiers; they are - private, public and protected."""


# Public - Accessible anywhere from the class, By default all member variables of class are public.
# Private - Accessible within the class. To define a private member, prefix the member name with a double underscore __
# Protected - Accessible within the class and also to its subClasses.
# To define a protected member, prefix the member name with a single underscore “_”.

class MyClass():
    def __init__(self):
        self.name = "Tasha"  # Public

    def publicFun(self):  # Public method
        print("Public func()")

    def __private__fun(self):  # Private method
        print("This is private")

    def publicFn_private(self):
        self.__private__fun()   # This func can call private function as this is written within the class.


a = MyClass()
a.publicFun()
a.publicFn_private()
# a.__private__fun() -> This is not allowed. Direct Private func call not allowed
