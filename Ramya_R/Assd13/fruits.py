fruits = [] #empty List
rate = []

while True:
	print("1. Add fruit")
	print("2. Delete fruit")
	print("3. Search fruit")
	print("4. Display all fruit")
	print("5. Change a fruit name in the list") 
	print("6. exit")
	ch = int(input("Enter your choice: "))
	if ch == 1:
		#Add fruit
		name = input("Enter name: ")
		cost = input("Enter Rate: ")
		fruits.append(name)
		rate.append(cost)
		
	elif ch == 2:
		#Delete fruit
		print(fruits)
		print("Choose name from this: ")
		name = input("Enter name to delete: ")
		#cost = input("Enter cost to delete: ")
		if name in fruits :
			#if i[0] == name:
				fruits.remove(name)
			#rate.remove(cost)
	elif ch == 3:
		#Search fruit
		name = input("Enter name you want to search: ")
		cost = input("Enter cost you want to search: ")	
		if name in fruits or cost in rate:
			print(name + " is in the list")
		else:
			print(name + "not in the list")
	elif ch == 4:
		#Display fruit
		print(list(zip(fruits,rate)))
		#print(fruits)
	elif ch== 5:
		#Change a fruit name in the list
		#Index,remove,insert
		#Index,assignment
		name = input("Enter the name: ")
		index =	fruits.index(name)
		new_name = input("Enter new name: ")
		fruits[index] = new_name
		cost = input("Enter the cost: ")
		index = rate.index(cost)
		new_cost = input("Enter new cost: ")
		rate[index] = new_cost
		#fruits[fruits.index(name)] = input("Enter new name")
	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")
