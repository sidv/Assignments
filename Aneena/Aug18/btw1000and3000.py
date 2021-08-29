#find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
lst = []
for x in range(1000,3001):
	count = 0
	for y in str(x):
		count+=1
		if int(y)%2 == 0:
			if count == len(str(x)):
				lst.append(x)
		else:
			break
print(lst)
