#1.Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

class Circle:
	def __init__(self,r):
		self.radius = r

	def area(self):
		print(F"Area is:{self.radius**2*3.14}")

c1=Circle(2)
area = c1.area()
