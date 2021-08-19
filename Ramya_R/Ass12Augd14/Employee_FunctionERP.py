employees = {} #empty List

def main_menu():
	print("1. Add employee")
	print("2. Delete employee")
	print("3. Search employee")
	print("4. Display all employee")
	print("5. Change a employee name in the list") 
	print("6. exit")

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
		
def search_employee():
	#Search employee
	name = input("Enter name you want to search: ")
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
	print(employees)
	for serial,employee in employees.items():
		print(f"\t{serial} | {employee['name']} | {employee['age']} | {employee['gender']} | {employee['place']}| {employee['salary']} | {employee['prev_company']} | {employee['join_date']} | {employee['empid']}")
		
def change_employee():
	#Change a employee name in the list
	#name = input("Enter the name: ")
	serial_no = input("\tEnter serial no: ")
	if serial_no not in employees.keys():
		print("\tWrong serial no")
	else:
		employees[serial_no]['name'] = input("\tEnter new name: ")
		employees[serial_no]['age'] = input("\tEnter new age: ")
		employees[serial_no]['gender'] = input("\tEnter new gender: ")
		employees[serial_no]['salary'] = input("\tEnter new salary: ")



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
		search_employee()
	elif ch == 4:
		#Display employee
		display_employee()
	elif ch== 5:
		#Change a employee name in the list
		change_employee()
	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")
