employees = {} #empty List

while True:
	print("1. Add employee")
	print("2. Delete employee")
	print("3. Search employee")
	print("4. Display all employee")
	print("5. Change a employee name in the list") 
	print("6. exit")
	ch = int(input("Enter your choice: "))
	if ch is None:
		print("no data present in Employees")
	elif ch == 1:
		#Add employee
		serial_no = input("\tEnter serial No ")
		if serial_no not in employees.keys():
			name = input("Enter name: ")
			age = int(input("Enter age: "))
			gender = input("Enter the Gender: ")
			place =  input("Enter place: ")
			salary = input("Enter salary: ")
			prev_company = input("Enter previous company: ")
			join_date = input("Enter join date: ")
			empid = input("Enter empid: ") 
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
	elif ch == 2:
		#Delete employee
		print(employees)
		serial_no = input("\tEnter serial no")
		if serial_no not in employees.keys():
			print("\tWrong serial No")
		else:
			del employees[serial_no]
	elif ch == 3:
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


	elif ch == 4:
		#Display employee
		print(employees)
		for serial,employee in employees.items():
			print(f"\t{serial} | {employee['name']} | {employee['age']} | {employee['gender']} | {employee['place']}| {employee['salary']} | {employee['prev_company']} | {employee['join_date']} | {employee['empid']}")
	elif ch== 5:
		#Change a employee name in the list
		#name = input("Enter the name: ")
		serial_no = input("\tEnter serial no.")
		if serial_no not in employees.keys():
			print("\tWrong serial no")
		else:
			employees[serial_no]['name'] = input("\tEnter new name: ")
			employees[serial_no]['age'] = input("\tEnter new age: ")
			employees[serial_no]['gender'] = input("\tEnter new gender: ")
			employees[serial_no]['salary'] = input("\tEnter new salary: ")


	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")
