class Circle:
	__doc__ = "This is for finding area of circle"
	def __init__(self,radius): 
		self.r = radius
	def area(self):
		return(3.14*(self.r)*(self.r))
	

radius = int(input("Enter the radius"))
c = Circle(radius)

print("area of circle", c.area())

