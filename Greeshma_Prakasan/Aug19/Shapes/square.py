from shapes import Shapes
class Square(Shapes):

	def __init__(self,l):
		self.length = l

	def area(self):
		area = self.length**2
		return area



s = Square(5)
print(s.area())
