rangenum = int(input("Enter the number"))

num1 = 0
num2 = 1
count = 0
if rangenum <= 0:
	print ("enter valid range")
	
elif rangenum == 1:
	print (num1)

else:
	print("Fibonacci Series")
	while(count<rangenum):
		print(num1)
		num3 = num1+num2
		num1 = num2 
		num2 = num3
		count+=1
