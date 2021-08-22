class Circle:
	
	def __init__(self,r):
		self.radius = r
	
	def get_area(self):
		area = 3.14*self.radius**2
		return area

c = Circle(5)
print(c.get_area())
