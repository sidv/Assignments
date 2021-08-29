#find all the first letter of words from above string (No repetition of letters)

string = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software  and peripheral
equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""
lst = string.split(" ")
l = list(filter(lambda a: a != "",lst))
first_letter = set(map(lambda l: l[0],l))
tail_letter = "".join(first_letter)
print(tail_letter)
