#1.Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
class Circle:
	def __init__(self,radius): 
		self.r = radius
	def area(self):
		return(3.14*(self.r)*(self.r))

radius = int(input("Enter the radius"))
c = Circle(radius)
print(c.area())

