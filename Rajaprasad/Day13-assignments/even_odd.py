num= int(input("Enter a number"))

for i in range(1,num):
	if i %2 == 0:
		print(f'{i} is an even number')
	else:
		print(f'{i} is an odd number')
