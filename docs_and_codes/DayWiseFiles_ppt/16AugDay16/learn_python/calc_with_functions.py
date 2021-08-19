#Menu driven Calculator


def print_menu():
	print("Press 1 for add")
	print("Press 2 for substract")
	print("Press 3 to exit")

def read_input():
	x = int(input("Enter number "))
	y = int(input("Enter number "))
	return x,y

def sum(x,y):
	return x + y

def substract(x,y):
	return x - y

while True:

	print_menu() # Use round braces with function always

	choice = int(input("Enter choice"))

	if choice == 1: #Its equal to
		#Sum
		num1,num2 = read_input()
		ret = sum(num1,num2)
		print(ret)
	elif choice == 2:
		#substract
		num1,num2 = read_input()
		ret = substract(num1,num2)
		print(ret)
	elif choice == 3:
		break
	else:
		print("Invalid choice")

