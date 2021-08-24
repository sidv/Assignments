
import math

class Shape():
    def __init__(self, length,area=0):
        self.length = length
    def area(self):
        return f"Area of shape is {math.pi*self.length**2}"


class square(Shape):
    def __init__(self, length):
        self.length =length
 

    def area(self):
        return f'Area of circle is {math.pow(2,5)}'

sq_obj = square(8)
print(sq_obj.area())
sh_obj = Shape(8)
print(sh_obj.area())
