import os
string = "abcdefghijklmnopqrstuvwxyz"

for i in string:
	os.system(f"touch {i}.txt")

k=1
for j in string:
	os.rename(f"{j}.txt",f"{k}{j}.txt")
	k+=1
