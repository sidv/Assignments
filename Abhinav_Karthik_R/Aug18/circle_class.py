class Circle:
	def __init__(self,r):
		self.radius = r

	def area(self):
		print(f"Area is:{self.radius**2*3.14}")

c1=Circle(2)
area = c1.area()
