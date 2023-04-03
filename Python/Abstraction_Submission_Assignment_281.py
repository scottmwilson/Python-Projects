

from abc import ABC, abstractmethod    # import ABC and abstractmethod from abc module

class Shape(ABC):    # define abstract base class Shape
    @abstractmethod    # abstract method to calculate area
    def calculate_area(self):
        pass
    
    def display_info(self):    # regular method to display information about shape
        print(f"This is a {type(self).__name__}.")

class Square(Shape):    # define child class Square that extends Shape
    def __init__(self, side_length):
        self.side_length = side_length
        
    def calculate_area(self):    # implementation of calculate_area for Square
        return self.side_length ** 2

# create an object that utilizes both parent and child methods
square = Square(5)
square.display_info()    # output: This is a Square.
print(square.calculate_area())    # output: 25
