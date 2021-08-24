employee = {} 

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

