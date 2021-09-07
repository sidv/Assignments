
import os

alpha = "abcdefghijklmnopqrstuvwxyz"

count = 1
for i in alpha:
	os.rename(f"{i}.txt", f"{count}{i}.txt")
	count += 1
