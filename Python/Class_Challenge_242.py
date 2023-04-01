# Create a class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    # Create a method in a class
    def accelerate(self, acceleration):
        self.speed += acceleration
    
# Create an object
my_car = Car("Toyota", "Camry", 2021)

# Assign values to object properties using the __init__() function
print(my_car.make)  # Output: "Toyota"
print(my_car.model)  # Output: "Camry"
print(my_car.year)  # Output: 2021

# Call the method on the object
my_car.accelerate(20)
print(my_car.speed)  # Output: 20
