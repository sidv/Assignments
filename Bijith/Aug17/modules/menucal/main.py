import cal
while True:
	
	print("1.Addition")
	print("2.Substraction")
	print("3.Multiplication")
	print("4.Division")
	print("5.Floor Division")
	print("6.Exit")

	choice =  int(input("Enter your choice"))

	a=int(input("Enter the first number"))
	b=int(input("Enter the second number"))	

	if choice == 1:
		cal.sum(a,b)
	elif choice == 2:
		cal.sub(a,b)
	elif choice == 3:
        	cal.mul(a,b)
	elif choice == 4:
        	cal.div(a,b)
	elif choice == 5:
        	cal.fldiv(a,b)
	elif choice == 6:
		break
	else:
		print("invalid choice")

