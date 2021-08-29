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


c_obj = Circle(5)
print(c_obj.area())
s_obj = Shape(6)
print(s_obj.area())
