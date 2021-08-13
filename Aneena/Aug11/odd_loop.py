#printing odd numbers using loop
print("Printing odd numbers")
r = int(input("Enter the range"))
for i in range(r+1):
	if(i%2!=0):
		print(str(i))

