import os
import stat
import string

string = "abcdefghijklmnopqrstuvwxyz"
count=1
for i in string:
	os.rename(i+".txt",str(count)+i+".txt")
	count+=1
	
print(os.listdir())
