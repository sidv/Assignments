#9.Generate a password with length "passlen" with no duplicate characters in the password(Read about random module)

import random 
import string

length = int(input("Enter length of pwd: "))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)
password = "".join(temp)

print(password)

