
#1.Write a program using os module to create all alphabetical letters file(E.g filename should be a.txt , b.txt and so on)(Use os module)

import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_lowercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

#2.Write a program to rename the file 1a.txt,2b.txt,3c.txt and so on(Use os module)

import os
string = "abcdefghijklmnopqrstuvwxyz"

for i in string:
	os.system(f"touch {i}.txt")

k=1
for j in string:
	os.rename(f"{j}.txt",f"{k}{j}.txt")
	k+=1
