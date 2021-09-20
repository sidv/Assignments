
class Rectangle:
	__doc__="\t\tEntering program to compute area of rectangle of given measurements"
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
		print("\t\tMeasurements added")
	def area(self):
		area = self.length * self.breadth
		return (f"\t\tThe area is {area}")
	def __add__(self,b):
		summ = self.length + b.length
		sumb = self.breadth + b.breadth
		return summ , sumb
	
	
		
