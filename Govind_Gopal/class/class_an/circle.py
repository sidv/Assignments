import math

class Circle:
	__doc__="!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	def __init__(self,radius):
		self.radius = radius
	def area(self):
		print("Computing Area!!")
		a=math.pow(self.radius,2)
		c=a*math.pi
		return c
	def __add__(self,b):
		return self.radius +  b.radius
	def __str__(self):
		return 'The radius is'+ str(self.radius)
