from cars import Car

#child class
class Sedan(Car):	
	def __init__(self):
		self.brand = ""
		self.model = ""
		self.speed = ""
		self.color = ""
	def insert(self):
		self.brand = input("Brand Name: ")
		self.model = input("Modal Name: ")
		self.speed = input("Speed km/h: ")
		self.color = input("Color: ")
		self.owner = input("Owner Name: ")
		self.manufacturing_date = input("Manufacturing Date: ")
		self.price = input("Price: ")
		self.type = input("Type: ")
	def display(self):
		print(f"\t{self.brand}")
		print(f"\t{self.speed}")
		print(f"\t{self.owner}")
		print(f"\t{self.type}")
		
