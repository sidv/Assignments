class Circle:
	__doc__ = "This is a class Circle!!!!!!!!!!!!!!!!"
	def __init__(self,r):
		self.radius = r
	
	def get_area(self):
		area = 3.14*self.radius**2
		return area

	def __add__(self,other):
		return self.radius + other.radius

	def __str__(self):
		return "The radius is "+str(self.radius)

c1 = Circle(5)
c2 = Circle(6)
print(c1+c2)
print(c1.get_area())
print(str(c1))
print(c1.__doc__)
