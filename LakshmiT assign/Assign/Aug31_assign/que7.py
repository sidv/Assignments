#7.Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too #low, too high, or exactly right.
import random
inp = random.randint(1,9)
user_num = int(input("enter the guess the number :"))
print(f"random number is {inp}")
if user_num == inp:
    print("entered number is exactly correct")
elif user_num > inp:
    print("guessed too high")
elif user_num < inp:
    print("guessed too low")
else:
    print("entered number is invalid")
