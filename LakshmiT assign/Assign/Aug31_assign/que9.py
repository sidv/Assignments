#9.Generate a password with length "passlen" with no duplicate characters in the password(Read about random module)
import random
passlen=6
DIGITS=['0','1','2','3','4','5','6','7','8','9']
LOWER_CASE=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
UPPER_CASE=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#SYMBOLS= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
COMBINED_LIST=DIGITS + LOWER_CASE + UPPER_CASE #+ #SYMBOLS

rand_digit = random.choice(DIGITS)
rand_lower = random.choice(LOWER_CASE)
rand_upper = random.choice(UPPER_CASE)
#rand_symbol = random.choice(SYMBOLS)
temp_pass = rand_digit + rand_upper + rand_lower #+ #rand_symbol
for x in range(passlen - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
rmv_dublicate = set(list(temp_pass))
print("".join(rmv_dublicate))
