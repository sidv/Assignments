"""1.Define a class named Circle which can be constructed by a radius.
 The Circle class has a method which can compute the area.
-Implement + operation (Perform addition of radius)
-Implement documentation attribute(_doc_ attribute)
-Implement string typecasting and print "The radius is ..value.."(_str_)"""

class Circle:
	def __init__(self,c1):
		self.radius = c1

	def area(self):
		print(F"Area is:{self.radius**2*3.14}")

	def __add__(self,other):
		return self.radius + other.radius

	def __doc__(self):
		return "The class circle is return radius of circle"

	def __str__(self):
		return "The radius "	
radius = float(input("Enter the radius of the circle : "))
other = float(input("Enter the radius of the other : "))
c1 = Circle(radius)
print(c1.area())
c2 = radius + other

print(c1.__str__())
print(c1.__doc__())
print(c2)
