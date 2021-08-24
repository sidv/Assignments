
class Circle:
	"""implementing doc"""
	pi =3.141
	def __init__(self,radius):
		self.radius = radius
	def area(self):
		return self.pi*self.radius**2
	def __add__(self,c2):
		return int(self.radius)+int(c2.radius)
	def __str__(self):
		return f"{self.radius}"
radius=int(input("Enter the first radius :\t"))
c1=Circle(radius)
radius2=int(input("Enter the 2nd radius :\t"))
c2=Circle(radius2)
print(f"Area of radius {radius}",c1.area())
print(f"Area of radius {radius2}",c2.area())
a=c1+c2
print("Sum of radius",a)
print(Circle.__doc__)
