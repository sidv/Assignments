n1=int(input("enter the number"))
m=int(input("enter the number"))
n3=int(input("enter the number"))
n4=int(input("enter the number"))

if((n1 > m) & (n1 > n3) & (n1 > n4)):
	print(n1,"is greater than ",m,",",n3,",",n4)
elif((m > n1) & (m > n3) & (m > n4)):
	print(m,"is greater than ",n1,",",n3,",",n4)
elif((n3 > n1) & (n3 > m) & (n3 > n4)):
	print(n3,"is greater than ",n1,",",m,",",n4)
else:
	print(n4,"is greater than ",n1,",",m,",",n3)
