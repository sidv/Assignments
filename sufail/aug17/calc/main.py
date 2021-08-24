import cal

def menu():
	print("1 for addition")
	print("2 for subtraction")
	print("3 for muliplication")
	print("4 for division")
	print("5 for exit")
def  getvalue():
	a=int(input("enter first number"))
	b=int(input("enter second number"))
	return a,b
while True:
	menu()
	choice=int(input("Enter choice"))
	if choice ==1:
		a,b=getvalue()
		print("result",cal.add(a,b))
	elif (choice ==2):
		a,b=getvalue()
		print("result",cal.sub(a,b))
	elif (choice ==3):
		a,b=getvalue()
		print("result",cal.mul(a,b))
	elif (choice ==4):
		a,b=getvalue()
		print("result",cal.div(a,b))
	else:
		break
