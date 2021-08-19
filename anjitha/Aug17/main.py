

import calc


while True:
	print("Enter 1 for Additon")
	print("Enter 2 for Substraction")
	print("Enter 3 for Multiplication")
	print("Enter 4 for Division")
	print("Enter 5 for Modulus")
	print("Enter 6 for Floor Division")
	print("Enter 7 for Exit")
	cho =int(input("\tEnter your choice."))
	if cho == 1:
		calc.add() 
	elif cho == 2:
		calc.sub()
	elif cho == 3:
		calc.mul()
	elif cho == 4:
		calc.div()
	elif cho == 5:
		calc.modulus()
	elif cho == 6:
		calc.floordiv()
	elif cho == 7:
		break
	else:
		print("invalid choice!!")

