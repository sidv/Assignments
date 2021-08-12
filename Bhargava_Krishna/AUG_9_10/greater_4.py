a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))
d = int(input("Enter 4th number"))

if (a>b and a>c and a>d):
	print("The greater num is" +str(a))
elif(b>a and b>c and b>d):
	print("The greater num is" +str(b))
elif(c>a and c>b and c>d):
	print("The greater num is" +str(c))
else:
	print("The greater num is" +str(d))
