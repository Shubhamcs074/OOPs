"""Q1: Create a class hierarchy for a Transport System.
Base class: Vehicle
Subclasses: Car, Bike, Bus
Each subclass should override a method calculate_fare() differently.
 Use constructor chaining.
 Include attributes like max_speed, capacity, fuel_type.

in python"""
 


class Vehicle:
    def __init__(self, max_speed, capacity, fuel_type):
        self.max_speed = max_speed
        self.capacity = capacity
        self.fuel_type = fuel_type

    def calculate_fare(self):
        return 0

    def __str__(self):
        return f"{self.__class__.__name__}(Max Speed: {self.max_speed}, Capacity: {self.capacity}, Fuel: {self.fuel_type})"


class Car(Vehicle):
    def __init__(self, max_speed, capacity, fuel_type):
        super().__init__(max_speed, capacity, fuel_type)

    def calculate_fare(self):
        
        return 50 + (self.capacity * 10)


class Bike(Vehicle):
    def __init__(self, max_speed, capacity, fuel_type):
        super().__init__(max_speed, capacity, fuel_type)

    def calculate_fare(self):
        
        return 20 + (self.capacity * 5)


class Bus(Vehicle):
    def __init__(self, max_speed, capacity, fuel_type):
        super().__init__(max_speed, capacity, fuel_type)

    def calculate_fare(self):
        
        return 100 + (self.capacity * 7)


car = Car(180, 4, "Petrol")
bike = Bike(120, 2, "Petrol")
bus = Bus(100, 40, "Diesel")

print(car)
print("Car fare:", car.calculate_fare())

print(bike)
print("Bike fare:", bike.calculate_fare())

print(bus)
print("Bus fare:", bus.calculate_fare())
