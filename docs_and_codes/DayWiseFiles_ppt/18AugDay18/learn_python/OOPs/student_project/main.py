from student import Student #If you are importing the class here directly you dont need to write the modulename.classname
#from modulename import classname/function/variable
students = []

def main_menu():
	print("1. Add student")
	print("2. Delete student")
	print("3. Search Student")
	print("4. Display all student")
	print("5. Change a student name in the list") 
	print("6. Manage All groups")
	print("7. exit")


while True:
	main_menu()
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add student
		st_id = input("\tEnter student id : ")
		name = input("\tEnter name : ")
		age = input("\tEnter student age : ")
		grade = input("\tEnter grade : ")

		st_temp = Student(st_id,name,age,grade)
		students.append(st_temp)

	elif ch == 2:
		#Delete student
		pass
	elif ch == 3:
		#Search student
		name = input("Enter name :")
		st = list(filter(lambda a: a.name == name , students))
		if len(st) == 0: #not st #st
			print("No student found")
		else:
			for i in st:
				print(f"{i.name}")
		#grade = input("Enter grade :")
		#st = list(filter(lambda a: a.grade == grade ,students))
		#for i in st:
		#	print(f"{i.name}")
	elif ch == 4:
		#Display student
		for i in students:
			print(f"{i.name} | {i.age} | {i.grade} ")
	elif ch== 5:
		#Change a student name in the list
		st_id = input("Enter Student id: ")
		st_temp  = list(filter(lambda a: a.st_id == st_id,students))
		st_temp[0].set_name(input("Enter new name: "))

	elif ch == 6:
		#Manage team
		pass
	elif ch == 7:
		#Exit
		break;
	else:
		print("Invalid Choice")

























