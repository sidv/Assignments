print("FRUIT SHOP")
print("-----------")

fruit = []

while True:
	print("1. Add Fruit")
	print("2. Delete Fruit by name")
	print("3. Search Fruit by name and rate")
	print("4. Change Fruit name and rate")
	print("5. Display Fruits list") 
	print("6. exit")

	ch = int(input("Enter your choice : "))

	if ch == 1:
		f = input("Enter the fruit name : ")
		r = int(input("Enter the rate : "))
		fruit.append([f,r])
		print(fruit)

	elif ch == 2:
		#Delete  fruit
		sub = []
		print(fruit)
		print("Choose name from this:")
		name = input("Enter fruit name to delete : ")
		rate = int(input("Enter the rate : "))
		sub.append(name)
		sub.append(rate)
		for i in fruit :
			if i == sub:
				fruit.remove(i) 

	elif ch == 3:
		#Search fruit
		sub = []
		name = input("Enter name of fruit you want to search : ")
		rate = int(input("Enter the rate you want to search : "))
		sub.append(name)
		sub.append(rate)
		for i in fruit:
			if i == sub:
				print(name + "," + rate, " is in the list")
			else:
				print(name + "," + rate, "is not in the list")

	elif ch == 4:
		#Change a fruit and rate in the list
		sub = []
		name = input("Enter the fruit name : ")
		rate = int(input("Enter the rate : "))
		sub.append(name)
		sub.append(rate)
		index =	fruit.index(sub)
		new_name = input("Enter new fruit name : ")
		new_rate = int(input("Enter the new rate : "))
		sub1 = []
		sub1.append(new_name)
		sub1.append(new_rate)
		fruit[index] = sub1
		print(fruit)
		
	elif ch == 5:
		#Display fruits
		if len(fruit) != 0:
			for i in range(0,len(fruit)):
				print(i+1,".",fruit[i][0],fruit[i][1])
		else:
			print("Item not in the list")
	elif ch == 6:
		#Exit
		break;
		
	else:
		break
