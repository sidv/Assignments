print("________________Calculator______________")


while True:
	print("press 1 for Addition")
	print("press 2 for subtraction")
	print("press 3 for Multiplication")
	print("press 4 for Division")
	print("press 5 for Floor Division")
	print("press 6 for  Modulus")
	print("press 7 for exit")
	choice = int(input("Enter choice"))

	if(choice == 7):
		break

	num1 = int(input("Enter First number"))
	num2 = int(input("Enter Second number"))
	
	if (choice == 1):
		print("the result is " ,num1+num2)
	elif (choice == 2):
		print("the result is " , num1-num2)
	elif (choice ==3):
		print("the result is " , num1*num2)
	elif (choice == 4):
		print(" the result is " , num1/num2)
	elif (choice == 5):
		print("the result is" , num1//num2)
	elif (choice == 6):
		print("the result is " , num1%num2)
	else:
		print("invalid choice") 
