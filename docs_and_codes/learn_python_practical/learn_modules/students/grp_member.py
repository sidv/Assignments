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


