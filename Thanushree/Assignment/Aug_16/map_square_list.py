"""def create_list(r1,r2):
	return [i for i in range(r1,r2+1)]
r1,r2 = 10,50
"""
#print(create_list(r1,r2))
lst = []
for i in range(10,50):
	lst.append(i)


lst2 = list(map(lambda a:a*a,lst))
print(lst2)
