class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.14*(self.radius**2)


circle = Circle(7)
print(circle.area())
