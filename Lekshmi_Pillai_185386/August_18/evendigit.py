#4.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even #number.The numbers obtained should be printed in a comma-separated sequence on a single line.

lst = []

for i in range(1000,3001):
	count = 0
	for j in str(i):
		count+=1
		if int(j)%2 == 0:
			if count == len(str(i)):
				lst.append(i)
		else:
			break
print(lst)
			
	
