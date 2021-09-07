#find all the first letter of words from above string
string = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software  and peripheral
equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""
lst = string.split(" ")
first_ltr = { x[0] for x in lst if x !=""  } 
print("first letter of words")
print(first_ltr)
