print("Enter four numbers")

num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())

if(num1>num2 and num1>num3 and num1>num4):
	print(str(num1)+" is greatest\n")
elif(num2>num3 and num2>num4):
	print(str(num2)+" is greatest\n")
elif(num3>num4):
	print(str(num3)+" is greatest\n")
else:
	print(str(num4)+" is greatest\n")
