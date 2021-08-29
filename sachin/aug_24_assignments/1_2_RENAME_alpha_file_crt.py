#1.Write a program using os module to create all alphabetical letters file
#(E.g filename should be a.txt , b.txt and so on)(Use os module)
#2.Write a program to rename the file 1a.txt,2b.txt,3c.txt and so on(Use os module)


import os
import string

lst = []
count = 0
for j in range(1,27):
    lst.append(j)

for i in string.ascii_lowercase:
    os.system(f"touch {i}.txt")
  
for i in string.ascii_lowercase:
   os.system(f"mv {i}.txt {lst[count]}{i}.txt")
   count +=1