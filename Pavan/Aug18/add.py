from emp_class import Employee 
from emp_store import employees

def add_employee():
	e_id = input("\tEnter employee id : ")
	name = input("\tEnter name : ")
	age = input("\tEnter employee age : ")
	gender = input("\tEnter gender : ")
	place = input("\tEnter place : ")
	salary = input("\tEnter salary : ")
	previous_company = input("\tEnter previous company : ")
	joining_date = input("\tEnter joining_date : ")
	
	st_temp = Employee(e_id,name,age,gender,place,salary,previous_company,joining_date)
	employees.append(st_temp)

