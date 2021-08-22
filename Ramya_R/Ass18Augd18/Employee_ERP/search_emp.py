from employee import Employee

from employee_list import employees


def search_employee_menu():
	print("\t1.Search by name")
	print("\t2.Search by age")
	print("\t3.Search by salary")
	print("\t4.search by gender")
	print("\t5.exit")
	
def search_employee():
	while True:
		search_employee_menu()
		ch = int(input("\tEnter your choice"))
		if ch == 1:
			#Search by name
			search_emp_by_name()
		elif ch == 2:
			#Search by age
			search_emp_by_age()
		elif ch == 3:
			#search by salary
			search_emp_by_salary()
		elif ch == 4:
			#search by gender
			search_emp_by_gender()
		elif ch == 5:
			#exit
			break
		else:
			print("Invalid choice")		


def search_emp_by_name():
	#Search employee by name
	name = input("Enter name :")
	emp = list(filter(lambda a: a.name == name , employees))
	if len(emp) == 0: 
		print("No employee found")
	else:
		for i in emp:
			print(f"{i.name}")
			print(f"{i.name} | {i.age} | {i.gender} | {i.place} | {i.salary} | {i.prev_company} | {i.join_date}")
			
def search_emp_by_age():

	#Search employee by age
	age = input("Enter age :")
	emp = list(filter(lambda a: a.age == age , employees))
	if len(emp) == 0: 
		print("No employee found")
	else:
		for i in emp:
			print(f"{i.age}")
			print(f"{i.name} | {i.age} | {i.gender} | {i.place} | {i.salary} | {i.prev_company} | {i.join_date}")
					
def search_emp_by_salary():
	#Search employee by salary
	salary = input("Enter salary :")
	emp = list(filter(lambda a: a.salary == salary , employees))
	if len(emp) == 0: 
		print("No employee found")
	else:
		for i in emp:
			print(f"{i.salary}")
			print(f"{i.name} | {i.age} | {i.gender} | {i.place} | {i.salary} | {i.prev_company} | {i.join_date}")

def search_emp_by_gender():
	#Search employee by gender
	gender = input("Enter gender :")
	emp = list(filter(lambda a: a.gender == gender , employees))
	if len(emp) == 0: 
		print("No employee found")
	else:
		for i in emp:
			print(f"{i.gender}")
			print(f"{i.name} | {i.age} | {i.gender} | {i.place} | {i.salary} | {i.prev_company} | {i.join_date}")

			
