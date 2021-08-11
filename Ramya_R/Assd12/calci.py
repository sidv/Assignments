#Menu driven Calculator

while True:
	print("Press 1 for add")
	print("Press 2 for substract")
	print("press 3 for multiplication")
	print("press 4 for division")
	print("press 5 for floor division")
	print("press 6 for modulus")
	print("press 7 for power values")
	print("Press 8 to exit")

	choice = int(input("Enter choice"))
	if choice != 8: # != means not equal to
		num1 = int(input("Enter number 1 :"))
		num2 = int(input("Enter number 2 :"))

	if choice == 1: #Its equal to
		res = num1 + num2
		print(res)
	elif choice == 2:
		res = num1 - num2
		print(res)
	elif choice == 3:
		res = num1 * num2
		print(res)
	elif choice == 4:
		res = num1 / num2
		print(res)
	elif choice == 5:
		res = num1 // num2
		print(res)
	elif choice == 6:
		res = num1 % num2
		print(res)
	elif choice == 7:
		res = num1 ** num2
		print(res)
	elif choice == 8:
		break
	else:
		print("Invalid choice")
