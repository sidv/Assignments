#1.Write a code to store fruit details in dictionary(fruit_name,rate,imported_from,import_date,buy_price)
#Take input from user

fruitdetails = {}
while True : 
	print("1. Add fruit details")
	print("2. display")
	print("3. Exit")
	ch = int(input("Enter the choice"))
	if ch == 1 :
		fruit_name = input("Enter fruit name")
		rate = input("Enter rate")
		imported_from = input("Enter the place")
		import_date = input("Enter the imported date")
		buy_price = input("Enter the buy price")
		fruitd = int(input("Enter fruit id"))
		fruit = {
			"fruit_name" : fruit_name,
			"rate" : rate,
			"imported_from" : imported_from,
			"import_date" : import_date,
			"buy_price" : buy_price
			}
		fruitdetails[fruitd] = fruit
	elif ch == 2 :
		print(fruitdetails)
	elif ch == 3 : 
		break
	else : 
		print("Invalid choice")


