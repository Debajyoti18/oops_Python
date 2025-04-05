class Car:
    # Class variable
    total_cars = 0
    
    def __init__(self, model, year):
        # Instance variables
        self.model = model
        self.year = year
        Car.total_cars += 1
    
    # Instance method
    def display_info(self):
        print(f"Car Model: {self.model}, Year: {self.year}")
    
    # Static method
    @staticmethod
    def print_car_info(model, year):
        print(f"Static method: Car Model: {model}, Year: {year}")
    
    # Class method (for comparison)
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars


# Accessing static method using class name
print("Accessing static method using class name:")
Car.print_car_info("Tesla", 2023)

# Creating an instance of Car
my_car = Car("Toyota", 2022)

# Accessing instance method using object
print("\nAccessing instance method using object:")
my_car.display_info()

# This works but it's not conceptually correct (accessing static method via instance)
print("\nAccessing static method via instance (not recommended):")
my_car.print_car_info("Honda", 2021)

# Trying to access instance method using class name would result in an error
print("\nTrying to access instance method using class name:")
try:
    Car.display_info()
except TypeError as e:
    print(f"Error: {e}")

# Accessing class method using class name
print("\nAccessing class method using class name:")
print(f"Total cars: {Car.get_total_cars()}")