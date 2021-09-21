fruit = []
rate=[]
while True:
	print("1.-Add fruit")
	print("2.-Delete fruit by name")
	print("3.-Search fruit by name and rate")
	print("4.-Change fruit name and rate")
	print("5.-Display")
	print("6.exit")
	
	ch = int(input("Enter a choice"))
	
	if ch == 1:
		fruit.append(input("Enter fruit name : "))
		rate.append(input("Enter rate : "))
		print("Fruit and rate added successfully")
	elif ch == 2:
		fr = input('Enter fruit name : ')
		rt = input('Enter rate')
		fruit.remove(fr)
		rate.remove(rt)
		print(f'{fr} {rt} removed from list')

	elif ch == 3:
		fr=input("Enter fruit name to search")
		rt = input("Enter rate for fruit: ")
		if fr in fruit:
			print(fruit)
		elif rt in rate:
			print('rate is ',rate) 
		else:
			print('not found')
	elif ch == 4:
		fr=input("Enter fruit name ")
		rt = input("Enter rate for fruit: ")
		fr1 = fruit.index(fr)
		fruit[fr1] = input('Enter new fruit name')
		rt1 = rate.index(rt)
		rate[rt1] = input('Enter new rate for fruit')
		print('new fruit and rate updated')
	elif ch == 5:
		new=[]
		for i in range(len(fruit)):
			for j in range(len(rate)):
				new.append([fruit[i],rate[j]])
		print(new)
	elif ch == 6:
		break
	else:
		print('you have choosen wrong key')

