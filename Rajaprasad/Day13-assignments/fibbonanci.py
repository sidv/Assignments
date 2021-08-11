num = int(input('Enter the  number'))
a=0
b=1
while a<num:
	print(a,end=",")
	a,b = b,a+b 
