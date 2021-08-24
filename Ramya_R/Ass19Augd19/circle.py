class Circle:
	__doc__ = "This is for finding area of circle"
	def __init__(self,radius): 
		self.r = radius
	def area(self):
		return(3.14*(self.r)*(self.r))
	def __add__(self,b):
		return int(self.r)+int(b.r)
	def __str__(self):
		return f"The radius is  : {self.r}"

radius = int(input("Enter the radius"))
c = Circle(radius)
d = Circle(radius)

print("area of circle", c.area())
sum_area = c+d
print("sum of 2 circle areas", sum_area)
print(str(c))
print(c.__doc__)
