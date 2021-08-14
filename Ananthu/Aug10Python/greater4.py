a = int(input("Enter the first num : "))
b = int(input("Enter the second num : "))
c = int(input("Enter the third num : "))
d = int(input("Enter the fourth num : "))

if a>b:
	if a>c:
		if a>d:
			print(a,"is bigger")
if b>c:
	if b>d:
		print(b,"is bigger")
if c>d:
	print(c,"is bigger")
else:
	print(d,"is bigger")
