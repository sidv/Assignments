import math
#parent class
class Rectangle:
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
	def area(self):
		return self.length*self.breadth     
	def __add__(self, length, breadth):
		return self.length+self.breadth
	def __str__(self):
		return f'length is {self.length} and breadth is {self.breadth}'
	def __gt__(self,other):
		if self.area() > other.area():
			return True	
		else:
			return False
	def __eq__(self,other):
		if self.area() == other.area():
			return True	
		else:
			return False
			
length = float(input("Enter length of Rectangle: "))
breadth = float(input("Enter breadth of Rectangle: "))
object = Rectangle(length,breadth)
#area		
print("Area of rectangle: ",object.area())

#add
#other = Rectangle(4,6)
#c=object+other
#print(c)

#doc
print(Rectangle.__doc__)
#str
print(str(object))
#gt
length = float(input("Enter length of Rectangle: "))
breadth = float(input("Enter breadth of Rectangle: "))
other = Rectangle(length,breadth)
print(object > other)
#eq		
print(object == other)	
		

		
		
		
		
		
		   
