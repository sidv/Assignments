print("FRUIT SHOP\n")

item=[]

while True:
	choice=int(input("Enter a choice for following functions.\n1 - add Fruit.\n2 - Delete Fruit\n3 - Search Fruit name and rate\n4 - Change Fruit name and rate\n5 - Display all\n"))
	if(choice == 1 or item):
		if choice == 1:
        		fr=[]
        		a=input("Add a new fruit\n")
        		fr.append(a)
        		b=int(input("Add a new fruit rate\n"))
        		fr.append(b)
        		item.append(fr)
		elif choice == 2:
			a=input("Enter the name of the Fruit to be deleted\n")
			for i in item:
				if i[0]==a:
					item.remove(i)
		elif choice == 3:
			x=input("Enter the name of the Fruit and rate you are searching for\n")
			y=int(input())
			for i in item:
				if (x in i and y in i):
					print("Yes "+x+" does belong to the fruit shop\n")
					break
				else:
					print("No doesnt exist\n")
		elif choice == 4:
			a=input("Enter the name of the fruit you are looking to change\n")
			b=int(input())
			for i in item:
				if(i[0]==a and i[1]==b):
					i[0]=input("Please enter the new name\n")
					i[1]=int(input("Please enter the new rate\n"))
		elif choice == 5:
			for i in item:
				print(str((item.index(i)+1))+"."+i[0]+" "+str(i[1]))
		else:
			print("Invalid input\n")
	else:
		print("Fruit shop is empty.\n")
			
