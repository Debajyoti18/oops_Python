'''Inheritance

Allows a class to inherit attributes and methods from another class
Parent class (base class): The class being inherited from
Child class (derived class): The class that inherits from another
super(): Function to call methods from parent class
Method overriding: Redefining a parent class method in a child class
Multiple inheritance: Inheriting from more than one class'''


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):  # Cat inherits from Pet
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Call parent's init method
        self.color = color
    
    def speak(self):
        return "Meow"