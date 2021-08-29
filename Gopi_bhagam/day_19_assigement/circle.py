class circle:
 	__doc__ ="this is circle "
 	def __init__(self,radius):
 		self.radius = radius
 	def area(self):
 		return 3.14 * (self.radius ** 2)
 	def __add__(self,a_radius):
 		return self.radius + a_radius.radius
 	def __str__(self):
 		return f"the radius is :{self.radius}"


radius=int(input("entr a radius:"))
obj=circle(radius)
print("area of circle:",obj.area())
a_radius =circle(5)
res=obj+a_radius
print(res)
print(circle.__doc__)
print(circle.__str__)

