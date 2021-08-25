class rectangle:
	__doc__ ="area of reactnagle class"
	def __init__(self,length,width):
		self.length=length
		self.width =width
	def area(self):
		return  self.length *self.width
	def __add__(self):
		return self.length+self.width
	def __str__(self):
		return f"this reactangle of  :{self.length }  {self.width}"
	def __gt__(self,greater):
		if rec.area() >greater.area():
			return True
		else:
			return False
	def __eq__(self,greater):
		if rec.area() == greater.area():
			return True
		else:
			return False

length=int(input("enter a rect of length:"))
width=int(input("enter a rect of width:"))
rec=rectangle(length,width)
print("area of rectangle:",rec.area())

plus=length+width
print(plus)

greater=rectangle(length,width)
print(rec > greater)

equal=rectangle(length,width)
print(rec==greater)

print(rectangle.__str__)
print(rectangle.__doc__)

