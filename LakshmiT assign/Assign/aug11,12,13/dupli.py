string = input("Enter the string")

strsplit = string.split(" ")
print(strsplit)
lst=[]
for i in range(0,len(strsplit)):
	print(strsplit[i])
	if(strsplit[i] not in lst):
		lst.append(strsplit[i])
print (lst)
string = " ".join(lst)
print(string)
