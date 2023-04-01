# Create a parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("The animal makes a sound.")

# Create a child class that inherits from the Animal class
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def make_sound(self):
        print("Woof! Woof!")

# Create an instance of the child class
my_dog = Dog("Fido", 3, "Labrador")

# Call the methods on the instance of the child class
print(my_dog.name)  # Output: "Fido"
print(my_dog.age)  # Output: 3
print(my_dog.breed)  # Output: "Labrador"
my_dog.make_sound()  # Output: "Woof! Woof!"
