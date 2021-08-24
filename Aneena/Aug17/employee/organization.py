org={}

def add_oganization():
	org['name']=input("Enter organization name")
	org['email']=input("Enter organization  email")

def display_organization():
	print(org)
def edit_oganization():
	print("1.Edit Organization name ")
	print("2.Edit Organization email")
	choice = int(input("Enter choice: "))
	if choice == 1:
		org['name'] = input("Enter new organization name")
	elif choice == 2:
		org['email'] = input("Enter new organization email")	
	else:
		print("Invalid choice")
def org_details():
	print("1.Add Organization")
	print("2.Edit Organization")
	print("3.Display Organization details")
	print("4.Exit")
	while True:
		choice = int(input("Enter choice : "))
		if choice == 1:
			add_oganization()
		elif choice == 2:
			edit_oganization()
		elif choice == 3:
			display_organization()
		elif choice == 4:
			break
		else:
			print("Invalid choice")	


