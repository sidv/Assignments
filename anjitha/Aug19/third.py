import math
class Shape:
	
	def area(self):
		
		area=0
		return area
class Square(Shape):
	def __init__(self,l):
		self.l = l
		
	def areas(self):
		print("Computing Area!!")
		a=l*l
		return a
l=int(input("Enter the length"))
r=Square(l)
print("The area of square is"+str(r.areas()))
print(r.area())











