import calc as ca
while True:

	print("enter 1 for Addition")
	print("enter 2 for Substraction")
	print("enter 3 for Multiplication")
	print("enter 4 for Division")
	print("enter 5 for Floor division")
	print("enter 6 for Modulus")
	print("enetr 7 for exit")

	c = int(input("enter the choice : "))
	if c==7:
                exit()

	a = float(input("enter the 1st no : "))
	b = float(input("enter the 2nd no : "))
	
	if c==1:
		ca.sum(a,b)
	elif c==2:
                ca.sub(a,b)
	elif c==3:
                ca.mul(a,b)
	elif c==4:
                ca.div(a,b)
	elif c==5:
                ca.floordiv(a,b)
	elif c==6:
                ca.mod(a,b)
	else:
		print("invalid option")
