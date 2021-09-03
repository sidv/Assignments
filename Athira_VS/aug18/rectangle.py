class Rectangle:
    def __init__(self, l, b):
        self.l =  l
        self.b = b

    def area(self):
        return l * b

l = int(input("Enter length: "))
b  = int(input("Enter breadth: "))
rec = Rectangle(l, b)
print(rec.area())
