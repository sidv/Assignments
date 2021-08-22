from employee_list import employees

class Employee:
	def __init__(self, emp_id = 0, name = "", age = 0, gender = "", place = "", salary = "", prev_company = "", join_date = ""):
		self.emp_id = emp_id
		self.name = name
		self.age = age
		self.gender = gender
		self.place =  place
		self.salary = salary
		self.prev_company = prev_company
		self.join_date = join_date
	def set_name(self,name):
		self.name = name
		return "Name assigned Successfully"
	def set_age(self,age):
		self.age = age
		return "Age assigned Successfully"
	def set_gender(self,gender):
		self.gender = gender
		return "Gender assigned Successfully"
	def set_salary(self,age):
		self.salary = salary
		return "Salary assigned Successfully"
