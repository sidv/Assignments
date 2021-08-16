employee = {} #Empty dictionary

while True:
	print("1. Add employee")
	print("2. Delete employee")
	print("3. Search employee by name")
	print("4. Display all employee")
	print("5. Change employee data") 
	print("6. exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add 
		serial_no = input("\tEnter serial No ")
		if serial_no not in employee.keys():
			name = input("\tEnter name ")
			age = int(input("\tEnter age "))
			gender = input("\tEnter the gender ")
			place = input("\tEnter place ")
			salary = int(input("\tEnter salary "))
			prevcomp = input("\tEnter previous company")
			date = input("\tEnter joining date ")
			
			temp ={
				"name":name,
				"age":age,
				"gender":gender,
				"place":place,
				"salary":salary,
				"prevcomp":prevcomp,
				"joining-date":date
				}
			employee[serial_no] = temp
		else:
			print("\tSerial No already Taken")

	elif ch == 2:
		#Delete 
		serial_no = input("\tEnter serial no")
		if serial_no not in employee.keys():
			print("\tWrong serial No")
		else:
			del employee[serial_no]
	elif ch == 3:
		#Search 
		name = input("\tEnter name")
		found = False
		for i in employee.values():
			if i["name"] == name: # find name
				print(f"\t{i['name']} | {i['age']} | {i['gender']} | {i['place']} | {i['salary']} | {i['prevcomp']} | {i['joining-date']}")
				found = True
				break
		
		if found == False :
			print("\tNot found")

	elif ch == 4:
#		#Display 
		for i,j in employee.items():
			print(f"\t{i} | {j['name']} | {j['age']} | {j['gender']} | {j['place']} | {j['salary']} | {j['prevcomp']} | {j['joining-date']} ")
	elif ch== 5:
		
		serial_no = input("\tEnter serial no.")
		if serial_no not in employee.keys():
			print("\tWrong serial no")
		else:
			print("modify employee data")
			print("a,A =>change employee name \nb,B => modify gender \nc,C => modify age \nd,D => modify salary ")
			choice = input("enter option:")
			if choice == 'a' or choice =='A':
				employee[serial_no]['name'] = input("enter new name:")
			elif choice == 'b' or choice =='B':
				employee[serial_no]['gender'] = input("enter new gender:")
			elif choice == 'c' or choice =='C':
                                employee[serial_no]['age'] = input("enter new age:")
			elif choice == 'd' or choice =='D':
                                employee[serial_no]['salary'] = input("enter new salary:")



	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")
#
#
#

