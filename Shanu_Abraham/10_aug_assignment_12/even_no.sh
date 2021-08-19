# Addition of all even numbers
num="1,2,3,4,5,6,7,8,9"
num1=num[::2]
print("The numbers are",num1)
even_nos=num1[1::2]
print("The even nos",even_nos)
sum=0
for i in even_nos:
	x=int(i)
	sum=sum+x
	print("The addition of even numbers",sum)

