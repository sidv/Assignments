rangenum = int(input("Enter the limit : "))

a = 1
b = 1
count = 0

if rangenum==1:
	print(b)
else:
	while count < rangenum:
		if count == rangenum-1 :
			print(a)
		else:
			print(a,end=",")
		t = a + b
		a = b
		b = t
		count += 1
