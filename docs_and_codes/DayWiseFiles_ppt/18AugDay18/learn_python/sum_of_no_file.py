fd = open("nums.txt","r") 
data = fd.read()
print(data)
lst = data.split(",")
print(lst)
sum=0
for i in lst:
	sum=int(i)+sum
print(sum)
fd.close()

