fruits = {} #Empty dictionary

while True:
	print("1. Add fruit")
	print("2. Delete fruit")
	print("3. Display all fruit")
	print("4. Search fruits")
	print("5. exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
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

	elif ch == 2:
		#Delete fruit by serial_no
		serial_no = input("Enter serial no: ")
		del fruits[serial_no]

	elif ch == 3:
		#Display fruit
		for serial,fruit in fruits.items():
			print(f"{serial} | {fruit['name']}")

	elif ch == 4:
		#Search fruit
		name = input("Enter name")
		for i in fruits.values():
			if i["name"] == name: # find name
				print(f"{i['name']} | {i['rate']} | {i['imp_from']} | {i['imp_date']} | {i['buy_price']}")

	elif ch == 5:
		#Exit
		break;
	else:
		print("Invalid Choice")
