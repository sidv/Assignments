fruit = []
while True:
	print("1.Add fruit and rate")
	print("2.Delete fruit by name")
	print("3.Search fruit by name and rate")
	print("4.Change fruit name and rate")
	print("5.Display all fruits")
	print("6.Exit")
	choice = int(input("enter your choice\n"))
	if choice == 1:
		name=input("Enter the fruit name\n")
		rate=input("Enter the fruit rate\n")
		if name != None and rate != None:
			fruit.append([name,rate])
	if choice == 2:
		print(fruit)
		#print("Choose the fruit name to delete")
		name=input("Enter the fruit name to delete\n")
		for i in fruit:
			if i[0] == name:
				fruit.remove(i)
	if choice == 3:
		name=input("Enter the fruit name to search\n")
		rate=input("Enter the fruit rate to search\n")
		for i in fruit:
			if i[0] == name and i[1] == rate:
				print("Fruit is found")
			else:
			        print("Fruit not found")
	if choice == 4:
		name = input("Enter the fruit name to be changed\n")
		rate = input("Enter the fruit rate to be changed\n")
		new_name = input("Enter the new_name\n")
		new_rate = input("Enter the new_rate\n")
		for i in fruit:
			if i[0] == name and i[1] == rate:
				fruit.remove(i)
				fruit.append([new_name,new_rate])
				print(fruit)
	#	fruit[index]=new_name
	#	fruit[index1]=new_rate
	#	for i in fruit:
        #               if i[0] == name and i[1] == rate:
	#			fruit.remove(i)
	#			fruit.append([new_name,new_rate])
	#			print(fruit)

	if choice == 5:
		print(fruit)
	if choice == 6: 
		break;
