# Program to find greatest no out of four nos

num1 = int(input("enter the 1st no"))
num2 = int(input("enter the 2nd no"))
num3 = int(input("enter the 3rd no"))
num4 = int(input("enter the 4th no"))
if ((num1>num2) and (num1>num3) and (num1>num4)):
	print("The greater no is",num1)
elif((num2>num1) and (num2>num3) and (num2>num4)):
	print("The greater no is",num2)
elif((num3>num1) and (num3>num2) and (num3>num4)):
	print("The greater no is",num3)
else:
	print("The greater no is",num4)
