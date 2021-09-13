class Demo:
	def __init__(self):
		self.a = 1
		self.__b = 1
	def disp_self(self):
		return self.__b
obj = Demo()
print(obj.__b)
