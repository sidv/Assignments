import os 

#1.Write a program using os module to create all alphabetical letters file
[os.system(f"touch {i}.txt") for i in "abcdefghijklmnopqrstuvwxyz"]

#2.Write a program to rename the file 1a.txt,2b.txt,3c.txt and so on(Use os module)
[os.rename(x,str(y)+x) for y,x in enumerate(os.listdir()) if x.split(".")[1] == "txt"]
