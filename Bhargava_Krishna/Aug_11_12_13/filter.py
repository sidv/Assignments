lst = []

for i in range (10,51):
	lst.append(i)
print(lst)

lst1 = list(filter(lambda a: a%2 == 0, lst))
print(lst1)
