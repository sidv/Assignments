import grp_member as grpm

def manage_all_group_menu():
	print("\t1.Create Group")
	print("\t2.Display Groups")
	print("\t3.Manage Group(Particular)")
	print("\t4.Delete Group")
	print("\t5.Exit")

def create_group():
	group_name = input("\tEnter group name ")
	groups[group_name] = []

def delete_group():
	group_name = input("\tEnter group name ")
	if group_name in groups.keys():
		del groups[group_name]
		print("\tDeleted the group")
	else:
		print("\tWrong group name")

def display_groups():
	for key,value in groups.items(): #key is group_name,value is list of student serial no
		name_string = ""
		for i in value:
			name_string = name_string +"|"+students[i]["name"]
		print(f"{key} => {name_string}")

def manage_group_menu():
	print("\t\t1.Add Member")
	print("\t\t2.Delete Member")
	print("\t\t3.List Members")
#	print("\t\t4.Exit")
	

def manage_group():
	group_name = input("\t\tEnter group name ")
	manage_group_menu()
	ch = int(input("\t\t Enter your Choice "))
	if ch == 1:
		#Add member
		grpm.add_member(group_name)
	elif ch == 2:
		#Delete member
		grpm.delete_member(group_name)
	elif ch == 3:
		#List member
		grpm.list_member(group_name)
	else:
		print("\tInvalid choice")	
	

def manage_all_groups():
	while True:
		manage_all_group_menu()
		ch = int(input("\tEnter your choice "))
		if ch == 1:
			#Create group
			create_group()
		elif ch == 2:
			#display groups
			display_groups()
		elif ch == 3:
			#Manage group(Particular)
			manage_group()
		elif ch == 4:
			#Delete Group
			delete_group()
		elif ch == 5:
			#exit
			break
		else:
			print("\tInvalid choice")	

