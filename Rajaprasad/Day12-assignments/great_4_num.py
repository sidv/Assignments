print("Findout the greatest num from 4 numbers")

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))
num4 = int(input("Enter 4th number:"))

if (num1>num2 and num1>num3 and num1 > num4):
	print(f'{num1} is the greatest number')
elif (num2>num1 and num2>num3 and num2 > num4):
	print(f'{num2 } is greatest number')

elif (num3>num1 and num3>num2 and num3 > num4):
        print(f'{num3 } is greatest number')
else :
        print(f'{num4 } is greatest number')

