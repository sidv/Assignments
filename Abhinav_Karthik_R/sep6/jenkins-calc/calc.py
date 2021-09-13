class Calc:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def add(self):
		return f"the sum is {self.a+self.b}"

	def sub(self):
		return f"the difference is {self.a-self.b}"

	def mul(self):
		return f"Multiplication result is {self.a*self.b}"

	def div(self):
		return f"Division result is {self.a/self.b}"
