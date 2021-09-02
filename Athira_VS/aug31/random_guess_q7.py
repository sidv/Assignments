import random

guess = int(input("Enter a number between 1 and 9 (including 1 and 9): "))

num = random.randint(1,9)

if guess > 9  or guess < 1:
    print("Invalid number.")
elif guess == num:
    print("EXactly right!!")
elif guess < num:
    print("Guessed too low!!")
elif guess > num:
    print("Guessed too high!!")

