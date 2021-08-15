#print table of given no(input from user)

num=int(input("Enter the number"))
print("Multiplication table of :")
for i in range(1,11):
	r=i*num
	print(num, '*' ,i, ' = ', r)
