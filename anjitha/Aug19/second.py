import math
class Rectangle:
	
	def __init__(self,l,b):
		self.l = l
		self.b = b
	def area(self):
		print("Computing Area!!")
		a=l*b
		return a
	def __add__(self,o):
		f=self.l + o.l
		s=self.b + o.b
		return Rectangle(f,s) 
	def __str__(self):
		return 'The length is'+ str(self.l) +'and The width is ' +str(self.b)
	def __gt__(self,o):
		return self.area() > o.area()
	def __eq__(self,o):
		
		return self.area() == o.area()
		
l=int(input("Enter the length"))
b=int(input("Enter the breadth"))
r=Rectangle(l,b)
print(r.area())
o=Rectangle(5,5)
c=r+o
print(c)
print(str(r))
d=r>o
print(d)
f=r==o
print(f)

