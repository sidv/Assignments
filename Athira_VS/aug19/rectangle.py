
class Rectangle:
    length = 0
    breadth = 0

    def __init__(self, l, b):
        self.length = int(l)
        self.breadth = int(b)

    def __add__(self,b):
        return (self.length + b.length, self.breadth + b.breadth)

    def __doc__(self):
        print("This class is to define a rectangle of given length and breadth and find its area.")

    def __str__(self):
        return f"The length is {self.length} and breadth is {self.breadth}"

    def __gt__(self,b):
        if self.area() > b.area():
            return True
        else:
            return False


    def area(self):
        return self.length * self.breadth

