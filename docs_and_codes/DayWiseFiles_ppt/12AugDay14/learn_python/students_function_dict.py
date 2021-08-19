#name,age,stream,address,serial_no
#{name:siddhant,age:20,stream: CS}
#{1:{
#	name:"Siddhant"
#	age:20
#	....
#	}
#2:{
#	name:"Sid"
#	age:30
#	....
#	}
# 3:{
#	name:"Pavan"
#	age:34
#	...
#	}
#}

#[{},{},{}]
#  0  1  2
# \t ->Tab space
# \n -> newline
# \\ -> Print \
# \' -> print '
# \" -> print "

students = {} #Empty dictionary

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
	print("6. exit")

while True:
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
		#Exit
		break;
	else:
		print("Invalid Choice")



