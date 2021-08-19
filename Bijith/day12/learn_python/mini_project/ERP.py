employee = [] #empty List

while True:
	print("1. Add employee")
	print("2. Delete employee")
	print("3. Search employee")
	print("4. Display all employee")
	print("5. Change a employee") 
	print("6. exit")
	ch = int(input("Enter your choice :"))
	if ch == 1:
		#Add 
		name = input("Enter name: ")
		employee.append(name)
		
	elif ch == 2:
		#Delete 
		print(employee)
		print("Choose name from this")
		name = input("Enter name to delete:")
		employee.remove(name)
	elif ch == 3:
		#Search 
		name = input("Enter name you want to search:")
		if name in employee:
			print(name + " is in the list")
		else:
			print(name + "not in the list")
	elif ch == 4:
		if len(employee) !=0:
		#Display
			print(employee)
 
			
			for i in range(0,len(employee)):
				print(i+1,".",employee[i])
			

		else:
			print("No data in the list")

	elif ch== 5:
		#Change a employee name in the list
		#Index,remove,insert
		#Index,assignment
		name = input("Enter the name:")
		index =	employee.index(name)
		new_name = input("Enter new name:")
		employee[index] = new_name
		
	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")
