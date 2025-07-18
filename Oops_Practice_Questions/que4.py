from abc import ABC, abstractmethod
import math

# Step 1: Define the abstract class Shape
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass  # Abstract method for calculating area

# Step 2: Implement concrete classes

# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Step 3: Use the concrete classes

# Creating objects for each shape
rectangle = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(8, 4)

# Display areas
print("Rectangle area:", rectangle.area())
print("Circle area:", circle.area())
print("Triangle area:", triangle.area())
