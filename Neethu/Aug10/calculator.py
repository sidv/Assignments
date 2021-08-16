#Menu driven Calculator

while True:
	print("Press 1 for add")
	print("Press 2 for substract")
	print("Press 3 to exit")
	print("press 4 for multiplication")
	print("press 5 for Division")
	print("press 6 for floor division")

	choice = int(input("Enter choice"))
	if choice != 3: # != means not equal to
		num1 = int(input("Enter number 1 :"))
		num2 = int(input("Enter number 2 :"))

	if choice == 1: #Its equal to
		res = num1 + num2
		print(res)
	elif choice == 2:
		res = num1 - num2
		print(res)
	elif choice == 4:
		res = num1 * num2
		print(res)
	elif choice == 5:
		res = num1 % num2
		print(res)
	elif choice == 6:
		res = num1 // num2
		print(res)
	elif choice == 3:
		break
	else:
		print("Invalid choice")
