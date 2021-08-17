lst=[]
for i in range(10,51):
	#print(i)
	lst.append(i)
print(lst)
out = list(map(lambda a: a*a,lst))
print(out)
