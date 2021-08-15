# Addition of numbers
num="1,2,3,4,5,6,7,8,9"
num1=num[::2]
print("The numbers are",num1)
sum=0
for i in num1:
	x = int(i)
	sum=sum+x
	print("The sum is",sum)
