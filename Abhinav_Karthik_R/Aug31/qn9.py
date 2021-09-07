import random
import string

passlen = 10
all_chars = list(string.digits + string.ascii_letters + string.punctuation)
random.shuffle(all_chars)
print (''.join(all_chars[:passlen]))