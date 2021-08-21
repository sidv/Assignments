from circle import Circle

#child class
class Radius(Circle):
	def __init__(self,radius):
		self.radius = radius
	def __add__(self, other):
		return float(self.radius) + float(other.radius)
	def __str__(self):
		return f'{self.radius}'
radius = float(input("Enter the radius of circle: "))
r = Circle(radius)
print("Area of circle: ",r.area())
#addition
#b = Circle(12)
#sum = r + b
#print(sum)

#print(add(r))
#doc
print(Circle.__doc__)
#__str__
print(str(r))
		
