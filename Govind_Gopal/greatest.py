num1 = int(input("enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("enter the third number"))
num4 = int(input("enter the fourth number"))



if ((num1 > num2) and (num1 > num3) and (num1 > num4)) :
	print ("{} is the greatest".format(num1))

elif ((num2 > num1) and (num2 > num3) and (num2 > num4)) :
	print ("{} is the greatest".format(num2))

elif ((num3 > num1) and (num3 > num2) and (num3 > num4)) :
	print ("{} is the greatest".format(num3))
elif ((num4 > num2) and (num4 > num3) and (num4 > num1)) :
	print("{} is the greatest".format(num4))
else:
	print("invalid input")


