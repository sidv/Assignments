import math


class Circle:
    """
    this class is going to give the result 
    of addition of 2 circle's radius
    and also the area of the circle
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f'area of the circle is {math.pi*self.radius**2}'

    def __add__(self, radius):
        return self.radius + other.radius

    def __str__(self):
        return f'The radius is {self.radius}'


radius = float(input("Enter the radius of circle : "))
r = Circle(radius)
print(r.area())
other = Circle(10)
c = r+other
print(c)
print(Circle.__doc__)
print(str(r))
