employee = {} 
groups = {} 
org={}
def add_employee():
	serial_no = input("Enter serial_no")
	if serial_no not in employee.keys():
		name=input("Enter the employee name\n")
		age=int(input("enter the age"))        
		gender=input("enter the gender")
		place=input("Enter the place")
		salary=int(input("Enter the salary"))
		previous_company=input("Enter the previous company")
		joining_date=int(input("Enter the joining date"))
		temp = {
                        "name" : name,
                        "age" : age,
                        "gender" : gender,
                        "place" : place,
                        "salary" : salary,
                        "previous_company" : previous_company,
                        "joining_date" : joining_date
                        }
		employee[serial_no] = temp
	else:
		print("Serial no already taken")



def delete_employee():
	serial_no = input("\tEnter serial no")
	if serial_no not in employee.keys():
		print("\tWrong serial No")
	else:
		del employee[serial_no]
def search_employee():
	#name = input("Enter name")
	#found = False
	#for i in employee.values():
	#	if i["name"] == name:
	#		print(f"{i['name']} | {i['age']} |{i['gender']} |{i['place']} |{i['salary']} | {i['previous_company']} | {i['joining_date']} ")
	#		found = True
	#		break
	#	if found == False :
	#		print("Not found")
	print("Press 1 for search by name")
	print("Press 2 for search by age")
	print("Press 3 for search by salary")
	print("Press 4 for search  by gender")
	print("Press 5 for exit")
	while True:
	
		choice = int(input("Enter choice : "))
		if choice == 1:
			search_by_name()
		elif choice == 2:
			search_by_age()
		elif choice == 3:
			search_by_salary()
		elif choice == 4:
			search_by_gender()
		elif choice == 5:
			break
		else:
			print("Invalid choice")
def search_by_name():	
	name=input("Enter the name: ")
	print(list(filter(lambda a:a["name"] == name, employees.values())))
	print("Employee founded")

def search_by_age():	
	age=int(input("Enter the age of employee : "))
	print(list(filter(lambda a:a["age"] == age, employees.values())))
	print("Employee founded")

def search_by_salary():	
	salary=int(input("Enter the salary of employee: "))
	print(list(filter(lambda a:a["salary"] == salary, employees.values())))
	print("Employee founded")

def search_by_gender():	
	gender=input("Enter the gender of employee : ")
	print(list(filter(lambda a:a["gender"] == gender, employees.values())))
	print("Employee founded")


def display_employee():
	for serial,employee in employee.items():
		print(f"{serial} | {employee['name']} | {employee['age']} | {employee['gender']} | {employee['place']} | {employee['salary']} | {employee['previous_company']} | {employee['joining_date']}")

def change_employee_details():
	print("1.Change employee name")
	print("2.Change employee age")
	print("3.Change employee gender")
	print("4.Change employee salary")
	ch =int(input("\tEnter your choice : "))
	serial_no = input("\tEnter serial no.")
	if cho == 1:
		employee[serial_no]['name'] = input("\tEnter new name")
	elif ch == 2:
		employee[serial_no]['age'] = int(input("Enter the new age"))
	elif ch == 3:
		employee[serial_no]['gender'] = input("Enter the new gender")
	elif ch == 4:
		employee[serial_no]['place'] = input("Enter the new place")
	else:
		print("Invalid choice")

def main_menu():
	print("1. Add employee details")
	print("2. Delete employee")
	print("3. Search employee")
	print("4. Display all employee details")
	print("5.Change employee data")
	print("6.Manage all groups")
	print("7.Exit")


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
	for key,value in groups.items(): 
		name_string = ""
		for i in value:
			name_string = name_string +"|"+employee[i]["name"]
		print(f"{key} => {name_string}")

def manage_group_menu():
	print("\t\t1.Add Member")
	print("\t\t2.Delete Member")
	print("\t\t3.List Members")
#	print("\t\t4.Exit")
	

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
	if serial_no in employee.keys():
		groups[group_name].append(serial_no)
	else:
		print("\t\tWrong serial No.")

def list_member(group_name):
	name_string=""
	for i in groups[group_name]:
		name_string = name_string +"|"+i+"."+employee[i]["name"]
	print(f"{name_string}")

def delete_member(group_name):
	list_member(group_name)
	serial_no = input("\t\tEnter serial no from list")
	if serial_no in groups[group_name]:
		groups[group_name].remove(serial_no)
	else:
		print("\t\tWrong serial No.")

def display_member(team_name):
	name_string=""
	for i in teams[team_name]:
		name_string=name_string +"|"+i+"."+employee[i]["name"]
	print(f"{name_string}")

def add_oganization():
	org['name']=input("Enter organization name")
	org['email']=input("Enter organization  email")

def edit_oganization():
	print("1.Edit Organization name ")
	print("2.Edit Organization email")
	choice = int(input("Enter choice: "))
	if choice == 1:
		org['name'] = input("Enter new organization name")
	elif choice == 2:
		org['email'] = input("Enter new organization email")	
	else:
		print("Invalid choice")
def display_organization():
	print(org)
def org_details():
	print("1.Add Organization")
	print("2.Edit Organization")
	print("3.Display Organization details")
	print("4.Exit")
	while True:
		choice = int(input("Enter choice : "))
		if choice == 1:
			add_oganization()
		elif choice == 2:
			edit_oganization()
		elif choice == 3:
			display_organization()
		elif choice == 4:
			break
		else:
			print("Invalid choice")	

while True:
	org_details()
	main_menu()
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add employee
		add_employee()
	elif ch == 2:
		#Delete employee
		delete_employee()
	elif ch == 3:
		#Search employee
		search_employee()
	elif ch == 4:
		#Display 
		display_employee()
	elif ch== 5:
		#Change 
		change_employee_details()
	elif ch == 6:
		#Manage groups
		manage_all_groups()
	elif ch == 7:
		#Exit
		break;
	else:
		print("Invalid Choice")

