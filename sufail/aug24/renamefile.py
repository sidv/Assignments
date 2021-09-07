import os
alpha="abcdefghijklmnopqrstuvwxyz"
j=1
for i in alpha:
	os.rename(f"{i}.txt",f"{i}{j}.txt")
	k=+1
