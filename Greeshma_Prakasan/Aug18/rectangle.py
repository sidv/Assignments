class Rectangle:

	def __init__(self,l,w):
		self.length = l
		self.width = w

	def get_area(self):
		area = self.length*self.width
		return area

r = Rectangle(8,9)
print(r.get_area())
