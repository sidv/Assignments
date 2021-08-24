#ERP Mini Dictionary
erpdict={}
found=0
while True:
	print("Press 1 for add employee: ")
	print("Press 2 for delete employee: ")
	print("Press 3 to search employee with id: ")
	print("press 4 to search  employee with name: ")
	print("press 5 to update employee details: ")
	print("press 6 to display employee details")
	print("press 7 to exit")

	choice = input("Enter choice: ")
	if choice.isdigit():
		print("choice taken.")
	else:
		print("you entered wrong choice")
		continue
	choice= int(choice)
	if choice == 1: # Add
		empid= input("enter employee id: ")
		if empid not  in erpdict.keys():
			erpdict[empid]={}
			#erpdict[empid]["name"]=input("enter employee name: ")
			name=input("enter ee name")
			empid["name"]=name
			erpdict[empid]["age"]=input("enter employee age: ")
			erpdict[empid]["gender"]=input("enter employee gender: ")
			erpdict[empid]["place"]=input("enter employee place: ")
			erpdict[empid]["salary"]=input("enter employee salary: ")
			erpdict[empid]["previous_company"]=input("enter employee previous company :")
			erpdict[empid]["joining_date"]=input("enter employee joining date :")
			for i in erpdict: #same output as below
				print(i,erpdict[i])
			for i in erpdict.keys():
				print(i,erpdict[i])
		else:
			print("the employee id is already present")
	elif choice == 2: # delete
		for i in erpdict:
			print(i,erpdict[i])
		empid= input("enter employee id  to delete: ")
		if empid not in  erpdict.keys():
			print("Give corret emp id to delete")
		else:
			print("this ",erpdict[empid],"getting deleted")
			del erpdict[empid]
			for i in erpdict:
				print(erpdict[i])
	elif choice == 3: # search by ID
		empid=input("enter employee id to search: ")
		if empid in erpdict.keys():
			for i in erpdict.keys():
				if i==empid:
					print(erpdict[empid])
		else:
			print("the employee doesn't exists in the erpdict to search the details")
	elif choice == 4: # search by name
		empname=input("enter employee name  to search: ")
		for i in erpdict.keys():
			if erpdict[i]["name"]==empname:
				found=1
				print(erpdict[i])
		if found==0:
			print("the employee name doesn't exists in the erpdict to search the details")
	elif choice == 5: #update
		ename=input("enter the name  you want to change: ")
		flag=True
		for empid  in erpdict:
			if erpdict[empid]["name"]==ename:
				nname=input("enter the new name you want to get updated for: ")
				erpdict[empid]["name"]=nname
				flag=False
		for empid in erpdict:
			print(empid,erpdict[empid])
		if flag:
			print("enter the name correctly")
			continue
	elif choice == 6: # Display
		i=1
		if erpdict=={}:
			print("the list is empty.")
			continue
		for empid in erpdict:
			print(i,".",empid,erpdict[empid])
			i=i+1
	elif choice == 7 : # exit
		break;
	else:
		print("enter right choice")

