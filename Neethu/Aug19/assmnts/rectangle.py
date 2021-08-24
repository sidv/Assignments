import math
class Rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b
	def area(self):
		print("Area")
		a=l*b
		print(a)
	def __add__(self,o):
		f=self.l + o.l
		s=self.b + o.b
		return Rectangle(f,s)
	def __str__(self):
		return 'The length is' + str(self.l) +'and The width is'+str(self.b)
	
	def __gt__(self,o):
		return
	def __eq__(self,o):
		return
	
l=int(input("enter the length : "))
b=int(input("enter the breadth : "))
r=Rectangle(l,b)
print(r.area())
o=Rectangle(5,5)
c=r+o
print(c)
print(str(r))
