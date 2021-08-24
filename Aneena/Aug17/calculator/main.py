import calc

def menu():
	print("1.Addition")
	print("2.Subtraction")
	print("3.Muliplication")
	print("4.Division")
	print("5.Exit")
def  getvalue():
	a=int(input("Enter first number\n"))
	b=int(input("Enter second number\n"))
	return a,b
while True:
	menu()
	choice=int(input("Enter choice\n"))
	if choice ==1:
		a,b=getvalue()
		print("result",calc.add(a,b))
	elif (choice ==2):
		a,b=getvalue()
		print("result",calc.sub(a,b))
	elif (choice ==3):
		a,b=getvalue()
		print("result",calc.mul(a,b))
	elif (choice ==4):
		a,b=getvalue()
		print("result",calc.div(a,b))
	else:
		break
