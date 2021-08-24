class Circle():
	def __init__(self, r):
		self.radius = r
	
	def area(self):
		return self.radius**2*3.14
	
	def __add__(self,other):
		return self.radius + other.radius

	def __str__(self):
		#return "Radius : {self.radius}"
		return "Radius"+ str(self.radius)
radius=int(input("Enter the radius\n"))
r = Circle(radius)
print(r.area())
print(r.__doc__)
other=Circle(5)
c=r+other
print(c)
print(str(r))
#print(str(r))
