#Define a class named Rectangle which can be constructed by a length and width. 
#The Rectangle class has a method which can compute the area.
#-Implement + operation (Perform addition of length and width)
#-Implement documentation attribute(__doc__ attribute)
#-Implement string typecasting and print "The length is ..value.. and width is ..value.."(__str__)
#-Implement > operation(__gt__(self,other) and return true or false if area is greater or smaller)
#-Implement == operation(__eq__(self,other) and return true or false if area is equal or not)

class Rectangle:
	__doc__ = "This is rectangle class"
	def __init__(self,l,w):
		self.len = l
		self.width = w

	def compute_area(self):
		print("AREA")
		area = self.len * self.width
		return area

	def __add__(self,other):
		return self.len + other.width
	
	def __str__(self):
		return f"This is length and width of rectangle is {self.len} and {self.width}"

	def __gt__(self,other):
		return self.compute_area() > other.compute_area()
	
	def __eq__(self,other):
		return self.compute_area() == other.compute_area()

len = float(input("Enter the length"))

width = float(input("Enter the width"))

r1 = Rectangle(len,width)
r1.compute_area()
print(r1)
len1 = float(input("Enter the length"))
width1 = float(input("Enter the width"))
r2 = Rectangle(len1,width1)
r2.compute_area()
print(r2)
c =r1 + r2 # add operation
print(c)
print(str(r1),"str")
print(str(r2),"str")
print(r1.__doc__,"doc")
g = r1 > r2
print(g)
d = r1 == r2  #equal operation
print(d)
