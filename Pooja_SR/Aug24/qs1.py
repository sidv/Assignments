#1.Write a program using os module to create all alphabetical letters file
#(E.g filename should be a.txt , b.txt and so on)(Use os modul

import os
string="abcdefghijklmnopqrstuvwxyz"
for i in string:
	os.system(f"touch {i}.txt")
