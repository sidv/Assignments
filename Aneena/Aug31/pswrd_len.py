#Generate a password with length "passlen" with no duplicate characters in the password(Read about random module)
import random
import string
passlen = 8
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
special = ['*','#','@','$','%','=', ':', '?', '.', '/', '|', '~', '>','(', '<', ')'] 
all = random.choice(lower)+random.choice(upper)+random.choice(number)+random.choice(special)
for i in range(0,passlen - 4):
	temp = all + random.choice(lower) + random.choice(upper) + random.choice(number) + random.choice(special)
	dup_rmv = set(temp)
print("".join(dup_rmv))
