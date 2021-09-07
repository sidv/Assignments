
while True:

	choice=int(input("Enter \n1 for Addition\n2 for Substraction\n3 for Multipication\n4 for Division\n"))

	num1=float(input("Enter first number\n"))
	num2=float(input("Enter second number\n"))
	
	if choice == 1:
		print(num1+num2)
	elif choice == 2:
		if(num1>num2):
			print(num1-num2)
		else:
			print(num2-num1)
	elif choice == 3:
		print(num1*num2)
	elif choice == 4:
		print(num1/num2)
	else:
		print("Invalid input")
