from cars import Car

#child class
class SUV(Car):
	def __init__(self):
		self.company = ""
		self.top_speed = ""
		self.length = ""
		self.weight = ""
		self.height = ""
	def insert(self):
		self.company = input("Company Name: ")
		self.weight = input("Weight: ")
		self.top_speed = input("Top Speed km/h: ")
		self.height = input("Height: ")
		self.length = input("Length: ")
		self.owner = input("Owner Name: ")
		self.manufacturing_date = input("Manufacturing Date: ")
		self.price = input("Price: ")
		self.type = input("Type: ")
	def display(self):
		print(f"\t{self.company}")
		print(f"\t{self.weight}")
		print(f"\t{self.owner}")
		print(f"\t{self.type}")


