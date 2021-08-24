class circle:
	def __init__(self,radius):
		self.radius = radius

	def area(self):
		return 3.14 * (self.radius ** 2)
obj=circle(3)
print("area of circle:",obj.area())
