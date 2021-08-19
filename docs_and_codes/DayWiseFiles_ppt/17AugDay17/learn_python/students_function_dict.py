students = {} #Empty dictionary
groups = {} #empty dictionary
school = {}
def add_student():
	serial_no = input("\tEnter serial No ")
	if serial_no not in students.keys():
		students[serial_no] ={
			"name":input("\tEnter name "),
			"age":int(input("\tEnter age ")),
			"stream":input("\tEnter the stream ")
		}
	else:
		print("\tSerial No already Taken")



def delete_student():
	serial_no = input("\tEnter serial no")
	if serial_no not in students.keys():
		print("\tWrong serial No")
	else:
		del students[serial_no]
def search_student_menu():
	print("\t1.Search by name")
	print("\t2.Search by age")
	print("\t3.Search by stream")
	print("\t4.exit")

def search_st_by_name():
	name = input("\t\tEnter name ")	
	found = False
	for i in students.values():
		if i["name"] == name: # find name
			print(f"\t\t{i['name']} | {i['age']} | {i['stream']} ")
			found = True
			break
	if found == False :
		print("\t\tNot found")

def search_st_by_age():
	age = int(input("\t\tEnter age"))
	for i in students.values():
		if i["age"] == age: # find name
			print(f"\t\t{i['name']} | {i['age']} | {i['stream']} ")
			found = True
	if found == False :
		print("\t\tNot found")
	
def search_st_by_stream():
	stream = input("\t\tEnter stream")
	for i in students.values():
		if i["stream"] == stream: # find name
			print(f"\t\t{i['name']} | {i['age']} | {i['stream']} ")
			found = True
	if found == False :
		print("\t\tNot found")


def search_student():
		
	while True:
		search_student_menu()
		ch = int(input("\tEnter your choice"))
		if ch == 1:
			#Search by name
			search_st_by_name()
		elif ch == 2:
			#Search by age
			search_st_by_age()
		elif ch == 3:
			#serach by stream
			search_st_by_stream()
		elif ch == 4:
			#exit
			break
		else:
			print("Invalid choice")	

def display_student():
	for serial,student in students.items():
		print(f"\t{serial} | {student['name']} | {student['age']} | {student['stream']}")


def change_student_name():
	serial_no = input("\tEnter serial no.")
	if serial_no not in students.keys():
		print("\tWrong serial no")
	else:
		students[serial_no]['name'] = input("\tEnter new name")

def main_menu():
	print("1. Add student")
	print("2. Delete student")
	print("3. Search Student")
	print("4. Display all student")
	print("5. Change a student name in the list") 
	print("6. Manage All groups")
	print("7. exit")

def manage_all_group_menu():
	print("\t1.Create Group")
	print("\t2.Display Groups")
	print("\t3.Manage Group(Particular)")
	print("\t4.Delete Group")
	print("\t5.Exit")

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
		add_member(group_name)
	elif ch == 2:
		#Delete member
		delete_member(group_name)
	elif ch == 3:
		#List member
		list_member(group_name)
	else:
		print("\tInvalid choice")	
	
def add_member(group_name):
	display_student()
	serial_no = input("\t\tEnter the serial no of student ")
	if serial_no in students.keys():
		groups[group_name].append(serial_no)
	else:
		print("\t\tWrong serial No.")

def list_member(group_name):
	name_string=""
	for i in groups[group_name]:
		name_string = name_string +"|"+i+"."+students[i]["name"]
	print(f"{name_string}")

def delete_member(group_name):
	list_member(group_name)
	serial_no = input("\t\tEnter serial no from list")
	if serial_no in groups[group_name]:
		groups[group_name].remove(serial_no)
	else:
		print("\t\tWrong serial No.")

	
def add_school():
	school["name"] = input("Enter school")
	school["email"] = input("Enter email")


while True:
	add_school()
	main_menu()
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add student
		add_student()
	elif ch == 2:
		#Delete student
		delete_student()
	elif ch == 3:
		#Search student
		search_student()
	elif ch == 4:
		#Display student
		display_student()
	elif ch== 5:
		#Change a student name in the list
		change_student_name()
	elif ch == 6:
		#Manage team
		manage_all_groups()
	elif ch == 7:
		#Exit
		break;
	else:
		print("Invalid Choice")




"""
{"1":{student}, "2":{student}, "3":{student}, "4":{student}, "5":{student}}
teams={}

Storage:
{
	agri:["1","5"],
	rocket:["3","5"]
}

Fetch:
x = teams[agri]
students[x[0]]

Manage Groups:
	-Create group
	-Display groups
	-Manage group(Particular)
	-Delete group
"""




























