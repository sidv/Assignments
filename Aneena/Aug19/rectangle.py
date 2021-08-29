
import math
class Rectangle():
	
	def __init__(self, l, w):
		self.length = l
		self.width  = w
	def rectangle_area(self):
        	return self.length*self.width
	def __add__(self,op):
		x=self.l + op.l
		y=self.b + op.w
		return Rectangle(x,y)
	def __str__(self):
		return "Length of rectangle :"+ str(self.l) + "width of rectangle :" + str(self.w)
	def __gt__(self,op):
		return
	def __eq__(self,op):
		return
		
l=int(input("Enter the length\n"))
w=int(input("Enter the width\n")) 
area=Rectangle(l,w)
print(area.rectangle_area())
op=Rectangle(5,5)
c=area+op
print(c)
print(str(r))
