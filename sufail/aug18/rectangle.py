class rectangle:
	def __init__(self,l,w):
		self.length=l
		self.width=w

	def area(self):
		return (self.length*self.width)

r=rectangle(2,2)
print(r.area())
