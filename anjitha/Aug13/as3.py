

first=0
second=1

n=int(input("Enter the range"))
m=n-2
print(first)
print(second)
for i in range(m):
	third=first+second
	print(third)
	first=second
	second=third


