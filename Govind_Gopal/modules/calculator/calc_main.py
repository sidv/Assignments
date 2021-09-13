import calc 

while True:
	calc.calc_menu()
	ch = input("Enter your choice")
	a = int(input("Enter the first number"))
	b = int(input("Enter the second number"))
	if ch == "1":
		calc.add(a,b)
	elif ch == "2":
		calc.sub(a,b)
	elif ch == "3":
		calc.mul(a,b)
	elif ch == "4":
		calc.div(a,b)
	elif ch == "5":
		break
	else:
		print("Invalid input")
