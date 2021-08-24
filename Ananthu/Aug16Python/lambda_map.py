lst = []
for i in range(10,51):
	lst.append(i)
print(lst)

lst = list(map(lambda a:a*a,lst))
print(lst)
