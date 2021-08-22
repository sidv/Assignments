print("FRUIT SHOP:V3")

fruit={}
cart=[]

def add_fruit():
	fruit_id = int(input("\tEnter the Fruit ID "))
	if fruit_id not in fruit.keys():
		fruit_name = input("\tEnter name ")
		rate= int(input("\tEnter rate "))
		imported_from = input("\tEnter where it is imported from ")
		import_date = input("\tEnter the import date ")
		buying_price = int(input("\tEnter the buying price "))
		temp ={
			"fruit_name":fruit_name,
			"rate":rate,
			"imported_from":imported_from,
			"import_date":import_date,
			"buying_price":buying_price,
		}
		fruit[fruit_id] = temp
	else:
		print("\tFruit ID has already been taken")

def delete_fruit():
	a=int(input("Enter the Fruit_ID of the fruit to be deleted\n"))
	if a in fruit.keys():
		del fruit[a]
	else:
		print("Fruit doesnot exist in the shop.\n")
def search_fruit():
	name=input("Enter the fruit name you want to search\t")
	rate=input("Enter the fruit rate you want to search\t")
	flag = False
	for i in fruit.values():
		if i["fruit_name"] == name and i["rate"] == rate:
			print("Fruit exists in inventory.")
			flag = True
			break
	if(flag == False):
		print("Fruit doesnot exist in the inventory.")
def update_fruit():
	for i,j in fruit.items():
		print(f"{i} :")
		for x in j.values():
			print(f"\t{x}")
	a = int(input('Enter the fruit id : '))
	if a not in fruit.keys():
		print('Please provide right fruit id ')
	else:
		print('Update the fruit data')
		fruit[a]['fruit_name'] = input('Enter new fruit name :')
		fruit[a]['rate'] =input('Enter new rate : ')
def add_cart():
	for i,j in fruit.items():
		print(f"Enter {i} for adding {j['fruit_name']} to cart")
	select_ID=int(input('Enter fruit id to add on cart : '))
	cart.append(fruit[select_ID])
def display_fruit():
	for i,j in fruit.items():
		print(f"{i} :")
		for x in j.values():
			print(f"\t{x}")	
def display_cart():
	print("\nElements in cart:")
	y=1	
	print(" ")		
	for i in range(len(cart)):
			print(f"{y}.)")
			y+=1
			print(f"\t{cart[i]['fruit_name']} | {cart[i]['rate']}")

while True:

	choice=int(input("Enter a choice for following functions.\n1 - Add Fruit.\n2 - Delete Fruit\n3 - Update name and rate of fruit\n4 - Search Fruit info from inventory\n5 - Display all\n6 - Add to cart\n7 - Display cart\n8 - Quit\t"))
	if(choice == 1 or fruit):
		if choice == 1:
			add_fruit()
			

		elif choice == 2:
			delete_fruit()
							
		elif choice == 4:
			search_fruit()
								
		elif choice == 3:
			update_fruit()
				
		elif choice == 6:
			add_cart()
			
				
		elif choice == 5:
			display_fruit()
			
		elif choice == 7:
			display_cart()
		
		elif choice == 8:
			break
				
		else:
			print("Invalid input.\n")
			
	else:
		print("Fruit shop is empty.\n")
