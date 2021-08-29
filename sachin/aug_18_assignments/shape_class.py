#3.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:

    def area(self,length=0):
        return(length**2)

class Square(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        ar = super().area(self.length)
        return(ar)
obj1 = Shape()
obj2 = Square(6)
print(obj1.area())
print(obj2.area())