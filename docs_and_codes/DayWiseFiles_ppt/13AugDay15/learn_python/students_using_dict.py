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

while True:
	print("1. Add student")
	print("2. Delete student")
	print("3. Search Student by name")
	print("4. Display all student")
	print("5. Change a student name in the list") 
	print("6. exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add student
		serial_no = input("\tEnter serial No ")
		if serial_no not in students.keys():
			name = input("\tEnter name ")
			age = int(input("\tEnter age "))
			stream = input("\tEnter the stream ")
			temp ={
				"name":name,
				"age":age,
				"stream":stream
				}
			students[serial_no] = temp
		else:
			print("\tSerial No already Taken")

	elif ch == 2:
		#Delete student
		serial_no = input("\tEnter serial no")
		if serial_no not in students.keys():
			print("\tWrong serial No")
		else:
			del students[serial_no]
	elif ch == 3:
		#Search student
		name = input("\tEnter name")
		found = False
		for i in students.values():
			if i["name"] == name: # find name
				print(f"\t{i['name']} | {i['age']} | {i['stream']} ")
				found = True
				break
		
		if found == False :
			print("\tNot found")

	elif ch == 4:
		#Display student
		for serial,student in students.items():
			print(f"\t{serial} | {student['name']} | {student['age']} | {student['stream']}")
	elif ch== 5:
		#Change a student name in the list
		serial_no = input("\tEnter serial no.")
		if serial_no not in students.keys():
			print("\tWrong serial no")
		else:
			students[serial_no]['name'] = input("\tEnter new name")


	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")



