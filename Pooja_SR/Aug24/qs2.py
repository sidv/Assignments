#Write a program to rename the file 1a.txt,2b.txt,3c.txt and so on(Use os module)

import os
string="abcdefghijklmnopqrstuvwxyz"
k=1
for i in string:
	os.rename(f"{i}.txt",f"{k}{i}.txt")
	k+=1
