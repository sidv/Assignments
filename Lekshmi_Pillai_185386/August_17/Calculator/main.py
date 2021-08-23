import calc

def menu():
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("5. Exit")
while True:
	menu()
	ch = int(input("Enter the choice"))
	num1 = int(input("Enter first number"))
	num2 = int(input("Enter first number"))
	if ch ==1:
		res = calc.add(num1,num2)
		print(res)
	elif ch == 2:
		res = calc.subb(num1,num2)
		print(res)
	elif ch == 3:
		res = calc.mul(num1,num2)
		print(res)
	elif ch == 4:
		res = calc.div(num1,num2)
		print(res)
	elif ch == 5:
		break
	else:
		print("Invalid Choice")
		
	
