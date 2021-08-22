class Rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return(self.l*self.w)
    
r1 = Rectangle(5,4)
print(r1.area())
