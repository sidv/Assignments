class Rectangle:
	"""implementing doc"""
	def __init__(self,length,width):
		self.length=length
		self.width=width
	def area(self):
		return self.length*self.width
	def __add__(self,r2):
		return self.length+self.width+r2.length+r2.width
	def __str__(self):
		return f"The lenth is {self.length}  breadth is {self.width}"
	def __gt__(self,r2):
		if self.area() > r2.area():
			return True
		else:
			return False
	def __eq__(self,r2):
		if self.area() == r2.area():
			return True
		else:
			return False
l1=int(input("Enter length of first rectangle"))
w1=int(input("Enter width"))
r1=Rectangle(l1,w1)
print("Area of first rectangle",r1.area())
l2=int(input("Enter length of second rectangle"))
w2=int(input("Enter width"))
r2=Rectangle(l2,w2)
print("Area of second rectangle",r2.area())
addition=r1+r2
print("Addition of rectangles",addition)
greatest=r1>r2
print("rectangle 1 is greater than rectangle 2",greatest)
eq=(r1==r2)
print("both are equal :",eq)
print(str(r1))
print(Rectangle.__doc__)

