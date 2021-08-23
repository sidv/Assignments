binary = [1000,1100,1110,1111,1101,1010]
lst= []
for i in binary:
	a = int(str(i),2)
	if a % 5 ==0:
		lst.append(i)
print(lst)
