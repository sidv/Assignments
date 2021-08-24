
lst=[]
for i in range (1000,3001):
	lst.append(i)


l=list(filter( lambda a:a%2==0, lst))
print(l)

