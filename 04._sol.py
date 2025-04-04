'''Polymorphism
Ability to use a common interface for different forms (data types)
Method overriding: Same method name but different implementations
Duck typing: "If it walks like a duck and quacks like a duck, it's a duck"
Runtime polymorphism: Method resolution at runtime'''




class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
        self.speed = 0
    
    def start_engine(self):
        self.is_running = True
        return f"The {self.make} {self.model}'s engine is now running."
    
    def stop_engine(self):
        self.is_running = False
        self.speed = 0
        return f"The {self.make} {self.model}'s engine has been stopped."
    
    def accelerate(self, speed_increase):
        if self.is_running:
            self.speed += speed_increase
            return f"The {self.make} {self.model} accelerates to {self.speed} km/h."
        else:
            return f"Cannot accelerate. The {self.make} {self.model}'s engine is not running!"
    
    def brake(self, speed_decrease):
        if self.speed >= speed_decrease:
            self.speed -= speed_decrease
        else:
            self.speed = 0
        return f"The {self.make} {self.model} slows down to {self.speed} km/h."
    
    def honk(self):
        return "Beep beep!"
    
    def describe(self):
        return f"Vehicle: {self.year} {self.make} {self.model}"


# Inheritance: Car class inherits from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type="Gasoline", num_doors=4):
        # Call parent constructor
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.num_doors = num_doors
    
    # Polymorphism: Overriding parent method with new implementation
    def honk(self):
        return "Honk honk!"
    
    # New method specific to Car class
    def describe(self):
        return f"Car: {self.year} {self.make} {self.model}, {self.num_doors}-door, runs on {self.fuel_type}"


# Another child class showing inheritance
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity, num_doors=4):
        # Call parent constructor but override fuel_type
        super().__init__(make, model, year, fuel_type="Electricity", num_doors=num_doors)
        self.battery_capacity = battery_capacity
    
    # Polymorphism: Overriding method from parent class
    def start_engine(self):
        self.is_running = True
        return f"The {self.make} {self.model} powers up silently."
    
    # Polymorphism: Overriding another method
    def honk(self):
        return "Beep boop!"
    
    def describe(self):
        return f"Electric Car: {self.year} {self.make} {self.model}, {self.battery_capacity}kWh battery"


# Demonstrate polymorphism with a function that works with any Vehicle object
def test_drive(vehicle):
    results = []
    results.append(vehicle.describe())
    results.append(vehicle.start_engine())
    results.append(vehicle.accelerate(50))
    results.append(vehicle.honk())
    results.append(vehicle.brake(20))
    results.append(vehicle.stop_engine())
    return results


# Create instances of each class
regular_car = Car("Toyota", "Camry", 2022)
tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
truck = Vehicle("Ford", "F-150", 2021)

# Demonstrate polymorphism by calling the same methods on different objects
print("\nTesting Regular Car:")
for result in test_drive(regular_car):
    print(result)

print("\nTesting Electric Car:")
for result in test_drive(tesla):
    print(result)

print("\nTesting Base Vehicle:")
for result in test_drive(truck):
    print(result)