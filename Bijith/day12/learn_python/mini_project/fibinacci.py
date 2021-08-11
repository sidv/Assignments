
nterm = int(input("enter how much term"))

n1 = 0
n2 = 1
count=0

if nterm <= 0:
	print("enter positive integer")
elif nterm == 1:
	print(n1)
else:
	print("FIBONACCI SERIES: ")
	while count < nterm:
		print(n1) 
		nth = n1+n2
		n1=n2
		n2=nth
		count+=1
