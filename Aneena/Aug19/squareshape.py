class shape:
	def area(self):
		return 0
class square(shape):
	def __init__(self,l):
		self.length=l
	def __area(self):
		return self.length*self.length
l=int(input("enter the length")
x=square(l)
print("Area :"+str(x.area()))
print(x.area())
