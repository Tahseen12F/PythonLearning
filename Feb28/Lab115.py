# Abstraction : Hiding the details and showing what is required
# Hide the implementation and show only important details
# 1. Abstract the Base class  2. Abstract the Base methods

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, Name):
        self.Name = Name

    @abstractmethod
    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        print("Meow")


cat = Cat("Kitty")
cat.sound()