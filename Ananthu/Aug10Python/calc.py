print("MENU DRIVEN CALCULATOR")

while True:
	print("1.ADDITION")
	print("2.SUBTRACTION")
	print("3.MULTIPLICATION")
	print("4.DIVISION")
	print("5.FLOOR DIVISION")
	print("6.MODULUS")
	print("7.Exit")

	choice = int(input("Enter your choice : "))

	if choice != 7:
		a = int(input("Enter the first number : "))
		b = int(input("Enter the second number : "))

	if choice == 1:
		print(a,"+",b,"=",a+b)

	elif choice == 2:
        	print(a,"-",b,"=",a-b)

	elif choice == 3:
        	print(a,"*",b,"=",a*b)

	elif choice == 4:
        	print(a,"/",b,"=",a/b)

	elif choice == 5:
        	print(a,"//",b,"=",a//b)

	elif choice == 6:
        	print(a,"%",b,"=",a%b)
	elif choice == 7:
		break

	else:
		print("Invalid Choice")
