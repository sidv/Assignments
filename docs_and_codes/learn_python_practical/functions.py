#Menu driven Calculator




def sum(num1,num2): #defining function (Order of the argument must be same)
	print(num1+num2)

num1 = int(input("Enter number "))
num2 = int(input("Enter number "))

sum(num1,num2) #Calling function with two input(parameters,arguments)










#while True:
#	print("Press 1 for add")
#	print("Press 2 for substract")
#	print("Press 3 to exit")
#
#	choice = int(input("Enter choice"))
#	if choice != 3: # != means not equal to
#		num1 = int(input("Enter number 1 :"))
#		num2 = int(input("Enter number 2 :"))
#
#	if choice == 1: #Its equal to
#		res = num1 + num2
#		print(res)
#	elif choice == 2:
#		res = num1 - num2
#		print(res)
#	elif choice == 3:
#		break
#	else:
#		print("Invalid choice")
#
