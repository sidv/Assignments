#Check given number divisible by given number

num1=int(input("enter a number"))
num2=int(input("enter another number"))
if num1%num2 == 0:
	print(str(num1)+"is divisible by"+str(num2))
else:
	print(str(num1)+"is not divisible by"+str(num2))
