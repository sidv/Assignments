
class Employee:
	def __init__(self, empid=0 , name="" , age=0 , gender="" , salary="", place="", previous_company="", joining_date=""):
		self.empid=empid
		self.name=name
		self.age=age
		self.gender=gender
		self.salary=salary
		self.place=place
		self.previous_company=previous_company
		self.joining_date=joining_date
	def set_name(self,name):
		self.name=name
		return "Name sucessfully assigned"
	def set_age(self,age):
		self.age=age
		return "Age sucessfully assigned"
	def set_gender(self,gender):
		self.gender=gender
		return "Gender sucessfully assigned"
	def set_salary(self,salary):
		self.salary=salary
		return "Salary sucessfully assigned"
	def set_place(self,place):
		self.place=place
		return "Place sucessfully assigned"
	def set_previous_company(self,previous_company):
		self.previous_company=previous_company
		return "Previous company sucessfully assigned"
	def set_joining_date(self,joining_date):
		self.joining_date=joining_date
		return "Joining date sucessfully assigned"
		

