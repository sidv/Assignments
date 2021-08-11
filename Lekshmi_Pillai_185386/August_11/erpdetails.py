employee = [] 
while True : 
	print("1. Add Employee")
	print("2. Delete Employee")
	print("3. Search Employee")
	print("4. Change employee data")
	print("5. Display")
	print("6. Exit")
	ch = int(input("Enter the choice"))
	if ch is None:
		print("Enter valid choice ")
	elif ch == 1:
		name = input("Enter the employee name")
		employee.append(name)
	elif ch == 2:
		name = input("Enter the employee name")
		employee.remove(name)
	elif ch == 3:
		name = input("Enter the name to be search")
		if name in employee:
			print(name," is in list")
		else:
			print(name," not in list")
	elif ch == 4:
		index = employee.index(input("Enter the name to be change"))
		employee[index] = input("Enter the new name")
	elif ch == 5:
		print(employee)
		for i in range(0,len(employee)):
			print(i+1,":",employee[i])
	elif ch == 6:
		break
	else:
		print("Invalid choice")
	
	
	
