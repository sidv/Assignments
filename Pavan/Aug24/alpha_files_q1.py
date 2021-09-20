from os import system
import string

for i in string.ascii_lowercase:
    system(f"touch {i}.txt")

print(system("ls"))

