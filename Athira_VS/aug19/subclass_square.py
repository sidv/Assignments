from math import pow

class Shape:

    def __init__(self):
        self.length = 0
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return pow(self.length,2)

