num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
num4=int(input("Enter fourth number"))

if (num1 > num2):
	if (num1>num3):
		if (num1>num4):
			print("Greatest is ",num1)
elif(num2 >num3):
	if (num2>num4):
		print("Greatest is ",num2)
	else:
		if (num3>num4):
			print("Greatest is ",num3)	
		else:
			print("Greatest is ",num4)	
			

