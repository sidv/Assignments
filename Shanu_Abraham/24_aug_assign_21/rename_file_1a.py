#Write a program to rename the file 1a.txt,2b.txt,3c.txt and so on(Use #os module)

import os
import string

lst = []
for j in range(1,27):
	lst.append(j)

count=0
for i in string.ascii_lowercase:
	os.system(f"mv {i}.txt {lst[count]}{i}.txt")
	count = count+1
