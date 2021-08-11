employees = [] #empty List

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
		name = input("Enter name: ")
		employees.append(name)
		#in one line
		#employees.append(input("Enter name: "))
	elif ch == 2:
		#Delete employee
		print(employees)
		print("Choose name from this: ")
		name = input("Enter name to delete: ")
		employees.remove(name)
	elif ch == 3:
		#Search employee
		name = input("Enter name you want to search: ")
		if name in employees:
			print(name + " is in the list")
		else:
			print(name + " not in the list")
	elif ch == 4:
		#Display employee
		#print("---['r','t']---like output")
		#print(employees)
			
		for i in range(0,len(employees)):
			print(i+1,".",employees[i])
		i+=1
	elif ch== 5:
		#Change a employee name in the list
		name = input("Enter the name: ")
		index =	employees.index(name)
		new_name = input("Enter new name: ")
		employees[index] = new_name
		#employees[employees.index(name)] = input("Enter new name: ")
	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")
