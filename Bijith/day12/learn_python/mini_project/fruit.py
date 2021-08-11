fruit = [] #empty List

while True:
	print("1. Add fruit")
	print("2. Delete fruit")
	print("3. Search fruit by name and rate")
	print("4. Display all ")
	print("5. Change a fruit name and rate") 
	print("6. exit")
	ch = int(input("Enter your choice :"))
	if ch == 1:
		#Add 
		name = input("Enter fruit name: ")
		rate =int(input("enter rate:"))
		fruit.append([name,rate])
		
	elif ch == 2:
		#Delete 
		print(fruit)
		print("Choose name from this")
		name = input("Enter name to delete:")
		rate = input("enter rate to delete:")
		fruit.remove([(name,rate)])
	#elif ch == 3:
		#Search 
	#	name = input("Enter name you want to search:")
	#	if name in employee:
	#		print(name + " is in the list")
	#	else:
	#		print(name + "not in the list")
	elif ch == 4:
		print(fruit)
			
	#		for i in range(0,len(employee)):
	#			print(i+1,".",employee[i])
			

	#	else:
	#		print("No data in the list")

	#elif ch== 5:
		#Change a employee name in the list
		#Index,remove,insert
		#Index,assignment
	#	name = input("Enter the name:")
	#	index =	employee.index(name)
	#	new_name = input("Enter new name:")
	#	employee[index] = new_name
		
	#elif ch == 6:
		#Exit
	#	break;
#	else:
#		print("Invalid Choice")
