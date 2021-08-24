class Shape:
	def area(self,side = 0):
		return (side*side)

class Square(Shape):
	def __init__(self,side=0):
		self.side = side
	def area(self):
		return(super().area(self.side))
	
num = int(input("Enter the side size : "))
if num == 0 or num == "":
	s = Square()
	print("Area of Sqaure : ",s.area())
else:
	s = Square(num)
	print("Area of Sqaure : ",s.area())
