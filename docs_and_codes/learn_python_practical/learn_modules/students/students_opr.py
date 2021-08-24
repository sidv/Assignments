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

def display_student():
	for serial,student in students.items():
		print(f"\t{serial} | {student['name']} | {student['age']} | {student['stream']}")


def change_student_name():
	serial_no = input("\tEnter serial no.")
	if serial_no not in students.keys():
		print("\tWrong serial no")
	else:
		students[serial_no]['name'] = input("\tEnter new name")

