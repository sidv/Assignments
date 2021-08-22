print("ERP System")
print("------------")

emp = []
while True:
	print("1.Add Employee")
	print("2.Delete Employee")
	print("3.Search Employee")
	print("4.Change Employee Data")
	print("5.Display Employee")
	print("6.Exit")

	ch = int(input("Enter your choice : "))
	if ch == 1:
		#Add Employee
		name = input("Enter name : ")
		emp.append(name)
	elif ch == 2:
		#Delete Employee
		print(emp)
		print("Choose name of employee for deletion : ")
		name = input("Enter name to delete : ")
		emp.remove(name)
	elif ch == 3:
		#Search Employee
		name = input("Enter name you want to search : ")
		if name in emp:
			print(name + " is in the list")
		else:
			print(name + "not in the list")

	elif ch == 4:
                #Change a Employee name in the list
                name = input("Enter the name : ")
                index = emp.index(name)
                new_name = input("Enter new name : ")
                emp[index] = new_name

	elif ch == 5:
		if len(emp) != 0:
			#Display Employee
			for i in range(0,len(emp)):
				print(i+1,".",emp[i])

		else:
			print("List is empty")
	elif ch == 6:
		break
