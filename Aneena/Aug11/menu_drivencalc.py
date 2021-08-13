#Menu driven calculator

while True:
	num1=int(input("enter num1"))
	num2=int(input("enter num2"))
	choice = int(input("enter choice"))
	print("Press 1 for Addition")
	print("Press 2 for Subtraction")
	print("Press 3 for Multiplication")
	print("Press 4 for Division")
	print("Press 5 for Floor division")
	print("Press 6 for Modulas")
	print("Press 7 for Exit")
#	choice = int(input("enter choice"))
#	num1=int(input("enter num1"))
#	num2=int(input("enter num2"))

	
	if choice == 1:
		res=num1+num2
		print(res)
	if choice == 2:
		res=num1-num2
		print(res)	
	if choice == 3:
		res=num1*num2
		print(res)
	if choice == 4:
		res=num1/num2
		print(res)
	if choice == 5:
		res=num1//num2
		print(res)
	if choice == 6:
		res=num1%num2
		print(res)
	if choice == 7:
	        break;
#	else:

#		print("Invalid choice")
