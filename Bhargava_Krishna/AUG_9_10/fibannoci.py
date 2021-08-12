n = int(input("Enter the number"))

a=0
b=1

while a<n:
	print(a,end=",")
	a,b=b,a+b
