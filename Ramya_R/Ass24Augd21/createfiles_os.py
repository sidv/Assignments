import os
import stat
import string

string = "abcdefghijklmnopqrstuvwxyz"
for i in string:
	os.system(f"touch {i}.txt")
print(os.listdir())
