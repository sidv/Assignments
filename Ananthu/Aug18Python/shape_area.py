import math


class Shape():
    def __init__(self, length, area=0):
        self.length = length

    def area(self):
        return f"Area of shape is {math.pi*self.length**2}"


class Circle(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return f'Area of circle is {math.pi * self.length**2}'


s = Circle(10)
print(s.area())
s1 = Shape(10)
print(s1.area())
