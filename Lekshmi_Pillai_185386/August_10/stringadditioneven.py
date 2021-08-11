num="1,2,3,4,5,6,7,8,9"
i=2
sum1=0
while(i<len(num)):
	
	a=int(num[i])
	if (a%2==0):
		print(a)
		sum1 = sum1 + a
		i+=4
	else:
		i+=4
print("Sum is ",sum1)
