class Student:
	def __init__(self, st_id = 0, name = "", age = 0, grade = ""):
		self.st_id = st_id
		self.name = name
		self.age = age
		self.grade = grade
	def set_name(self,name):
		self.name = name
		return "Name assigned Successfully"
	def set_age(self,age):
		self.age = age
		return "Age assigned Successfully"
