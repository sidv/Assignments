from math import pi

class Circle:
    radius = 0

    def __init__(self,radius):
        self.radius = int(radius)
        
    def __add__(self,b):
        return self.radius + b.radius

    def __doc__(self):
        print("This class is to define a circle of given radius")

    def __str__(self):
        return f"The radius is {self.radius}"


    def area(self):
        return pi*self.radius*self.radius

    

