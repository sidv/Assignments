s = input("Enter the string : ")
c = 0
for i in s:
	if i.isalnum():
		c += 1
print(c)
