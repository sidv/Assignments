
def add_fruit():
    fid = int(input("Enter the ID number "))
    if fid not in fruit.keys():
        name = input("Enter Fruit name ")
        rate = input("Enter Fruit rate ")
        import_from = input("Imported from : ")
        import_date = input("Imported date : ")
        price = input("Buy price : ")
        temp = {
            "name":name,
            "rate":rate,
            "import_from":import_from,
            "import_date":import_date,
            "price":price
        }
        fruit[fid] = temp
    else:
        print("Fruit ID is already taken")

def delete_fruit():
    fname = input("Enter fruit name ")
    for id,item in (fruit.copy()).items():  # list[dict] can be used too
        if item["name"] == fname:
            del fruit[id]


def search_name():
    name = input("Enter the fruit name ")
    found = False
    for item in fruit.values():
        if(item['name'] == name):
            found = True
            print(item," is where the name exists")
            break
    if(found == False):
        print("not found")

def search_rate():
    rate = input("Enter the rate")
    found = False
    for item in fruit.values():
        if(item['rate'] == rate):
            found = True
            print(item," is where the value exists")
            break
    if(found == False):
        print("not found")


def change_name():
    newname = input("Enter new name")
    fruit[fruit_id]['name'] = newname

def change_rate():
    newrate = input("Enter new rate")
    fruit[fruit_id]['rate'] = newrate

def display_fruit():
    print(fruit)

def add_to_cart():
    count = 1
    for item in fruit:
        print(count,"." ,item)
        count+=1
    id = int(input("Enter fruit id"))
    cart.append(fruit[id])

def display_cart():
    print(cart)


fruit = {}
cart = []
while True:
    print("\nPress 1 for Add fruit ")
    print("Press 2 for Delete fruit  ")
    print("Press 3 for Search fruit by name and rate  ")
    print("Press 4 for Change fruit name and rate  ")
    print("Press 5 for Display  ")
    print("Press 6 for Add to cart")
    print("Press 7 to display cart")
    print("Press 8 for exit  ")

    ch = int(input())
	if(ch == 1):
		add_fruit()
	elif (ch == 2):
		delete_fruit()
	elif(ch == 3):
		print("Press 1 for search by name ")
		print("Press 2 for search by rate ")
		choice = int(input())
	        if (choice == 1):
	            search_name()
	        elif (choice == 2):
	            search_rate()
	        else:
	            print("invalid choice")
	elif(ch == 4):
		fruit_id = int(input("Enter id"))
		if fruit_id not in fruit.keys():
			print("invalid id")
		else:
			print("Press 1 for change name")
			print("Press 2 for change rate")

		choice = int(input("Enter choice"))
		if(choice == 1):
	                change_name()
		elif (cho == 2):
			change_rate()
                
	elif(ch == 5):
      		display_fruit()
	elif(ch == 6):
      		add_to_cart()
	elif(ch == 7):
     		display_cart()
	elif (ch == 8):
      		break
	else:
			        print("invalid choice")


