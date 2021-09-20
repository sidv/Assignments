print("ERP System")

Emp=[]

while True:

	choice=int(input("Enter a choice for following functions.\n1 - add Employee.\n2 - Delete Employee\n3 - Search Employee\n4 - Change Employee Data\n5 - Display all\n"))
	if(choice == 1 or Emp):
		if choice == 1:
			a=input("Add a new employee\n")
			Emp.append(a)
		elif choice == 2:
			a=input("Enter the name of the employee to be deleted\n")
			Emp.remove(a)
		elif choice == 3:
			a=input("Enter the name of the Employee you are searching for\n")
			if a in Emp:
				print("Yes "+a+" does belong to the ERP system\n")
			else:
				print("No doesnt exist\n")
		elif choice == 4:
			a=input("Enter the name of the Employee you are looking to change\n")
			Emp[(Emp.index(a))]=input("Please enter the new name\n")
		elif choice == 5:
			for i in Emp:
				print(str((Emp.index(i)+1))+"."+i)
		else:
			print("Invalid input\n")
	else:
		print("ERP is empty.\n")
