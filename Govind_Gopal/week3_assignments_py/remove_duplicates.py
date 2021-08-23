strng = []
i = 0
num = int(input("Enter the number of elements\t"))
while i < num :
	text = input("Enter the texts to be added\t")
	strng.append(text)
	i += 1

print (set(strng))
