lst=[]
for i in range(10,51):
	#print(i)
	lst.append(i)
print(lst)
out = list(filter(lambda a: a%2 == 0,lst))
print(out)
