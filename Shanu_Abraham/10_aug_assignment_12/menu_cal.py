#Menu driven calculator
while True:
	print("Press 1 to Addition")
	print("Press 2 to Subtraction")
	print("Press 3 to Multiplication")
	print("Press 4 to Division")
	print("Press 5 to Floor Division")
	print("Press 6 to Modulus")
	print("press 7 to Exit")
	choice=int(input("enter the choice"))
	if choice == 7:
		break
	num1=input("enter the no")
	num2=input("enter the no")
	if choice == 1:
		res=float(num1)+float(num2)
		print("The sum is",res)
	elif choice == 2:
		res=float(num1)-float(num2)
		print("The diff is",res)
	elif choice == 3:
		res=float(num1)*float(num2)
		print("The multiplication is",res)
	elif choice == 4:
		res=float(num1)/float(num2)
		print("The division is",res)
	elif choice == 5:
		res=float(num1)//float(num2)
		print(type(res))
		print("The floor division is",res)
	elif choice == 6:
		res=float(num1)%float(num2)
		print("the modulus is",+res)
	else:
		print("invalid choice")
