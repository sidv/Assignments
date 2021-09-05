import random

charslet ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
charsnum = "1234567890"


def password():
    pwd = ""

    passlen = int(input("How long do you want the password to be?: "))
    passlet = int(input("How many letters do you want in your password?: "))
    passnum = int(input("How many numbers do you want in your password?: "))
    chars = ""

    for let in range(passlet):
        chars += random.choice(charslet)
    for num in range(passnum):
        chars += random.choice(charsnum)

    list_chars = list(chars)
    list_rand = random.shuffle(list_chars)
    print(list_chars)

    if len(list_chars) > passlen:
    	print("Out of password length")
    else:
    	pwd = "".join(list_chars)
    print(pwd)

password()
