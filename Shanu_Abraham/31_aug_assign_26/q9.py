#Generate a password with length "passlen" with no duplicate 
#characters in the password(Read about random module)

import random
import string

passlen = 8
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = str(random.randint(0,10))
special = str(string.punctuation)



pasw = random.choice(lower) + random.choice(upper) + random.choice(digit) + random.choice(special)

for i in range(0,passlen+1):
	temp = list(pasw + random.choice(lower) + random.choice(upper) + random.choice(lower) + random.choice(special))
	dup_rem = set(temp)

print("".join(dup_rem))
