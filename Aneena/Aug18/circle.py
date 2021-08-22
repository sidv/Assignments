class Circle():
	def __init__(self, r):
		self.radius = r
	
	def area(self):
		return self.radius**2*3.14
	
radius=int(input("enter the radius"))
c = Circle(radius)
print(c.area())

