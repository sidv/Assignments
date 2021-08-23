import math

class Shape:

    def area(self,l=0):
        return(math.pow(l,2))

class Square(Shape):
    def __init__(self,l):
        self.l = l

    def area(self):
        ar = super().area(self.l)
        return(ar)
s0 = Shape()
s1 = Square(6)
print(s0.area())
print(s1.area())
    



