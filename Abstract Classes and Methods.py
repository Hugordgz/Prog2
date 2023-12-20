from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating objects of the derived classes
rectangle = Rectangle(5, 3)
circle = Circle(7)

# Calling the abstract methods
print(rectangle.area())  # Output: 15
print(rectangle.perimeter())  # Output: 16
print(circle.area())  # Output: 153.86
print(circle.perimeter())  # Output: 43.96