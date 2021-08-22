while True:
	print("Press 1 for add")
	print("Press 2 for substract")
	print("Press 3 for mulutification")
	print("Press 4 for division")
	print("Press 5 for floor division")
	print("Press 6 for modulus")
	print("Press 7 to exit")


	choice = int(input("Enter choice"))
	if choice != 7: # != means not equal to
		num1 = int(input("Enter number 1 :"))
		num2 = int(input("Enter number 2 :"))

	if choice == 1: 
		res = num1 + num2
		print(res)
	elif choice == 2:
		res = num1 - num2
		print(res)
	elif choice == 3:
		res= num1* num2
		print(res)
	elif choice == 4:
		res = num1/num2
		print(res)
	elif choice == 5:
                res = num1//num2
                print(res)
	elif choice == 6:
                res = num1%num2
                print(res)
	elif choice ==7:
		print("exit"))
                break

	else:
		print("Invalid choice")
