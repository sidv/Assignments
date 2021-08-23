#3.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes #have a area function which can print the area of the shape where Shape's area is 0 by default.
#Use Math function
import math
class Shape:
	def area(self,length = 0):
		print(length)
		return (math.pow(length,2))

class Square(Shape):
	def __init__(self,length=0):
		print(length)
		self.length = length
	def area(self):
		return(super().area(self.length))
	
num = int(input("Enter the side length : "))
if num == 0 or num == "":
	s = Square()
	print("Sqaure : ",s.area())
else:
	s = Square(num)
	print("Sqaure : ",s.area())
print(dir(math))
