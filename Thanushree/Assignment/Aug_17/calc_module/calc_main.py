#Menu driven Calculator
import calc_functions as c

while True:

	c.print_menu() # Use round braces with function always

	choice = int(input("Enter choice"))

	if choice == 1: #Its equal to
		#Sum
		num1,num2 = c.read_input()
		ret = c.sum(num1,num2)
		print(ret)
	elif choice == 2:
		#substract
		num1,num2 = c.read_input()
		ret = c.substract(num1,num2)
		print(ret)
	elif choice == 3:
                #multiply
                num1,num2 = c.read_input()
                ret = c.multiply(num1,num2)
                print(ret)
	elif choice == 4:
                #division
                num1,num2 = c.read_input()
                ret = c.division(num1,num2)
                print(ret)
	elif choice == 5:
                #floor_division
                num1,num2 = c.read_input()
                ret = c.floor_division(num1,num2)
                print(ret)
	elif choice == 6:
                #substract
                num1,num2 = c.read_input()
                ret = c.modulus(num1,num2)
                print(ret)
	elif choice == 7:
		break
	else:
		print("Invalid choice")
