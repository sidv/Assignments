num="1,2,3,4,5,6,7,8,9"
a=num[0::2]
print(a)
r=int(a[0])+int(a[1])+int(a[2])+int(a[3])+int(a[4])+int(a[5])+int(a[6])+int(a[7])+int(a[8])

print(r)

b=0
for i in range(0,len(a)):
	b = b + int(a[i])

print(b)

