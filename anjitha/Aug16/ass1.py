

l=[]

for i in (10,51):
	l.append(i)
print(l)

li=list(map(lambda a:a*a,l))
print(li)

l=list(filter(lambda a:a%2==0,l))
print(l)
