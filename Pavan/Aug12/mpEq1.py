print("ERP System")

Emp={}

while True:

	choice=int(input("Enter a choice for following functions.\n1 - add Employee.\n2 - Delete Employee\n3 - Search Employee\n4 - Change Employee Data\n5 - Display all\n"))
	if(choice == 1 or Emp):
		if choice == 1:
			Emp_List=[]
			EmpID=int(input("Enter the employee ID\n"))
			if EmpID in Emp.keys():
				print("Already exists.\n")
			else:
				
				name=input("Add name of the new employee\n")
				Emp_List.append(name)
				age=input("Add age of the new employee\n")
				Emp_List.append(age)
				gender=input("Add a gender of new employee\n")
				Emp_List.append(gender)
				salary=int(input("Add the new employee salary.\n"))
				Emp_List.append(salary)
				pv_co=input("Add the previous company of the  new employee\n")
				Emp_List.append(pv_co)
				doj=input("Add the new employee date of joining in dd/mm/yyyy format.\n")
				Emp_List.append(doj)
				Emp[EmpID]=Emp_List

		elif choice == 2:
			a=int(input("Enter the EmpID of the employee to be deleted\n"))
			if a in Emp.keys():
				del Emp[a]
			else:
				print("Employee doesnot exist.\n")
		elif choice == 3:
			a=input("Enter the EmpID of the Employee you are searching for\n")
			b=Emp.values()
			
			for i in b:
				if a in i[0]:
					print("Yes "+a+" does belong to the ERP system\n")
				else:
					print("No doesnt exist\n")
		elif choice == 4:
			a=int(input("Enter the EmpID you want to update.\n"))
			if a in Emp.keys():
				Emp[a][0]=input("Enter the name.\n")
				Emp[a][1]=input("Enter the age.\n")
				Emp[a][2]=input("Enter the gender.\n")
				Emp[a][3]=int(input("Enter the new salary\n"))
		elif choice == 5:
			for i,j in Emp.items():
				print(f"{i} :")
				for x in j:
					print(f"\t{x} ")
		else:
			print("Invalid Input\n")
	else:
		print("ERP is empty.\n")
