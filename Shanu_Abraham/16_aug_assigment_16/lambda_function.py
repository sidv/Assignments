lst=[]
for i in range(10,51):
	lst.append(i)
print(lst)
lst = list(map(lambda a:a*a,lst))
print(lst)

even_list =list(filter(lambda a:a%2==0,lst))
print(even_list)
