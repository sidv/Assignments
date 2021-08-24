lst = []

for i in range(1000,3001):
	count = 0
	for j in str(i):
		count+=1
		if int(j)%2==0:
			if count == len(str(i)):
				lst.append(i)
		else:
			break
print(lst)

