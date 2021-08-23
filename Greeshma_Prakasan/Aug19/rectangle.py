class Rectangle:
	__doc__ = "this class for rectangle"
	def __init__(self,l,w):
		self.length = l
		self.width = w

	def get_area(self):
		area = self.length*self.width
		return area

	def __add__(self,other):
		
		l = self.length+other.length
		w = self.width+other.width
		return Rectangle(l,w)

	def __str__(self):
		return "the length is "+str(self.length)+" the width is "+str(self.width)

	def __gt__(self,other):
		return self.get_area() > other.get_area()
	
	def __eq__(self,other):
		return self.get_area() == other.get_area()	

r1 = Rectangle(8,9)
r2 = Rectangle(4,5)
print(r1.get_area())
r = r1+r2
print(r.length)
print(str(r1))
print(r1.__doc__)
print(r1 > r2)
print(r1 == r2)
