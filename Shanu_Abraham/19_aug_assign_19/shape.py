#Define a class named Shape and its subclass Square. The Square class
# has an init function which takes a length as argument. Both classes
# have a area function which can print the area of the shape 
#where Shape's area is 0 by default.
#-Use math function to perform here calculation
import math

class Shape:
	def __init__(self):
		return 0


class Square(Shape):
	def __init__(self,length):
		self.lenth = length

	def area(self):
		return  math.pow(self.lenth,2)
length = int(input("\tEnter the length"))
a = Square(length)
a1 = a.area()
print(a1)
