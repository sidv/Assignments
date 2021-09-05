import random
import string

population = string.ascii_letters+string.digits+string.punctuation

size = int(input(f"Enter the length of password (Must be less than {len(population)}: "))

if size > len(population):
	print("Cannot generate password with no duplicate characters.")

else:

	psswd = ''.join(set(random.choices(population,k = size)))

	if len(psswd) == size:
		print(psswd)
	else:
		#print(f"Password less than size {psswd}")
		while len(psswd) < size:
			new_population = ''.join(set(population) - set(psswd))
			psswd = psswd + random.choice(new_population)
		print(psswd)



