#reverse all the words of above string
string = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software  and peripheral
equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""
lst = string.split(" ")
reverse_str = [ x[::-1]  for x in lst ]
print("...String in reverse order...") 
print(" ".join(reverse_str))
