

class Circle:
	def __init__(self,r):
		self.radius = r

	def area(self):
		print(F"Area is:{self.radius**2*3.14}")

	def __add__(self,obj):
		return self.radius + obj.radius

	def __doc__(self):
		return "The circle has a method which can compute the area"

	def __str__(self):
		return f"The radius is {self.radius}"	

c1 = Circle(2)
c2 = Circle(3)
total = c1+c2
print(total)
print(c1.__doc__())
print(str(c2))
