#Parent class
# __ double underscore variable are super private ,accessible only inside class
# _ single underscore variable are partially private,Accessible inside child class also outside( YOu should not use this publicly)(You have reseverd this variable for personal use)
class User:
	def __init__(self):
		self.__username = ""  #Use __ underscore to create private attribute of class. Private attribute are not accessible outside class
		self.__password = ""
		self._role = ""
	def set_username(self,username):
		self.__username = username
	def get_username(self):
		return self.__username

	def set_password(self,password):
		self.__password = password
	def get_password(self):
		return self.__password

	def _data(self): #YOu can access this function anywhere but should not use because author of library have reserved for personal use
		print("This is _data function")
	def __sample(self): #Super private you cannot access outside class
		print("This is __sample function ")

	def display(self):
		print("This is user class display function")

