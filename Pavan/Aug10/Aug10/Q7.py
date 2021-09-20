nums="1,2,3,4,5,6,7,8,9"

num=nums.split(",")

sum=0

for i in num:
	sum=sum+int(i)

print(sum)

print("\n___________Second part_____________\n")

Sum=0

for i in num:
	if int(i)%2==0:
		Sum+=int(i)

print(Sum)
