import math
class Circle:
	__doc__="!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	def __init__(self,radius):
		self.radius = radius
	def area(self):
		print("Computing Area!!")
		a=math.pow(radius,radius)
		c=a*math.pi
		print(c)
	def __add__(self,b):
		return self.radius +  b.radius
	def __str__(self):
		return 'The radius is'+ str(self.radius)
		
radius=int(input("Enter the radius"))
r=Circle(radius)
print(r.area())
print(r.__doc__)
b=Circle(5)
c=r+b
print(c)
print(str(r))





		
