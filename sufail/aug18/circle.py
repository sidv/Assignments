
class circle:
	def __init__(self,radius):
		self.radius=radius

	def area(self):
		area=3.14*self.radius**2
		return area

c=circle(5)
area=c.area()
print(area)
