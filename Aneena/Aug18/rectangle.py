class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

l=int(input("Enter the length\n"))
w=int(input("Enter the width\n")) 
area=Rectangle(l,w)
print(area.rectangle_area())
