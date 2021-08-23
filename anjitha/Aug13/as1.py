
str=input("Enter new string!!")
new=str.split(" ")
count=0
for i in new:
	temp=i
	for j in new:
		if(j==temp):
			count=count+1
			print(j)
		if(count>1):
			new.remove(j)
			
print(new)
