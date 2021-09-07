# 9.Generate a password with length "passlen" with no duplicate characters in the password(Read about random module)
import random

try:
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passlen = int(input("Enter the length of password : "))
    password = ''.join(set(random.sample(s, passlen)))
    print(password)
except ValueError:
    password = None
    print('password should be less than length of s')
