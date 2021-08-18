#perform addition of all number in string
print("addition of all number")
num="1,2,3,4,5,6,7,8,9"
s=0
for i in num[0:17:2]:
	s=s+int(i)
print(s)

#perform addition of all even number from string 
print("addition of all even number")
s=0
for i in num[2:17:4]:
        s=s+int(i)
print(s)

