class Rectangle():
    '''
    This class will provide the area of rectangle
    as well as addition of length and width
    '''

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f'area of rectangle is {self.length * self.width}'

    def __add__(self, length, width):
        return f'addition of length and width is {self.length+self.width}'

    def __str__(self):
        return f'The length is {self.length} and the width is {self.width}'

    def __gt__(self, other):
        if self.area() > other.area():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False


length = float(input("Enter th elength of rectangle : "))
width = float(input("Enter width of rectangle : "))
a = Rectangle(length, width)
print(a.area())

# addition of length and width

print(length + width)

# __doc__
print(Rectangle.__doc__)

# __str__
print(str(a))

# __gt__
other = Rectangle(length, width)
print(other.area())

print(a > other)

# __eq__
print(a == other)
