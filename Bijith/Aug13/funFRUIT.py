
cart_list = []
fruitsshop = {}


def menu():
	print("1. Add fruit")
	print("2. Delete fruit by name")
	print("3. Search fruit by name and rate")
	print("4. Change fruit name and rate")
	print("5. Add to cart")
	print("6. Display")
	print("7. Display Cart")
	print("8. Exit")


def add_fruit():
	fruitd = int(input("Enter fruit id"))
	if fruitd not in fruitsshop.keys():
		fruitsshop[fruitd]  = {
			"fruit_name" : input("Enter fruit name"),
			"rate" : input("Enter rate"),
			"imported_from" : input("Enter the place"),
			"import_date" : input("Enter the imported date"),
			"buy_price" : input("Enter the buy price")
			}
		print("Fruit Details Added")
		
def delete_by_name():
	fruitid = int(input("Enter fruit id"))
	name = input("Enter fruit name")
	flag = False
	if fruitid in fruitsshop.keys():
		for frdet in fruitsshop.values():
			if frdet["fruit_name"] == name :
				flag = True
	else:
		print("Enter valid ID")
	if flag == True:
		del fruitsshop[fruitid]

def search_menu():
	print("\t a. Search by name")
	print("\t b. Search by rate")
def search_by_name(fruitid):
	flag = False
	name = input("\tEnter the name")
	for frdet in fruitsshop.values():
		if frdet["fruit_name"] == name :
			flag = True
	if flag == True:
		print(f"\t{fruitid} : {name} is found")
	else:
		print(f"\t{name} is not found")

def search_by_rate(fruitid):
	flag = False
	rate = input("\tEnter the rate")
	for frdet in fruitsshop.values():
		if frdet["rate"] == rate :
			flag = True
	if flag == True:
		print(f"\t{fruitid} : {rate} is found")
	else:
		print(f"\t{rate} is not found")
def search_function():
	fruitid = int(input("Enter fruit id"))
	if fruitid in fruitsshop.keys():
		search_menu()
		choice = input("\tEnter the choice")
		if choice == "a":
			search_by_name(fruitid)
		elif choice == "b":
			search_by_rate(fruitid)
		else:
			print("Wrong Choice")
def update_menu():
	print("\t a. Update by name")
	print("\t b. Update rate ")

def update_by_name(fruitid):
	new_name = input("\tEnter the fruit name to be change")
	fruitsshop[fruitid]["fruit_name"] = new_name	
	
def update_by_rate(fruitid):
	new_rate = input("\tEnter the fruit rate to be change")
	fruitsshop[fruitid]["rate"] = new_rate
def update_fruit():
	fruitid = int(input("Enter fruit id"))
	if fruitid in fruitsshop.keys():
		update_menu()
		choice = input("\tEnter the choice")	
		if choice == "a":
			update_by_name(fruitid)
		elif choice == "b":
			update_by_rate(fruitid)
		else:
			print("Wrong Choice")
	else:
		print("ID is not present")
			
def cart_menu():
	print("\t a. Add to Cart")
	print("\t b. Display Cart")

def display_cart():
	for i in cart_list:
		print(f"{i} : {fruitsshop[i]}\n")

def display():
	for fid,values in fruitsshop.items():
		print(f"{fid} : {values}\n")

def addtocart_function():
	num = int(input("\tEnter the fruitid to add"))
	if num in fruitsshop.keys():
		cart_list.append(num)
	else:
		print("\tInvalid ID")
def add_to_cart():
	for fid,values in fruitsshop.items():
		print(f"{fid} : {values}\n")
		cart_menu()
		choice = input("\tEnter the choice")
		if choice == "a":
			addtocart_function()
		elif choice == "b":
			display_cart()
		else:
			print("\tInvalid Choice")
while True :
	menu()
	ch = int(input("Enter the choice "))
	if ch == 1 :
		print("Add fruit")
		add_fruit()
	elif ch == 2 :
		print("Delete fruit by name")
		delete_by_name()
	elif ch == 3:
		print("Search fruit by name and rate")
		search_function()
	elif ch == 4:
		print("Change fruit name and rate")
		update_fruit()
	elif ch == 5:
		print("Add to cart Function")
		add_to_cart()
	elif ch == 6:
		print("Display")
		display()
	elif ch == 7:
		print("Display Cart")
		display_cart()
	elif ch == 8:
		print("Exit")
		break
	else:
		print("Invalid choice")
	
