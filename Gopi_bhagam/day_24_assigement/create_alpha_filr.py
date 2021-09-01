
import os
alpha= "abcdefghijklmnopqrstuvwxyz"

for i in alpha:
	os.system(f"touch {i}.txt")

count=1
for j in alpha:
	os.rename(f"{j}.txt",f"{count}{j}.txt")
	count=count+1
