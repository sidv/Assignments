#employee pgm using function
employee = {}


def add_employee():
	#add
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
	#delete
	serial_no = input("Enter serial_no")
	if serial_no not in employee.keys():
		print("Wrong serial number")
	else:
		 del employee[serial_no]


def search_employee():
	#search
	name = input("Enter name")
	found = False
	for i in employee.values():
		if i["name"] == name:
			print(f"{i['name']} | {i['age']} |{i['gender']} |{i['place']} |{i['salary']} | {i['previous_company']} | {i['joining_date']} ")
			found = True
			break
	if found == False :
		print("Not found")

def display_employee():
	for serial,employee in employee.items():
		print(f"{serial} | {employee['name']} | {employee['age']} | {employee['gender']} | {employee['place']} | {employee['salary']} | {employee['previous_company']} | {employee['joining_date']}")
#	for serial,employee in employee.items():
#		print(f"{serial} | {employee['name']} | {employee['age']} | {employee['gender']} | {employee['place']} | {employee['salary']} | {employee['previous_company']} | {employee['joining_date']}")

def change_employee():
	serial_no = input ("Enter serial no")
	if serial_no not in employee.keys():
		print("Wrong serial no")
	else:
		employee[serial_no]['name'] = input("Enter the new name")
		employee[serial_no]['age'] = input("Enter the new age")
		employee[serial_no]['gender'] = input("Enter the new gender")
		employee[serial_no]['place'] = input("Enter the new place")

def main_menu():
	print("1.Add employee details")
	print("2.Delete employee")
	print("3.Search employee")
	print("4.Display all employee details")
	print("5.Change employee data")
	print("6.Exit")


while True:
	main_menu()
	choice = int(input("enter your choice\n"))
	if choice == 1:
		#add
		add_employee()
	elif choice == 2:
		#delete
		delete_employee()			
	elif choice == 3:
		#search
		search_employee()
	elif choice == 4:
		#Display
		display_employee()	
	elif choice == 5 :
		#Change
		change_employee()
	elif choice == 6:
		break;
	else:
		print("invalid choice")
		
