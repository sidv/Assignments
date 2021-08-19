from cars import Car

#child class
class Sedan(Car):	
	#__name__ = "Sedan"
	#__doc__ = "This is sedan car class"
	#__bases__ = ("Car") 
	def __init__(self):
		self.brand = ""
		self.model = ""
		self.speed = ""
		self.color = ""
	def __len__(self):
		#return len(self.brand)
		return 4
	def __str__(self):
		return f"THis is string: {self.brand} | {self.model}"

	def __add__(self,b):
		return int(self.price)+int(b.price)
	

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
		
