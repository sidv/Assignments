from emp_class import Employee 
from emp_store import employees

def update_employee():
	print("Enter 1 for change name")
	print("Enter 2 for change age")
	print("Enter 3 for change gender")
	print("Enter 4 for change salary")	
	cho =int(input("\tEnter your choice."))
	employee_id = input("\tEnter employee id.")
	if cho == 1:
		for i in employees:
			if i.e_id == employee_id: 
				i.name = input("\tEnter new name") 
	elif cho == 2:
		for i in employees:
			if i.e_id == employee_id: 
				i.age = input("\tEnter new age") 
	elif cho == 3:
		for i in employees:
			if i.e_id == employee_id: 
				i.gender = input("\tEnter new gender") 

	elif cho == 3:
		for i in employees:
			if i.e_id == employee_id: 
				i.salary = input("\tEnter new salary") 
	else:
		print("invalid choice!!")

