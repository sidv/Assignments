fruitsshop = [] 
while True : 
	print("1. Add fruit")
	print("2. Delete fruit")
	print("3. Search fruit")
	print("4. Change fruit data")
	print("5. Display")
	print("6. Exit")
	ch = int(input("Enter the choice"))
	if ch ==1:
		name = input("Enter fruit name")
		rate = int(input("Enter the rate"))
		fruitsshop.append([name,rate])
	elif  ch == 2:
		name = input("Enter fruit name")
		for i in range(0,len(fruitsshop)):
			print(fruitsshop[i][0])
			if(fruitsshop[i][0] == name):
				fruitsshop.pop(i)
				break
	elif ch == 3:
		name = input("Enter fruit name")
		rate = int(input("Enter the rate"))
		for i in range(0,len(fruitsshop)):
			if(fruitsshop[i][0] == name and fruitsshop[i][1] == rate):
				print(name ," is found")
				break
	elif ch == 4:
		name = input("Enter the fruit name")
		rate = int(input("Enter the rate"))
		new_name = input("Enter the fruit name to be change")
		new_rate = int(input("Enter the fruit rate to be change"))
		
		for i in range(0,len(fruitsshop)):
			if(fruitsshop[i][0] == name and fruitsshop[i][1] == rate):
				print("Entered")
				fruitsshop[i] = [new_name,new_rate]
				break
	elif ch == 5:
		print(fruitsshop)
		
	elif ch == 6:
		print("Exit")
		break
	else:
		print("Invalid choice")
	
