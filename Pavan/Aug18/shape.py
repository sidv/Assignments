class Shape():
    def __init__(self, length):
        self.length = length

    def area(self):
        return 0
        

class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        return self.length * self.length


sq = Square(int(input("Square: Enter length: ")))
sh = Shape(int(input("Shape: Enter length: ")))
print(f"Area of square: {sq.area()}")
print(f"Area of shape: {sh.area()}")
