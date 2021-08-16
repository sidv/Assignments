def main_menu():
	print("Press 1 for add employee")
	print("Press 2 for delete employee ")
	print("Press 3 for search employee")
	print("Press 4 for change employee details")
	print("Press 5 for managing the teams in the company")
	print("Press 6 for display  employee")
	print("Press 7 for Quit")
	
def add_employee():
	employee_id = input("\tEnter Employee id ")
	if employee_id not in employees.keys():
		name = input("\tEnter name ")
		age = int(input("\tEnter age "))
		gender = input("\tEnter the gender ")
		place = input("\tEnter place ")
		salary = int(input("\tEnter salary "))
		previous_company = input("\tEnter your previous company ")
		joining_date = input("\tEnter joining date ")
		temp ={
			"name":name,
			"age":age,
			"gender":gender,
			"place":place,
			"salary":salary,
			"previous_company":previous_company,
			"Joining_date":joining_date,
			}
		employees[employee_id] = temp
	else:
		 print("\tEmployee id  already Taken")
def delete_employee():
	eID = input("\tEnter employee id") 
	if eID not in employees.keys():
		print("\tWrong Employee id")
	else:
		del employees[eID]
def search_employee():
	name = input("\tEnter name")
	found = False
	for i in employees.values():
			if i["name"] == name: 
				print(f"\t{i['name']} | {i['age']} | {i['place']} | {i['gender']} | {i['previous_company']} | {i['salary']} ")
				found = True
				break
	if found == False :
		print("\tNot found")
def display_employee():
	for id,employee in employees.items():
		print(f"\t{id} | {employee['name']} | {employee['age']} | {employee['place']} | {employee['gender']} | {employee['previous_company']} | {employee['salary']} ")
def update_employee():
	print("Enter 1 for change name")
	print("Enter 2 for change age")
	print("Enter 3 for change gender")
	print("Enter 4 for change salary")	
	cho =int(input("\tEnter your choice."))
	employee_id = input("\tEnter employee id.")
	if cho == 1:
		employees[employee_id]['name'] = input("\tEnter new name") 
	elif cho == 2:
		employees[employee_id]['age'] = input("\tEnter new age")
	elif cho == 3:
		employees[employee_id]['gender'] = input("\tEnter gender")
	elif cho == 3:
		employees[employee_id]['salary'] = input("\tEnter new salary")
	else:
		print("invalid choice!!")

def manage_all_group_menu():
	print("\t1.Create Group")
	print("\t2.Display Groups")
	print("\t3.Manage Group(Particular)")
	print("\t4.Delete Group")
	print("\t5.Exit")

def manage_all_groups():
	while True:
		manage_all_group_menu()
		ch = int(input("\tEnter your choice "))
		if ch == 1:
			#Create group
			create_group()
		elif ch == 2:
			#display groups
			display_groups()
		elif ch == 3:
			#Manage group(Particular)
			manage_group()
		elif ch == 4:
			#Delete Group
			delete_group()
		elif ch == 5:
			#exit
			break
		else:
			print("\tInvalid choice")	

def create_group():
	group_name = input("\tEnter group name ")
	groups[group_name] = []

def delete_group():
	group_name = input("\tEnter group name ")
	if group_name in groups.keys():
		del groups[group_name]
		print("\tDeleted the group")
	else:
		print("\tWrong group name")

def display_groups():
	for key,value in groups.items(): #key is group_name,value is list of employee serial no
		name_string = ""
		for i in value:
			name_string = name_string +"|"+employees[i]["name"]
		print(f"{key} => {name_string}")

def manage_group_menu():
	print("\t\t1.Add Member")
	print("\t\t2.Delete Member")
	print("\t\t3.List Members")
	

def manage_group():
	group_name = input("\t\tEnter group name ")
	manage_group_menu()
	ch = int(input("\t\t Enter your Choice "))
	if ch == 1:
		#Add member
		add_member(group_name)
	elif ch == 2:
		#Delete member
		delete_member(group_name)
	elif ch == 3:
		#List member
		list_member(group_name)
	else:
		print("\tInvalid choice")	
	
def add_member(group_name):
	display_employee()
	serial_no = input("\t\tEnter the serial no of student ")
	if serial_no in employees.keys():
		groups[group_name].append(serial_no)
	else:
		print("\t\tWrong serial No.")

def list_member(group_name):
	name_string=""
	for i in groups[group_name]:
		name_string = name_string +"|"+i+"."+employees[i]["name"]
	print(f"{name_string}")

def delete_member(group_name):
	list_member(group_name)
	serial_no = input("\t\tEnter serial no from list")
	if serial_no in groups[group_name]:
		groups[group_name].remove(serial_no)
	else:
		print("\t\tWrong serial No.")

	
	

groups={}
employees={}
while True:
	
	main_menu()
	ch = int(input("Enter choice"))
	if ch == 1:
		add_employee()
	elif ch == 2:
		delete_employee()
	elif ch == 3:
		search_employee()
	elif ch == 4:
		update_employee()
	elif ch == 5:
		manage_all_groups()	
	elif ch == 6:
		display_employee()
	elif ch == 7:
		break;
	else:
		print("Invalid Choice")

