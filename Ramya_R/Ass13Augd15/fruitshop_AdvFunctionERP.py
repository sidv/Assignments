fruits = {} #Empty dictionary
cartitems = []

def main_menu():
	print("1. Add fruit")
	print("2. Add cart details")
	print("3. Delete fruit")
	print("4. Display all fruit")
	print("5. Display cart")
	print("6. Search fruits")
	print("7. change fruit name and rate")
	print("8. exit")

def add_fruit():
	#Add fruit
	serial_no = input("Enter serial No: ")
	name = input("Enter name: ")
	rate = int(input("Enter rate: "))
	imp_from = input("Enter place imported from: ")
	imp_date = input("Enter date when it is imported: ")
	buy_price = input("Enter buy price: ")
	temp ={
		"name":name,
		"rate":rate,
		"imp_from":imp_from,
		"imp_date":imp_date,
		"buy_price":buy_price
		}
	fruits[serial_no] = temp

def add_cart():
	#Add to cart
	#serial_no = int(input("\tEnter serial no."))
	for serial in fruits.keys():
		print(f"press {serial} for add to cart")
	cartitems.append(fruits[input('enter serial_no to add on cart : ')])
	
	print(' added Fruit in the cart ')
	#for i in fruits.keys():
	#if serial_no in fruits.keys():
	#	cartitems[serial_no] = []
				
def delete_fruit():
	#Delete fruit by serial_no
	serial_no = input("Enter serial no: ")
	if serial_no not in fruits.keys():
		print("\tWrong serial no")
	else:
		del fruits[serial_no]

def delete_fruitbyName():
	#delete fruit by name
	name = input("Enter fruit name: ")
	serial_no = input("Enter serial no: ")
	flag = False
	if serial_no in fruits.keys():
		for i in fruits.values():
			if i['name'] == name:
				flag = True
				#del fruits[serial_no]
	else:	
		print("name not found")
	if flag == True:
		del fruits[serial_no]
def display_allfruit():
	#Display all fruit
	#for serial,fruit in fruits.items():
	#	print(f"{serial} | {fruit['name']}")
	for serial,fruit in fruits.items():
		print(f"\t {fruit['name']} | {fruit['rate']} | {fruit['imp_from']} | {fruit['imp_date']}| {fruit['buy_price']}")
		
def display_cart():
	#Display cart fruits
	print(cartitems)
	
def search_fruit():
	#Search fruit
	name = input("Enter name: ")
	rate = int(input("Enter rate: "))
	found = False
	for i in fruits.values():
		if i["name"] == name and i["rate"] == rate: # find name 
			print(f"{i['name']} | {i['rate']} | {i['imp_from']} | {i['imp_date']} | {i['buy_price']}")
			print("found")
			found = True
			break
		#else:
			#print("not found")
	if found == False :
		print("\tNot found")


def search_fruit_byname():
	#Search fruit
	
	name = input("Enter name: ")
	#rate = input("Enter rate: ")
	found = False
	for i in fruits.values():
		if i["name"] == name:
			print(f"{i['name']} | {i['rate']} | {i['imp_from']} | {i['imp_date']} | {i['buy_price']}")
			print("found")
			found = True
			break
			
def change_fruit_fun():
	#Change a fruit name and rate in the list
	serial_no = input("\tEnter serial no.")
	if serial_no not in fruits.keys():
		print("\tWrong serial no")
	else:
		fruits[serial_no]['name'] = input("\tEnter new name: ")
		fruits[serial_no]['rate'] = input("\tEnter new rate: ")
		
def change_fruit():
		#Change a fruit detailes
	print("\t Enter 1 for change name")
	print("\t Enter 2 for change rate ")
	print("\t Enter 3 for change imp_from ")
	print("\t Enter 4 for change imp_date ")
	print("\t Enter 5 for change buy_price ")

	choice = int(input("\tEnter the choice which u want to change: "))
	serial_no = input("\tEnter serial no: ")
	if choice == 1:
		fruits[serial_no]['name'] = input("\tEnter new name: ")
	elif choice == 2:
		fruits[serial_no]['rate'] = input("\tEnter new rate: ")
	elif choice == 3:
		fruits[serial_no]['imp_from'] = input("\tEnter new imp_from: ")
	elif choice == 4:
		fruits[serial_no]['imp_date'] = input("\tEnter new imp_date: ")
	elif choice == 4:
		fruits[serial_no]['buy_price'] = input("\tEnter new buy_price: ")
	#else:
def cart_menu():
	print("\t 1. Add to Cart")
	print("\t 2. Display Cart")
	print("\t 3. Delete From cart")
	print("\t 4. Display Bill")
	print("\t 5. Exit")

def addto_cart():
	i = int(input("\t\tEnter the fruitid to add"))
	if i in fruits.keys():
		cartitems.append(i)
	else:
		print("\tInvalid ID")

def display_cartitems():
	#Display cart fruits
	print(cartitems)
	
def delete_from_cart():
	#display_cartitems()
	serial_no = int(input("\t\tEnter the serialno to delete from cart: "))
	for serial in fruits.keys():
		print(f"press {serial} for delete from cart")
	cartitems.remove(fruits[input('enter serial_no to delete from cart : ')])
	
	print(' delete Fruit in the cart ')
	
def print_bill():
	serial_no = int(input("\t\tEnter the serialno for bill: "))
	for serial in cartitems:
		print(cartitems)
		#print(f"{fruits['buy_price']})		

def add_to_cart():
	while True:		
		cart_menu()
		choice = int(input("\tEnter the choice: "))
		if choice == 1:
			add_cart()
		elif choice == 2:
			display_cart()
		elif choice == 3:
			delete_from_cart()
		elif choice == 4:
			print_bill()
		elif choice == 5:
			break
		#else:
			#print("\tInvalid Choice")

while True:
	main_menu()
	ch = int(input("Enter your choice: "))
	if ch == 1:
		#add fruit
		add_fruit()
	elif ch == 2:
		#Add to cart
		#add_cart()
		add_to_cart()
	elif ch == 3:
		#Delete fruit by serial_no
		#delete_fruits()
		delete_fruitbyName()
	elif ch == 4:
		#Display all fruit
		display_allfruit()
	elif ch == 5:
		#Display cart fruits
		display_cart()
	elif ch == 6:
		#Search fruit
		search_fruit()

	elif ch== 7:
		#Change a fruit name and rate in the list
		change_fruit()
	elif ch == 8:
		#Exit
		break;
	else:
		print("Invalid Choice")
