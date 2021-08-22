employees = {} #empty List
import Employees as e

def search_employee_menu():
	print("\t1.Search by name")
	print("\t2.Search by age")
	print("\t3.Search by empid")
	print("\t4.exit")


def search_emp_by_age():
	age = int(input("\t\tEnter age"))
	for i in e.employees.values():
		if i["age"] == age: # find name
			print(f"\t{i['name']} | {i['age']} | {i['gender']} | {i['place']} | {i['salary']} | {i['prev_company']} | {i['join_date']} | {i['empid']}")
			found = True
	if found == False :
		print("\t\tNot found")
	
def search_emp_by_empid():
	empid = input("\t\tEnter empid")
	for i in e.employees.values():
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
	for i in e.employees.values():
		if i["name"] == name: # find name
			print(f"\t{i['name']} | {i['age']} | {i['gender']} | {i['place']} | {i['salary']} | {i['prev_company']} | {i['join_date']} | {i['empid']}")
			found = True
			break		
	if found == False :
		print("\tNot found")

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
		print(list(filter(lambda a: a["name"] == name,e.employees.values())))
	elif choice == 2:
		age = int(input("\t\tEnter age"))
		print(list(filter(lambda a: a["age"] == age,e.employees.values())))
	elif choice == 3:
		gender = input("\t\tEnter gender you want to search: ")
		print(list(filter(lambda a: a["gender"] == gender,e.employees.values())))
	elif choice == 4:
		salary = input("\t\tEnter salary you want to search: ")
		print(list(filter(lambda a: a["salary"] == salary,e.employees.values())))
	#else:	
		#print("\t invalid choice")
