class Calculator:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def sum(self):
		return self.a+self.b
	def sub(self):
		return self.a-self.b
	def mul(self):
		return self.a*self.b
	def div(self):
		return self.a/self.b
	def mod(self):
		return self.a%self.b
	def power(self):
		return self.a**self.b
	#def floordiv(self):
		#return self.a//self.b
