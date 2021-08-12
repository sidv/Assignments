
fruit={}
cart=[]
while True:
	print("Press 1 for add fruit details")
	print("Press 2 for delete employee ")
	print("Press 3 for change name and rate of fruit")
	print("Press 4 for search  fruit details")
	print("Press 5 for display fruit details")
	print("Press 6 for Add to cart")
	print("Press 7 for Display cart")
	print("Press 8 for Quit")
	ch = int(input("Enter choice"))

	if ch == 1:
		fruit_id = input("\tEnter Fruit_id ")
		if fruit_id not in fruit.keys():
			fruit_name = input("\tEnter name ")
			rate= int(input("\tEnter rate "))
			imported_from = input("\tEnter the imported from ")
			import_date = input("\tEnter import_date ")
			buying_price = int(input("\tEnter buying_price "))
			temp ={
				"fruit_name":fruit_name,
				"rate":rate,
				"imported_from":imported_from,
				"import_date":import_date,
				"buying_price":buying_price
            }
            
            fruit

            

        else:
            print("\tEmployee id  already Taken")
    
    elif choice == 2:
        fid = input("\tEnter fruit id") 
		if fid not in fruit.keys():
			print("\tWrong fruit id")
		else:
			del fruit[fid]
	elif choice == 3:
		fr_id=int(input("enter the fruit_id you want to change:"))
		
        # you need to change for loop to if
		# for fr_id in fruit.keys():
        if fr_id not in fruit.keys():
            print("Wrong fruit name and fruit rate")
		else:
            name=input("Enter the fruit name you want to change")
		    rate=int(input("Enter the rate you want to change"))

			if fruit[fr_id]["fruit_name"] == name and fruit[fr_id]["rate"] == rate :
			   fruit[fr_id]["fruit_name"]=input("Enter new fruit name")
			   fruit[fr_id]["rate"]=int(input("Enter new rate"))
			# print(fruit)
	elif choice == 4:
		name=input("enter the fruit name you want to search")
		rate=input("enter the fruit rate you want to search")
		found = False
		for i in fruit.values():
			if i["fruit_name"] == name and i["rate"] == rate:
				print("We found!!")
				found = True
				break
		if(found == False):
				print("Not Found!!!!")
	elif choice == 5: 
                print(fruit)
	elif choice == 6:
		for i in fruit.keys():
			print(f"press {i} for add to cart")
		print("cart")
		cart.append(fruit[int(input("enter your choice"))])
	elif choice == 8:
        break
	elif choice == 7:
		print(cart)
	else:
		print("Invalid choice")
