# Menu driven code to print table of given number for given range

num=int(input("Enter the number"))
range=int(input("Enter the range"))
count=1
while count<=range:
	result=count*num
	print(result)
	count=count+1
