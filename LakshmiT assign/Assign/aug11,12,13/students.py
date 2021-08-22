
students = [] #empty List

while True:
	print("1. Add student")
	print("2. Delete student")
	print("3. Search Student")
	print("4. Display all student")
	print("5. Change a student name in the list") 
	print("6. exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add student
		name = input("Enter name")
		students.append(name)
		#students.append(input("Enter name"))
	elif ch == 2:
		#Delete student
		print(students)
		print("Choose name from this:")
		name = input("Enter name to delete")
		students.remove(name)
	elif ch == 3:
		#Search student
		name = input("Enter name you want to search")
		if name in students:
			print(name + " is in the list")
		else:
			print(name + "not in the list")
	elif ch == 4:
		#Display student
		print(students)
	elif ch== 5:
		#Change a student name in the list
		#Index,remove,insert
		#Index,assignment
		name = input("Enter the name")
		index =	students.index(name)
		new_name = input("Enter new name")
		students[index] = new_name
		#students[students.index(name)] = input("Enter new name")
	elif ch == 6:
		#Exit
