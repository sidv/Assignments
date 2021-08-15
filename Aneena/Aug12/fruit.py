fruit = {}
cart=[]
while True:

	print("1.Add fruit details")
	print("2.Delete fruit by name")
	print("3.Search fruit by name and rate")
	print("4.Change fruit name and rate")
	print("5.Add to cart")
	#(List the fruits with fruit_id->select id->store in cart list)
	print("6.Display all fruits")
	print("7.Display the cart")
	print("8.Exit")
	choice = int(input("enter your choice\n"))
	if choice == 1:
		#add
		fruit_id =int(input("Enter fruit_id\n"))
		if fruit_id not in fruit.keys():
			fruit_name=(input("enter fruit_name\n"))
			imported_from=input("enter imported_from\n")
			import_date=input("Enter import_date\n")
			buy_price=int(input("buy_price\n"))
			temp = {
				"fruit_name" : fruit_name,
				"imported_from" : imported_from,
				"import_date" : import_date,
				"buy_price" : buy_price
				}
			fruit[fruit_id] = temp	
	elif choice == 2:
		#delete
		fruit_id = int(input("Enter fruit id"))
		if fruit_id not in fruit.keys():
			print("Wrong fruit id")
		else:
			del fruit[fruit_id]
	
	elif choice == 3:
		#search
		fruit_name = input("Enter fruit name to search")
		fruit_rate = int(input("Enter fruit rate to search"))
		found = False
		for i in fruit.values():
			if i["fruit_name"] == fruit_name and i["fruit_rate"] == fruit_rate:
				print("Found")
				found = True
				break
		if found == False :
			print("Not found")
	
	elif choice == 4:
		#change
		print(fruit)
		fruit_id = int(input("Enter fruit id : "))
		if fruit_id not in fruit.keys():
			print("Given fruitid not found")
		else:
			print("Change fruit name and rate")
			fruit[fruit_id]['fruit_name'] = input("Enter new fruit name ")
			fruit[fruit_id]['rate'] =input("Enter new rate ")
	
	elif choice == 5:
		#Add to cart
		for i in fruit.keys():
			print(f"press {i} for add to cart")
			cart.append(fruit[int(input("enter fruit id to add on cart : "))])

	elif choice == 6:
		#Display fruits
		print(fruit)
	elif choice == 7:
		#Display cart
		print(cart)
	elif choice == 8:
		break;
	else:
		print("Invalid choice")
