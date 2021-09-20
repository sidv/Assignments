def add():
	x=int(input("Enter the first number to be added\t"))
	y=int(input("Enter the second number to be added\t"))
	print(x+y)
def sub():
	x=int(input("Enter the first number to be substracted\t"))
	y=int(input("Enter the second number to be substracted\t"))
	if x>y:
		print(x-y)
	else:
		print(y-x)
		
def mul():
	x=int(input("Enter the first number to be multiplied\t"))
	y=int(input("Enter the second number to be multiplied\t"))
	print(x*y)
	
def div():
	x=int(input("Enter the Divident\t"))
	y=int(input("Enter the Divisor\t"))
	if y!=0:
		print(x/y)
	else:
		print("Infinity")
