num="1,2,3,4,5,6,7,8,9"
a=num[0::2]
print(a)
#without loop
r=int(a[0])+int(a[1])+int(a[2])+int(a[3])+int(a[4])+int(a[5])+int(a[6])+int(a[7])+int(a[8])
print("add all num")
print(r)
#using for loop
b=0
for i in range(0,len(a)):
	b = b + int(a[i])

print(b)

#Even number addition
z=a[1::2]
print("even-----")
print(z)
print("add even")
#without loop
x=int(z[0])+int(z[1])+int(z[2])+int(z[3])
print(x)

#with loop
y=0
for j in range(0,len(z)):
	y = y + int(z[j])

print(y)	
