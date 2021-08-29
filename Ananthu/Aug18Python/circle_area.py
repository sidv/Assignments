import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f'area of the circle is {math.pi*self.radius**2}'


radius = float(input("Enter th radius of circle : "))
r = Circle(radius)
print(r.area())
