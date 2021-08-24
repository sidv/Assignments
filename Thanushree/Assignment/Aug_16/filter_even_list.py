lst=[]
for i in range(10,50):
	lst1=lst.append(i)

lst2 = list(filter(i%2 == 0,lst1))
print(lst2)
