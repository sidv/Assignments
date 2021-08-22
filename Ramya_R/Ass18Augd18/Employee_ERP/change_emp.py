from employee import Employee
from employee_list import employees

def change_employee():
	#Change a employee detailes
	print("\t Enter 1 for change name")
	print("\t Enter 2 for change age ")
	print("\t Enter 3 for change gender ")
	print("\t Enter 4 for change salary ")

	choice = int(input("\tEnter the choice which u want to change: "))
	emp_id = input("Enter employee id: ")
	emp_temp  = list(filter(lambda a: a.emp_id == emp_id, employees))
	if choice == 1:
		emp_temp[0].set_name(input("Enter new name: "))
	elif choice == 2:
		emp_temp[0].set_age(input("Enter new age: "))
	elif choice == 3:
		emp_temp[0].set_gender(input("Enter new gender: "))
	elif choice == 4:
		emp_temp[0].set_salary(input("Enter new salary: "))
	#else:
		#print("\t invalid choice")
