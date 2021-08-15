
employee = []
while True:
	
	print("1.Add employee")
	print("2.Delete employee")
	print("3.Search employee")
	print("4.Change employee data")
	print("5.Display all employee details")
	print("6.Exit")
	choice = int(input("enter your choice\n"))
	if choice == 1:
		name=input("Enter the employee name\n")
		if name != None: 
			employee.append(name)
	if choice == 2:
		print(employee)
		print("Choose the employee name to delete")
		name=input("Enter the employee name to delete\n")
		employee.remove(name)
	if choice == 3:
		name=input("Enter the name to search\n")
		if name in employee:
			print(name + "is in the list\n")
		else:
			print(name + "is not in the list\n")
	if choice == 4:
		name = input("Enter the name to be changed\n")
		index = employee.index(name)
		new_name = input("Enter the new_name\n")
		employee[index] = new_name

	if choice == 5:
		#print(employee)
		x=1
		for i in employee:
			print (str(x) + "." + i)
			x += 1
	if choice == 6: 
		break;
