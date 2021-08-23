#1.Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
#Implement + operation (Perform addition of radius)
#-Implement documentation attribute(_doc_ attribute)
#-Implement string typecasting and print "The radius is ..value.."(_str_)
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
print("*****Area of a Circle*****")
print(c.area())
print("Sum of length and width")
sum_area = c+d
print(sum_area)
print(str(c))
print("*****__doc__Attribute*****")
print(c.__doc__)

