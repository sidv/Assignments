import math
class Circle:
	__doc__="\t\tEntering program to compute area of cirices of given radius"
	def __init__(self,radius):
		self.radius = radius
		print("Radius added")
	def area(self):
		a=math.pow(self.radius,2)
		c=a*math.pi
		return (f"\t\tThe area is {c}")
	def __add__(self,b):
		return self.radius +  b.radius
	def __str__(self):
		return 'The radius is'+ " " +str(self.radius)
