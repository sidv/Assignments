class rectangle:
	def __init__(self,length,width):
		self.length=length
		self.width =width
	def area(self):
		return  self.length *self.width
len=int(input("enter a rect of length:"))
wid=int(input("enter a rect of width:"))
rec=rectangle(len,wid)
print("area of rectangle:",rec.area())
