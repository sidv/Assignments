
lst=[]
for i in range (1,11):
	lst.append(i)
print(lst)



l=list(map(lambda b:b**2, filter( lambda a:a%2==0, lst)))
print(l)






