class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f'Area of rectangle is {self.length * self.width}'


length = float(input("Enter th length of rectangle : "))
width = float(input("Enter width of rectangle : "))
a = Rectangle(length, width)
print(a.area())
