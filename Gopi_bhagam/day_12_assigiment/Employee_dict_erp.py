employee = {}
while True: 
	print("1. Add empolyee")
	print("2. Delete employee")
	print("3. Search employee by name")
	print("4. Display all employee")
	print("5. Change a employee name in the list") 
	print("6. exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add employee
		serial_no = input("\tEnter serial No ")
		if serial_no not in employee.keys():
			name = input("\tEnter employee name: ")
			age = int(input("\tEnter employee  age: "))
			gender = input("\tEnter the employee gender: ")
			place =input("\tEnter  the employee place :")
			salary=int(input("\tEnter  the employee salary :"))
			company=input("\tEnter  the previous company name: ")
			join_date=input("\tEnter  joining date of employee :")
			temp ={
				"name":name,
				"age":age,
				"gender":gender,
				"place":place,
				"salary":salary,
				"company":company,
				"join_date":join_date,
				}
			 
			employee[serial_no] = temp
		else:
			print("\tSerial No already Taken")
	elif ch ==2 :
		serial_no = input("\tEnter serial no")
		if serial_no not in employee.keys():
                        print("\tWrong serial No")
		else:
			del employee[serial_no]
	elif ch == 3:       
		serial_no = input("\tEnter serial no")
		found = False
		for i in employee.values():
			if i["name"] == name: 
				print(f"\t{i['name']} | {i['age']} | {i['gender']} | {i['place']} | {i['salary']} | {i['company']} | {i['join_date']} ")
				found = True
				break
		if found == False :
			print("\tNot found")

	elif ch == 4:
		#Display employee 
		serial_no = input("\tEnter serial no")
		for serial,employe in employee.items():
			print(f"\t{serial} | {employe['name']} | {employe['age']} | {employe['gender']} | {employe['place']} |{employe['salary']} ")
	elif ch== 5:
		#Change a employee name in the list
		serial_no = input("\tEnter serial no.")
		if serial_no not in employee.keys():
			print("\tWrong serial no")
		else:
			employee[serial_no]['name'] = input("\tEnter new name")

	elif ch == 6:
		break;
	else:
		print("Invalid Choice")

