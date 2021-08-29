l=int(input("enter limit"))

f=0
s=1
count=0
while count<l:
	print(f,end=",")
	fib=f+s
	f=s
	s=fib
	count+=1
