import math
class shape:
	def area(self,length=0):
		self.length=length
		return (math.pow(length,2))
		
class square(shape):
	def __init__ (self,length):
		self.length=length
	def area(self):
		return (super().area(self.length))

l=int(input("Enter length"))
sh=shape()
sq=square(l)
print(sh.area())
print(sq.area())
