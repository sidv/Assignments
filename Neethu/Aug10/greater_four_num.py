#Find greater number from foure numbers

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
num4 = int(input("Enter four number"))
if num1 > num2:
	if num1 > num4:
		print(str(num1)+" is greater")
else:
	if num2 > num4:
		print(str(num2)+ " is greater")
	else:
		print(str(num4)+ " is greater")
