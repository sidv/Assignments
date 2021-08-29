class Rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return self.l*self.w
    def __add__(self,obj):
        return f"{self.l+obj.l} {self.w+obj.w}"
    def __doc__(self):
        return "The rectangle class which can compute the area"
    def __str__(self):
        return f"The length is {self.l} and the width is {self.w}"
    def __gt__(self,obj):
        if (self.area() > obj.area()):
            return True
        else:
            return False
    def __eq__(self,obj):
        if (self.area() == obj.area()):
            return True
        else:
            return False
    

r1 = Rectangle(5,4)
r2 = Rectangle(6,5)
print(r1+r2)
print(r1.__doc__())
print(str(r1))
print(r1>r2)
print(r2==r1)
