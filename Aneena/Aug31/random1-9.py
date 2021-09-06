import random
a = random.randint(1,9)
num = int(input("Guess the number :"))
print(f"Random number is {a}")
if num == a:
    print("Exactly correct")
elif num > a:
    print("Guessed too high")
elif num < a:
    print("Guessed too low")
else:
    print("Invalid number")
