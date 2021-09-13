import math 
class Circle:
	def __init__(self,radius):
		self.radius = radius
		print("Radius added")
	def area(self):
		a = math.pow(radius1,radius1)		
		area = math.pi * a
		return (f"\t\tThe area is {area}")
				
radius1 = int(input("\t\tEnter first the radius"))
r = Circle(radius1)
r1 = Circle(5)

print(r.area())

