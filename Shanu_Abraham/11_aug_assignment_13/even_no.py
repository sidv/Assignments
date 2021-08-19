limit=int(input("enter the range"))
print("The given range of numbers")
for i in range(1,limit+1):
	print(i)
print("The even numbers are:")
for i in range(1,limit+1):
	if i%2==0:
		print(i)
