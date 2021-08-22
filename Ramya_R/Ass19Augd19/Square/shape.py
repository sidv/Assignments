import math
#parent class
class Shape:
	def __init__(self,side):
		self.side = side
	def area(self,side=0):
		return self.side*self.side
	
