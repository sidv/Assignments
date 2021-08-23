import math
#parent class
class Shape:
	#def __init__(self,side):
		#self.side = side
	def area(self,side=0):
		return (side*side)
	
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
if side == 0 or side == "":
	s = Square()
	print("Area of Sqaure : ",s.area())
else:
	s = Square(side)
	print("Area of Sqaure : ",s.area())
#addition
other = Square(side)
c=s+other
print(c)
#doc
print(Square.__doc__)
#__str__
print(str(s))
		
