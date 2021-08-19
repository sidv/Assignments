#Find greater number from Four  numbers

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
num4 = int(input("Enter fourth number"))

if ((num1 > num2)or(num1 > num3)or(num1 > num3)):
	#if num1 > num3:
		#if num1 > num4:
		print(str(num1)+" is greater")
elif ((num2 > num3)or(num2 > num4)):
	#if num2 > num4:
		print(str(num2)+" is greater")
else:
	if (num3 > num4):
		print(str(num3)+" is greater")
	else:
		print(str(num4)+" is greater")
