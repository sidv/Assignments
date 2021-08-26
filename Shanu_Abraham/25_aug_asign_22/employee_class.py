#creating employee class for GUI
class Employee:
	def __init__(self, emp_id = 0, name = "", gender = "", place = "",salary = 0, prv_company = "",joining_date = 0):
		self.emp_id = emp_id
		self.name = name
		self.gender = gender
		self.place = place
		self.salary = salary
		self.prv_company = prv_company
		self.joining_date = joining_date
