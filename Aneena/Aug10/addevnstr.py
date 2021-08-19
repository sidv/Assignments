#Perform addition of all even number from string

num="1,2,3,4,5,6,7,8,9"

sum=0
for i in num[0:17:2]:
	if (int(i)%2==0):
		sum=sum+int(i)
print(sum)
