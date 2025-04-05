'''The @property decorator in Python is a powerful feature that allows you to:

1.Create getter methods: By decorating a method with @property, you can access it like an attribute without calling
parentheses (e.g., temp.celsius instead of temp.celsius()).
2.Create setter methods: Using the @property_name.setter decorator, you can define how values are assigned to properties, 
enabling validation and side effects during assignment.
3.****Create read-only properties: If you define a property with a getter but no setter, the property becomes read-only.
Add computed properties: You can create properties that depend on other attributes or properties.
'''
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    # Getter method
    @property
    def celsius(self):
        print("Getting celsius value")
        return self._celsius
    
    # Setter method
    @celsius.setter
    def celsius(self, value):
        print(f"Setting celsius to {value}")
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    # Property that depends on another property
    @property
    def fahrenheit(self):
        print("Converting celsius to fahrenheit")
        return (self.celsius * 9/5) + 32
    
    # Setter for the dependent property
    @fahrenheit.setter
    def fahrenheit(self, value):
        print(f"Setting fahrenheit to {value}")
        self.celsius = (value - 32) * 5/9
    
    # Read-only property
    @property
    def kelvin(self):
        print("Converting celsius to kelvin")
        return self.celsius + 273.15


# Creating an instance
temp = Temperature(25)

# Accessing properties (behave like attributes)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")
print(f"Kelvin: {temp.kelvin}")

# Setting values through properties
print("\nChanging celsius to 30")
temp.celsius = 30
print(f"New celsius: {temp.celsius}")
print(f"New fahrenheit: {temp.fahrenheit}")

print("\nChanging fahrenheit to 86")
temp.fahrenheit = 86
print(f"New celsius: {temp.celsius}")
print(f"New fahrenheit: {temp.fahrenheit}")

# Attempting to set a read-only property would raise an AttributeError
try:
    temp.kelvin = 300
except AttributeError as e:
    print(f"\nError when trying to set kelvin: {e}")

# Validation in action
try:
    temp.celsius = -300
except ValueError as e:
    print(f"\nValidation error: {e}")
    '''Properties are one of Python's most elegant features for creating clean, 
    intuitive interfaces while maintaining proper encapsulation and control over attribute access.'''
    
    '''Duck Typing
    Duck typing is a programming concept in dynamic languages like Python that focuses on an object's behavior (what methods and properties it has) rather than its type or class. 
    The name comes from the phrase: "If it walks like a duck and quacks like a duck, then it's a duck."
    In duck typing, you don't check if an object is of a specific type. Instead, you simply try to use the object as if it has 
    the methods or attributes you need. If the object has those capabilities, it works; if not, it fails.'''
def make_it_swim(animal):
    # We don't check the type of animal
    # We just expect it to have a swim() method
    animal.swim()

class Duck:
    def swim(self):
        print("Duck swimming")
    
    def quack(self):
        print("Quack quack")

class Fish:
    def swim(self):
        print("Fish swimming")

class Dog:
    def bark(self):
        print("Woof woof")

# These work because they have a swim() method
duck = Duck()
fish = Fish()
make_it_swim(duck)  # Output: Duck swimming
make_it_swim(fish)  # Output: Fish swimming

# This will fail because Dog doesn't have swim() method
dog = Dog()
try:
    make_it_swim(dog)
except AttributeError as e:
    print(f"Error: {e}")  # Output: Error: 'Dog' object has no attribute 'swim'