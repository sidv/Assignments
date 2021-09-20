import calc as cf

while True:
	ch=int(input("1. for Addition.\n2. for Substraction.\n3. for Multiplication.\n4. for Division.\t"))
	
	if ch == 1:
		cf.add()
	elif ch == 2:
		cf.sub()
	elif ch == 3:
		cf.mul()
	elif ch == 4:
		cf.div()
	else:
		print("Invalid input.")
