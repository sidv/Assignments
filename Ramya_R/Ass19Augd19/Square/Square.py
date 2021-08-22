from shape import Shape

#child class
class Square(Shape):
	def __init__(self,side=0):
		print(side)
		self.side = side
	def area(self):
		return(super().area(self.side))
	def __add__(self, side):
		return self.side+other.side
	def __str__(self):
		return f'{self.side}'
side = int(input("Enter the side of circle: "))
s = Shape(side)
print("Area of Square: ",s.area())
#addition
#other = Shape(side)
#c=s+other
#print(c)
#doc
print(Shape.__doc__)
#__str__
print(str(s))
		
