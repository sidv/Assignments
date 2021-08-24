#Menu driven Calculator

import calc
while True:
	print("1.ADDITION")
	print("2.SUBSTRACTION")
	print("3.MULTIPLICATION")
	print("4.DIVISION")
	print("5.FLOOR DIVISION")
	print("6.MODULUS")
	print("7.EXIT")

	choice = int(input("Enter choice"))
	if choice != 7: 
		a = int(input("Enter number 1 :"))
		b = int(input("Enter number 2 :"))

	if choice == 1: #Its equal to
		calc.sum(a,b)
		
	elif choice == 2:
		calc.sub(a,b)
		
	elif choice == 3:
		calc.mul(a,b)
	elif choice == 4:
		calc.div(a,b)

	elif choice == 5:
		calc.floordiv(a,b)

	elif choice == 6:
		calc.mod(a,b)
	
	elif choice == 7:
		break
	else:
		print("Invalid choice")
