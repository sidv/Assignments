# 7.Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

while True:
    num = random.randint(1, 9)
    guess = int(input("Enter the number for guess : "))
    if num == guess:
        print(f'Hurray! exact guess | you guess:{guess} num:{num}')
    elif guess < num:
        print(f'Sorry too low  | you guess:{guess} & number:{num}')
    else:
        print(f'Sorry too High | you guess {guess} & number:{num}')
