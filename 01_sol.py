
#Classes and Objects
#Class: Blueprint for creating objects (a data structure)
#Object: Instance of a class with its own attributes and methods
#__init__(): Special method (constructor) that initializes object attributes
#self: Reference to the current instance of the class
#Class attributes: Shared by all instances of a class
#Instance attributes: Unique to each object of a class
#Instance methods: Functions defined within a class that operate on instances
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects
buddy = Dog("Buddy", 5)
max = Dog("Max", 3)

print(buddy.name)        # Buddy
print(buddy.bark())      # Buddy says Woof!
print(buddy.species)     # Canis familiaris