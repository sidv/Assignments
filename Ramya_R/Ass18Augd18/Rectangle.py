import math
#parent class
class Rectangle:
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
	def area(self):
		return self.length*self.breadth     
	
length = float(input("Enter length of Rectangle: "))
breadth = float(input("Enter breadth of Rectangle: "))

object = Rectangle(length,breadth)

#area		
print("Area of rectangle: ",object.area())

		
		
		
		   
