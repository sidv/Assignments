a = int(input("enter the 1st no : "))
b = int(input("enter the 2nd no : "))
c = int(input("enter the 3rd no : "))
d = int(input("enter the 4th no : "))

if (a > b and a>c and a>d):
	print(a,"is greater")
elif (b>c and b>d and b>a):
	print(b,"is greater")
elif (c>a and c>b and c>d):
	print(c,"is greater")
else:
	print(d,"is greater")
