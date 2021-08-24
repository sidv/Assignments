class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.14*(self.radius**2)


circle = Circle(7)
print(circle.area())

radius = int(input("enter the radius"))
c =  Circle(radius)
d = Circle(radius)
print("Area of Circle")
print(c.area())
print("sum of length and width")
sum_area =  c + d
print(sum_area)
print(str(c))
print("__doc__Attribute")
print(c.__doc__)

