from user import User
#child class
class Student(User):
	def __init__(self):
		self.name = ""
		self.age = 0
		self.grade = ""
		self.__gender = ""
		#super().__init__()
	def insert(self):
		print("Enter Student Details:")
		self.name = input("\tName: ")
		self.age = input("\tAge: ")
		self.grade = input("\tGrade :")
		self.__gender = input("\tGender: ")
		self.set_username(input("\tUsername: "))
		self.set_password(input("\tPassword: "))
		self._role = input("Role: ")
	def display(self):
		print("Details:")
		print(f"{self.name} | {self.age} | {self.grade} | {self.__gender} | {self.get_username()} | {self._role}")
		self._data() #Should not use
#		self.__sample() #Not accessible

	def xyz(self):
		super().display()
