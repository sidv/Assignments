#2.Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the #area
#-Implement + operation (Perform addition of length and width)
#-Implement documentation attribute(_doc_ attribute)
#-Implement string typecasting and print "The length is ..value.. and width is ..value.."(_str_)
#-Implement > operation(_gt_(self,other) and return true or false if area is greater or smaller)
#-Implement == operation(_eq_(self,other) and return true or false if area is equal or not)
class Rectangle:
	__doc__ = "Rectangle operation"
	def __init__(self,length,width): 
		self.length = length
		self.width = width
	def area(self):
		return(self.length)*(self.width)
	def __add__(self,others):
		length_sum = self.length + others.length
		width_sum = self.width + others.width
		return (length_sum + width_sum)
	def __str__(self):
		return f"The length is  : {self.length} and width is {self.width}"
	def __gt__(self,other):
		print(self.area())
		if self.area() > other.area():
			return True
		else:
			return False
	def __eq__(self,other):
		if self.area() == other.area():
			return True
		else:
			return False
		
length = int(input("Enter the length : "))
width = int(input("Enter the width : "))
r1 = Rectangle(length,width)
r2 = Rectangle(2,3)
print("*****__doc__Attribute*****")
print(r1.__doc__)
print("*****Area of a Rectangle*****")
print(r1.area())
print("*****A=ddition of length and width*****")
r = r1+r2
print(r)
print("*****Greatest of Area*****")
print(r1 > r2)
print("*****Equal of Area*****")
print(r1 == r2)
print("*****str() of length and width*****")
print(str(r1))


