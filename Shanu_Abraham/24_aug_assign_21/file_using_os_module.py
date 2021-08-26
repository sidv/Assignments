#Write a program using os module to create all alphabetical letters file
#(E.g filename should be a.txt , b.txt and so on)(Use os module)


import os
import string

for i in string.ascii_lowercase:
	os.system(f"touch {i}.txt")
