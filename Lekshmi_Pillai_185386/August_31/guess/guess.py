#7.Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too #low, too high, or exactly right.

import random
random_num = random.randint(1,9)
print(random_num)
num = int(input("Guess your number : "))

if random_num == num :
	print("Exactly right")
elif random_num < num :
	print("Too High")
else:
	print("Too Low")
