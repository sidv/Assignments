s = '''A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together'''

#print(s.swapcase())
res = ""
n = len(s)
for i in range(n):
    if s[i].isupper():
        res = res + s[i].lower()
    elif s[i].islower():
        res = res + s[i].upper()
    else:
        res = res + s[i]

print(res)