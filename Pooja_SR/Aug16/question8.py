string = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software and peripheral
equipment needed and used for full operation.This term may also refer 
to a group of computers that are linked and function together"""
 # 8)Write a program to find all the first letter of words from above string (No repetition of letters)
print("_______________all the first ltr________________")
print(set(list(map(lambda a: a[0], string.split(" ")))))

#Write a program to reverse all the words of above string
print("__________________________reverse__________________")
print(' '.join(list(map(lambda a: a[::-1], string.split(" ")))))
