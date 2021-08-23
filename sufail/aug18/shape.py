class Shape:

	def area(self,length=0):
        	return (length**2)

class Square(Shape):
	def __init__(self,length):
		self.length = length

	def area(self):
		area=super().area(self.length)
		return area

sh=Shape()
sq=Square(10)
print(sq.area())
