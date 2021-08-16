#1.Write a python code to take string input from user and remove duplicate words.

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
	
