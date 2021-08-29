
employee = {}
def search_menu():
	print("Change employee data")
	print("\ta. search by Name")
	print("\tb. search by age")
	print("\tc. search by gender")
	print("\td. search by salary")
	print("\te. Exit")		
def update_menu():
	print("Change employee data")
	print("\ta. Change Name")
	print("\tb. Change age")
	print("\tc. Change gender")
	print("\td. Change salary")
def add_employee():
	print("Add Employee")
	emp_id  = int(input("Enter id"))
	if emp_id not in employee.keys():
		employee[emp_id]  = {
			"emp_name" : input("Enter name"),
			"emp_age" : int(input("Enter age")),
			"emp_gender" : input("Gender"),
			"emp_sal" : input ("Enter salary"),
			"emp_place" : input("Enter place"),
			"emp_joindate" : input("Enter joined date"),
			"emp_prevcomp" : input("Enter previous company")
		}
	else:
		print("employee ID already taken")
		
def delete_employee():
	print("Delete Employee")
	emp_id = int(input("Enter employee ID"))
	if emp_id not in employee:
		print("Enter valid Emp_ID")
	else:
		del employee[emp_id]

def search_employee_options():
	search_menu()
	ch = input("Enter the choice")
	if ch == "a":
		name = input("Enter the name to be search")
		print(list(filter(lambda a: a["emp_name"] == name,employee.values())))
	elif ch == "b":
		age = int(input("Enter the name to be search"))
		print(list(filter(lambda a: a["emp_age"] == age,employee.values())))
	elif ch == "c":
		gender = input("Enter the name to be search")
		print(list(filter(lambda a: a["emp_gender"] == gender,employee.values())))
	elif ch == "d":
		salary = input("Enter the name to be search")
		print(list(filter(lambda a: a["emp_sal"] == salary,employee.values())))
	else:	
		print("Invalid choice")
		
def display_employee():
	for emp_id,emp_det in employee.items():
		print(f"{emp_id} | {emp_det['emp_name']} | {emp_det['emp_age']} | {emp_det['emp_gender']} | {emp_det['emp_sal']}")

	
def update_empoyee():
	emp_id = int(input("Enter employee id"))
	update_menu()
	choice = input("\tEnter the choice")
	if emp_id in employee.keys():
		if choice == "a":
			name = input("\tEnter new name")
			employee[emp_id]["emp_name"] = name
		elif choice == "b":
			age = input("\tEnter new age")
			employee[emp_id]["emp_age"] = age
		elif choice == "c":
			gender = input("\tEnter new gender")
			employee[emp_id]["emp_gender"] = gender
		elif choice == "d":
			sal = input("\tEnter new salary")
			employee[emp_id]["emp_sal"] = sal
		else:
			print("Wrong choice")

def search_employee():# Currently not using
	print("Search employee by name")
	name = input("Enter the name to be search")
	flag = False
	for ename in employee.values():
		if ename["emp_name"] == name :
			flag = True
	if flag == True:
		print(f"{name} is found")
	else:
		print(f"{name} is not found")
