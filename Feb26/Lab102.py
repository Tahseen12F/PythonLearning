# Use of Constructor
""" Constructors are generally used for instantiating an object.
The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created.
In Python the __init__() method is called the constructor and is always called when an object is created. """


# Note - If you're using multiple parameterized constructor then we can't create empty constructor that time.

class Car:
    name = None
    make = None
    model = None

    def __init__(self, ob_name, ob_make, ob_model):
        # Special function (__init__() Method is also known as Constructor).
        # Automatically called whenever object is created.
        self.name = ob_name
        self.make = ob_make
        self.model = ob_model

    def start_engine(self):
        print("Car name is:" + self.name)
        print("Car make is:" + self.make)
        print("Car model is:" + self.model)


lambo = Car("Lambo", "V2", "2024")
lambo.start_engine()
print("................................")
tata = Car("TATA", "Altroz", "2023")
tata.start_engine()
