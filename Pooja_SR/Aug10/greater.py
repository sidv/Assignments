#find greater number from four number
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
num3=int(input("enter 3rd number"))
num4=int(input("enter 4th number"))
if (num1 > num2):
	if (num1 > num3):
		if(num1 > num4):
			print(str(num1)+"is greater")
elif (num2 > num3):
	if (num2 > num4):
			print(str(num2)+"is greater")
else:
	if (num3 > num4 ):
		print(str(num3)+"is greater")
	else:
		print(str(num4)+"is greater")
