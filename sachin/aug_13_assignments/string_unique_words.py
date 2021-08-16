#11.Write a program to find all the unique words in above string and string2



string1 = """A computer is a machine that can be programmed to carry out sequences of
arithmetic or logical operations automatically. Modern computers can perform
generic sets of operations known as programs. These programs enable computers
to perform a wide range of tasks. A computer system is a complete computer
that includes the hardware operating system main software  and peripheral
equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

strin2 = """A broad range of industrial and consumer products use computers as control systems.
Simple special-purpose devices like microwave ovens and remote controls are included, 
as are factory devices like industrial robots and computer-aided design, 
as well as general-purpose devices like personal computers and mobile devices like smartphones. 
Computers power the Internet, which links hundreds of millions of other computers and users. """


set1 = set(string1.split(" "))
set2 = set(strin2.split(" "))

print(set1.union(set2))