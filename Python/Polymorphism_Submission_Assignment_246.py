

# Define the parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        pass # this method will be overridden in the child classes

    
# Define the first child class
class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name, "Canine")
        self.breed = breed
        self.age = age
        
    def make_sound(self):
        return "Woof!"


# Define the second child class
class Cat(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name, "Feline")
        self.color = color
        self.weight = weight
        
    def make_sound(self):
        return "Meow!"

    
# Create instances of the child classes and call the polymorphic method
dog = Dog("Fido", "Golden Retriever", 5)
print(dog.make_sound()) # Output: Woof!


cat = Cat("Fluffy", "Gray", 8)
print(cat.make_sound()) # Output: Meow!
