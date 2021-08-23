coma=input("Enter sequence by coma separated")
new=coma.split(",")
print(new)
sum=0
for i in new:
	sum=sum+int(i)

print(sum)
