employees = {} #empty List
organization = {}
teams = {}

def main_menu():
	print("1. Add employee")
	print("2. Delete employee")
	print("3. Search employee")
	print("4. Display all employee")
	print("5. Change a employee name in the list") 
	print("6.Manage all groups")
	print("7.Manage organization details")
	print("8. exit")

def add_employee():
	#Add employee
	serial_no = input("\tEnter serial No: ")
	if serial_no not in employees.keys():
		name = input("\tEnter name: ")
		age = int(input("\tEnter age: "))
		gender = input("\tEnter the Gender: ")
		place =  input("\tEnter place: ")
		salary = input("\tEnter salary: ")
		prev_company = input("\tEnter previous company: ")
		join_date = input("\tEnter join date: ")
		empid = input("\tEnter empid: ") 
		temp ={
			"name":name,
			"age":age,
			"gender":gender,
			"place":place,
			"salary":salary,
			"prev_company":prev_company,
			"join_date":join_date,
			"empid":empid
			}
		employees[serial_no] = temp
	else:
		print("\tSerial No already Taken")
def delete_employee():
	#Delete employee
	print(employees)
	serial_no = input("\tEnter serial no: ")
	if serial_no not in employees.keys():
		print("\tWrong serial No")
	else:
		del employees[serial_no]

def search_employee_menu():
	print("\t1.Search by name")
	print("\t2.Search by age")
	print("\t3.Search by stream")
	print("\t4.exit")


def search_emp_by_age():
	age = int(input("\t\tEnter age"))
	for i in employees.values():
		if i["age"] == age: # find name
			print(f"\t{i['name']} | {i['age']} | {i['gender']} | {i['place']} | {i['salary']} | {i['prev_company']} | {i['join_date']} | {i['empid']}")
			found = True
	if found == False :
		print("\t\tNot found")
	
def search_emp_by_empid():
	empid = input("\t\tEnter empid")
	for i in employees.values():
		if i["empid"] == empid: # find empid
			print(f"\t{i['name']} | {i['age']} | {i['gender']} | {i['place']} | {i['salary']} | {i['prev_company']} | {i['join_date']} | {i['empid']}")
			found = True
	if found == False :
		print("\t\tNot found")


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
			#search by empid
			search_emp_by_empid()
		elif ch == 4:
			#exit
			break
		else:
			print("Invalid choice")	

def search_emp_by_name():
	#Search employee
	name = input("\t\tEnter name you want to search: ")
	found = False
	for i in employees.values():
		if i["name"] == name: # find name
			print(f"\t{i['name']} | {i['age']} | {i['gender']} | {i['place']} | {i['salary']} | {i['prev_company']} | {i['join_date']} | {i['empid']}")
			found = True
			break		
	if found == False :
		print("\tNot found")
		
def display_employee():
	#Display employee
	#print(employees)
	for serial,employee in employees.items():
		print(f"\t{serial} | {employee['name']} | {employee['age']} | {employee['gender']} | {employee['place']}| {employee['salary']} | {employee['prev_company']} | {employee['join_date']} | {employee['empid']}")

def search_employee_lambda():
		#search a employee detailes
	print("\t Enter 1 for search name")
	print("\t Enter 2 for search age ")
	print("\t Enter 3 for search gender ")
	print("\t Enter 4 for search salary ")

	choice = int(input("\tEnter the choice which u want to search: "))
	#serial_no = input("\tEnter serial no: ")
	if choice == 1:
		name = input("\t\tEnter name you want to search: ")
		print(list(filter(lambda a: a["name"] == name,employees.values())))
	elif choice == 2:
		age = int(input("\t\tEnter age"))
		print(list(filter(lambda a: a["age"] == age,employees.values())))
	elif choice == 3:
		gender = input("\t\tEnter gender you want to search: ")
		print(list(filter(lambda a: a["gender"] == gender,employees.values())))
	elif choice == 4:
		salary = input("\t\tEnter salary you want to search: ")
		print(list(filter(lambda a: a["salary"] == salary,employees.values())))
	#else:	
		#print("\t invalid choice")
		
def change_employee():
		#Change a employee detailes
	print("\t Enter 1 for change name")
	print("\t Enter 2 for change age ")
	print("\t Enter 3 for change gender ")
	print("\t Enter 4 for change salary ")

	choice = int(input("\tEnter the choice which u want to change: "))
	serial_no = input("\tEnter serial no: ")
	if choice == 1:
		employees[serial_no]['name'] = input("\tEnter new name: ")
	elif choice == 2:
		employees[serial_no]['age'] = input("\tEnter new age: ")
	elif choice == 3:
		employees[serial_no]['gender'] = input("\tEnter new gender: ")
	elif choice == 4:
		employees[serial_no]['salary'] = input("\tEnter new salary: ")
	#else:
		#print("\t invalid choice")

def manage_all_team_menu():
	print("\t1.Create team")
	print("\t2.Display teams")
	print("\t3.Manage team(Particular)")
	print("\t4.Delete team")
	print("\t5.Rename team")
	print("\t6.Exit")
def manage_all_teams():
	while True:
		manage_all_team_menu()
		ch = int(input("\tEnter your choice "))
		if ch == 1:
			#Create team
			create_team()
		elif ch == 2:
			#display teams
			display_teams()
		elif ch == 3:
			#Manage group(Particular)
			manage_team()
		elif ch == 4:
			#Delete team
			delete_team()
		elif ch == 5:
			#Rename team
			rename_team()
		elif ch == 6:
			#exit
			break
		else:
			print("\tInvalid choice")	

def create_team():
	team_name = input("\tEnter team name: ")
	teams[team_name] = []

def rename_team():
	team_name = input("\tEnter team name: ")
	newteam_name = input("\tEnter new team name: ")
	prev=teams[team_name]
	del teams[team_name]
	teams[newteam_name] = prev

def delete_team():
	team_name = input("\tEnter team name: ")
	if team_name in teams.keys():
		del teams[team_name]
		print("\tDeleted the team")
	else:
		print("\tWrong team name")

def display_teams():
	for key,value in teams.items(): #key is team_name,value is list of student serial no
		name_string = ""
		for i in value:
			name_string = name_string +"|"+employees[i]["name"]
		print(f"{key} => {name_string}")

def manage_team_menu():
	print("\t\t1.Add Member")
	print("\t\t2.Delete Member")
	print("\t\t3.List Members")
#	print("\t\t4.Exit")
	

def manage_team():
	team_name = input("\t\tEnter team name: ")
	manage_team_menu()
	ch = int(input("\t\t Enter your Choice: "))
	if ch == 1:
		#Add member
		add_member(team_name)
	elif ch == 2:
		#Delete member
		delete_member(team_name)
	elif ch == 3:
		#List member
		list_member(team_name)
	else:
		print("\tInvalid choice")	
	
def add_member(team_name):
	display_employee()
	serial_no = input("\t\tEnter the serial no of employee: ")
	if serial_no in employees.keys():
		teams[team_name].append(serial_no)
	else:
		print("\t\tWrong serial No.")

def list_member(team_name):
	name_string=""
	for i in teams[team_name]:
		name_string = name_string +"|"+i+"."+employees[i]["name"]
	print(f"{name_string}")

def delete_member(team_name):
	list_member(team_name)
	serial_no = input("\t\tEnter serial no from list")
	if serial_no in teams[team_name]:
		teams[team_name].remove(serial_no)
	else:
		print("\t\tWrong serial No.")

	
def org_menu():
	print("\t1.Add organization")
	print("\t2.view organization")
	print("\t3.edit organization")
	print("\t4.delete organization")
	#print("\t5.exit")
	
	
def manage_all_organizations():
	org_menu()
	ch = int(input("\tEnter your choice "))
	if ch == 1:
		#Create organization
		add_org()
	elif ch == 2:
		#display organization
		display_org()
	elif ch == 3:
		#edit organization details
		edit_org()
	elif ch == 4:
		#Delete organization
		delete_org()
	#elif ch == 5:
		#exit
		#break
	else:
		print("\tInvalid choice")
	
	
def add_org():
	org_id = input("Enter org id: ")
	
	organization[org_id] ={
		"name":input("\tEnter name "),
		"email":input("\tEnter email "),
		"phno":input("\tEnter the phno "),
		"address":input("\tEnter address ")
	}
#	else:
#		print("\tid already Taken")

def edit_org():
	#Change a employee detailes
	print("\t Enter 1 for change name")
	print("\t Enter 2 for change email ")
	print("\t Enter 3 for change phno ")
	print("\t Enter 4 for change address ")

	choice = int(input("\tEnter the choice which u want to change: "))
	org_id = input("\tEnter org id: ")
	if choice == 1:
		organization[org_id]['name'] = input("\tEnter new name: ")
	if choice == 2:
		organization[org_id]['email'] = input("\tEnter new email: ")
	if choice == 3:
		organization[org_id]['phno'] = input("\tEnter new gender: ")
	if choice == 4:
		organization[org_id]['address'] = input("\tEnter new Address: ")
	#else:
		#print("\t invalid choice")

def display_org():
	#Display organization
	print(organization)
	for org_id,i in organization.items():
		print(f"\t{org_id} | {i['name']} | {i['email']} | {i['phno']} | {i['address']}")
def delete_org():
	org_id = input("\tEnter org id: ")
	if org_id not in organization.keys():
		print("\tWrong serial No")
	else:	
		del organization[org_id]
while True:
	main_menu()
	ch = int(input("Enter your choice: "))
	if ch is None:
		print("no data present in Employees")
	elif ch == 1:
		#Add employee
		add_employee()
	elif ch == 2:
		#Delete employee
		delete_employee()
	elif ch == 3:
		#Search employee
		#search_employee()
		search_employee_lambda()
	elif ch == 4:
		#Display employee
		display_employee()
	elif ch== 5:
		#Change a employee name in the list
		change_employee()
	elif ch== 6:
		#Manage all groups in the list
		manage_all_teams()
	elif ch== 7:
		#Manage all organizations in the list
		manage_all_organizations()
	elif ch == 8:
		#Exit
		break;
	else:
		print("Invalid Choice")
		
#organization = {}

	
