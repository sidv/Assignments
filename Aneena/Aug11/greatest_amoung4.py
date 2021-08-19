#greatest amoung four

num1=int(input("Enter the first number\n"))
num2=int(input("Enter the second number\n"))
num3=int(input("Enter the third number\n"))
num4=int(input("Enter the fourth number\n"))
if num1 > num2 and num1 > num3 and num1 > num4:
	print(str(num1)+"is greater")

elif    num2 > num1 and num2 > num3 and num2 > num4:
	print(str(num2)+"is greater")

elif	num3 > num1 and num3 > num2 and num3 > num4:
	print(str(num3)+"is greater")
else:
	print(str(num4)+"is greater")
