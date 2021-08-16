sq_d={}

l=int(input("Enter the limit.\n"))
l=l+1

for i in range(1,l):
	sq_d[i]=i*i
	

for i in sq_d.keys():
	print(f"{i} |  {sq_d[i]}")
