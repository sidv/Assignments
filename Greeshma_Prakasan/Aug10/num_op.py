num = "1,2,3,4,5,6,7,8,9"
s = 0
for i in num[::2]:
	s += int(i)
print("sum of no's",s)

e=0
for i in num[2::4]:
	e += int(i)
print("sum of even no's",e)	
