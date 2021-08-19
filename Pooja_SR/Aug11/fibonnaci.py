#write a code to print fibonnaci series (1,1,2,3,5,8,13,21) till 100
a=0
b=1
while (a<100):
	c=b
	b=a
	a=c+b
	print(a)
	
