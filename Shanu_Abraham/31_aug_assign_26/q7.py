#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
#then tell them whether they guessed too low, too high, or exactly right.

from random import randrange

value = randrange(0,10)
print(f"The random value is:{value}")
inp = int(input("Enter the guessed value"))

if  inp == value:
	print("The guessed value is exactly right")
elif inp < value:
	print("The guessed value is too low")
elif inp > value:
	print("The guessed value is too high")
else:
	print("Invalid number")
