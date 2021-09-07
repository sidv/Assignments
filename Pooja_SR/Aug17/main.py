import calc
while True:
	print("press 1 for addition")
	print("press 2 for substraction")
	print("press 3 for multiplication")
	print("press 4 for division")
	print("press 5 for floor division ")
	print("press 6 for modulas")
	print("press 7 for exit")
	choice = int(input("enter your choice"))
	if choice !=7:
		num1=float(input("enter number 1:"))
		num2=float(input("enter number 2:"))
	if choice ==1:
		calc.sum(num1,num2)
	elif choice ==2:
                calc.sub(num1,num2)
	elif choice ==3:
                calc.mul(num1,num2)
	elif choice ==4:
                calc.div(num1,num2)
	elif choice ==5:
                calc.fldiv(num1,num2)
	elif choice ==6:
                calc.mod(num1,num2)
	elif choice ==7:
                break	
	else:
		print("invalid")
