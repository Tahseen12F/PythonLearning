# Variable Example (Instance and Local)
class Person:
    # Class variable or Instance variable
    name = None
    age = None

    def walk(self):
        a = 10  # Local Variable
        print("Hi your name is", self.name)
        print("Hi your age is", self.age)
        print(a)


nisha = Person()
nisha.walk()
