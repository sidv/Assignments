import random
r = random.randint(1,9)
num = int(input("Guess the number :"))
if num == r:
    print("entered number is exactly right")
elif num > r:
    print("guessed too high")
elif num < r:
    print("guessed too low")
else:
    print("invalid")
