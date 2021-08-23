str = str(input("Enter the string input"))
strsplit = str.split(" ")
print(strsplit)
lst=[]
for i in range(0,len(strsplit)):
	print(strsplit[i])
	if(strsplit[i] not in lst):
		lst.append(strsplit[i])
print (lst)
str = " ".join(lst)
print(str)
