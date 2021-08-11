num1= int(input("Enter first number"))
num2 = int(input("Enter 2nd number : "))

if num1 % num2 == 0 :
	print(f'{num1} divisible by {num2} ')
elif num2 % num1 == 0 :
	print(f'{num2} divisible by {num1} ')
else:
	print('not divisible')
