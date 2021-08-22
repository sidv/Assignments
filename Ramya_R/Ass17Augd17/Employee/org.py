#employees = {} #empty List
organization = {}
def org_menu():
	print("\t1.Add organization")
	print("\t2.view organization")
	print("\t3.edit organization")
	print("\t4.delete organization")
	#print("\t5.exit")
	
	
def manage_all_organizations():
	org_menu()
	ch = int(input("\tEnter your choice "))
	if ch == 1:
		#Create organization
		add_org()
	elif ch == 2:
		#display organization
		display_org()
	elif ch == 3:
		#edit organization details
		edit_org()
	elif ch == 4:
		#Delete organization
		delete_org()
	#elif ch == 5:
		#exit
		#break
	else:
		print("\tInvalid choice")
	
		
def add_org():
	org_id = input("Enter org id: ")
	
	organization[org_id] ={
		"name":input("\tEnter name "),
		"email":input("\tEnter email "),
		"phno":input("\tEnter the phno "),
		"address":input("\tEnter address ")
	}
#	else:
#		print("\tid already Taken")

def edit_org():
	#Change a employee detailes
	print("\t Enter 1 for change name")
	print("\t Enter 2 for change email ")
	print("\t Enter 3 for change phno ")
	print("\t Enter 4 for change address ")

	choice = int(input("\tEnter the choice which u want to change: "))
	org_id = input("\tEnter org id: ")
	if choice == 1:
		organization[org_id]['name'] = input("\tEnter new name: ")
	if choice == 2:
		organization[org_id]['email'] = input("\tEnter new email: ")
	if choice == 3:
		organization[org_id]['phno'] = input("\tEnter new phno: ")
	if choice == 4:
		organization[org_id]['address'] = input("\tEnter new Address: ")
	#else:
		#print("\t invalid choice")

def display_org():
	#Display organization
	print(organization)
	for org_id,i in organization.items():
		print(f"\t{org_id} | {i['name']} | {i['email']} | {i['phno']} | {i['address']}")
def delete_org():
	org_id = input("\tEnter org id: ")
	if org_id not in organization.keys():
		print("\tWrong serial No")
	else:	
		del organization[org_id]
