print("ERP system")

emp = []
while True:
	print("1.-Add Employee ")
	print("2.-Delete Employee")
	print("3.-Search Employee")
	print("4.-Change Employee Data")
	print("5.-Display")
	print("6.exit")
	ch = int(input("Enter your choice"))
	if ch is None:
		print("please provide a value here")
	elif ch ==1 :
		emp.append(input("Enter the employee name :" ))
	elif ch == 2:
		emp.remove(input("Enter employee name to delete"))
	elif ch == 3:
		name = input("Enter a name for search")
		if name in emp:
			print(f'{name} found inside the list')
		else:
			print(f'{name} not found')
	elif ch ==4:
		name = input('Enter previous employee name : ')
		index = emp.index(name)
		emp[index] = input('Enter new employee name')
	elif ch == 5:
		print('Printing all employee information')
		
		for i in range(0,len(emp)):
			print(f'{i+1}.{emp[i-1]}')
	elif ch ==6:
		break
	else:
		print(" nothing to show ")
