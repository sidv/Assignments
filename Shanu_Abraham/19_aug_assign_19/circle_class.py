#Define a class named Circle which can be constructed by a radius.
 #The Circle class has a method which can compute the area.
#-Implement + operation (Perform addition of radius)
#-Implement documentation attribute(__doc__ attribute)
#-Implement string typecasting and print "The radius is ..value.."(__str__)


class Circle:
	def __init__(self,r):
		self.radius = r

	def area(self):
		print(F"Area is:{self.radius**2*3.14}")

	def __add__(self,other):
		return self.radius + other.radius 

	def __str__(self):
		return F"The radius  is {self.radius}"

radius =float(input("Enter the radius of circle:"))
r = Circle(radius)
print(r.area())

other = float(input("Enter the other radius of circle:"))
o = Circle(other)
o.area()
c1 = r + o
print(c1)
print(str(c1),"str _function")	
