from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

cir = Circle(int(input("Enter radius: ")))
print(cir.area())