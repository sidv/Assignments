while True:
	print("1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Floor Division 6.Modulas")
	choice=int(input("Enter choice"))
	num1=int(input("Enter first number"))
	num2=int(input("Enter second number"))
	if(choice ==1):
		print("Addition is ",(num1+num2))
		break;
	elif(choice ==2):
		print("Subtraction is ",(num1-num2))
	elif(choice ==3):
		print("Multiplication is ",(num1*num2))
	elif(choice ==4):
		print("Division is ",(num1/num2))
	elif(choice ==5):
		print("Floor division is ",(num1//num2))
	elif(choice ==6):
		print("Modulas, is ",(num1%num2))
	else:
		print("Not a valid choice")
		
