 

#7.Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
#then tell them whether they guessed too low, too high, or exactly right.

import random
num = random.randint(1,9)
guess = int(input("Enter ur guess no: "))
#range(1,10):
	
if guess > 9 or guess < 1:
	print("wrong guess")
elif guess == num:
	print("correct guess")
elif guess > num:
	print("ur guessing too high")
elif guess < num:
	print("ur guessing too low")

