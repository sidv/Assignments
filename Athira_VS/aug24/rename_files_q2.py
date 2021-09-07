from os import system
import string

count = 1
for i in string.ascii_lowercase:
    system(f"mv {i}.txt {count}{i}.txt")
    count += 1

print(system("ls"))

