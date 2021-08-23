fruit = {}
while True: 
	print("1. Add fruit :")
	print("2. Delete fruit_name :")
	print("3. Search fruit by name")
	print("4. Display all fruit")
	print("5. Change a fruit name in the list") 
	print("6. exit")
	ch = int(input("Enter your choice"))
	if ch == 1:
		serial_no = input("\tEnter serial No ")
		if serial_no not in fruit.keys():
			name = input("\tEnter fruit name: ")
			rate = int(input("\tEnter fruit rate: "))
			import_from= input("\tEnter the fruit import from: ")
			import_date =input("\tEnter  the fruit import date :")
			buy_price=int(input("\tEnter  the fruit price :"))
			temp ={
				"name":name,
				"rate":rate,
				"import_from":import_from,
				"import_date":import_date,
				"buy_price":buy_price,
				}
			 
			fruit[serial_no] = temp
		else:
			print("\tSerial No already Taken")
	elif ch ==2 :
		serial_no = input("\tEnter serial no")
		if serial_no not in fruit.keys():
                        print("\tWrong serial No")
		else:
			del fruit[serial_no]
	elif ch == 3:       
		serial_no =input("\tEnter serial no")
		found = False
		for i in fruit.values():
			if i['name'] == name: 
				print("\t{i['name']} | {i[rate']} | {i['import_rate']} | {i['import_date']} | {i['price']} ")
				found = True
				break
		if found == False :
			print("\tNot found")

	elif ch == 4:
		
		serial_no = input("\tEnter serial no")
		for serial,fruit in fruit.items():
			print(f"\t{serial} | {fruit['name']} | {fruit['rate']} | {fruit['import_from']} | {fruit['import_date']} |{fruit['buy_price']} ")
	elif ch== 5:
		
		serial_no = input("\tEnter serial no.")
		if serial_no not in fruit.keys():
			print("\tWrong serial no")
		else:
			fruit[serial_no]['name'] = input("\tEnter new name")

		
	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")


