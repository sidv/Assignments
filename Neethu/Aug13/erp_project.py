Employee = {} #Empty dictionary

while True:
	print("1. Add employee")
	print("2. Delete employee")
	print("3. Search employee by name")
	print("4. Display all employee")
	print("5. Change a employee name in the list") 
	print("6. exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add employee
		emp_id = input("\tEnter employe id ")
		if emp_id not in Employee.keys():
			name = input("\tEnter name ")
			age = int(input("\tEnter age "))
			gender = input("\tEnter the gender ")
			place = input("\tEnter the place ")
			date = input("\tEnter the date ")
			salary = int(input("\tEnter the salary "))
			previous_company = input("\tEnter the previous company ")
			joining_date = input("\tEnter the joining date ")
			temp ={
				"name":name,
				"age":age,
				"gender":gender,
				"place":place,
				"date":date,
				"salary":salary,
				"previous_company":previous_company,
				"joining_date":joining_date
				}
			Employee[emp_id] = temp
		else:
			print("\tEmployee id already Taken")
	elif ch == 2:
		#Delete student
		emp_id = input("\tEnter emp id")
		if emp_id not in Employee.keys():
			print("\tWrong emp id")
		else:
			del Employee[emp_id]
	elif ch == 3:
		#Search employee
		name = input("\tEnter name")
		found = False
		for i in Employee.values():
			if i["name"] == name: # find name
				print(f"\t{i['name']} | {i['age']} | {i['gender']} | {i['place']} | {i['salary']} | {i['previous_company']} | {i['joining_date']} | {i['date']} ")
				found = True
				break
		
		if found == False :
			print("\tNot found")

	elif ch == 4:
		#Display Employee
		for emp_id,employee in Employee.items():
			print(f"\t{emp_id} | {Employee['name']} | {Employee['age']} | {Employee['gender']} | {Employee['date']} | {Employee['place']} | {Employee['salary']} | {Employee['previous_company']} | {Employee['joining_date']}")
	elif ch== 5:
		#Change a Employee 
		
		print("\t1.change Name")
		print("\t2. change Age")
		print("\t3.change Gender")
		print("\t4.change Salary")
		ch = input("\tEnter your choice")
		
		if ch== 1:
			
			emp_id = input("\tEnter employ id ")
			if emp_id not in Employee.keys():
				print("\tWrong employ id")
			else:
				Employee[emp_id]['name'] = input("\tEnter new name")
		if ch== 2:
			emp_id = input("\tEnter employ id ")
			if emp_id not in Employee.keys():
                                print("\tWrong employee")
			else:
                                Employee[emp_id]['age'] = input("\tEnter new age")


		if ch== 2:

                       emp_id = input("\tEnter employ id ")
                       if emp_id not in Employee.keys():
                                print("\tWrong employ id")
                       else:
                                Employee[emp_id]['gender'] = input("\tEnter new gender")


					


		if ch== 3:

                       emp_id = input("\tEnter employ id ")
                       if emp_id not in Employee.keys():
                                print("\tWrong employ id")
                       else:
                                Employee[emp_id]['salary'] = input("\tEnter new salary")

		if ch== 4:

                       emp_id = input("\tEnter employ id ")
                       if emp_id not in Employee.keys():
                                print("\tWrong employ id")
                       else:
                                Employee[emp_id]['place'] = input("\tEnter new place")


	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")


