string = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""

string2 = "A broad range of industrial and consumer products use computers as control systems. Simple special-purpose devices like microwave ovens and remote controls are included, as are factory devices like industrial robots and computer-aided design, as well as general-purpose devices like personal computers and mobile devices like smartphones. Computers power the Internet, which links hundreds of millions of other computers and users. "

str1 = set(string.split(" "))
str2 = set(string2.split(" "))
print("______________________________________________________")
print("Common words \n",str1.intersection(str2))
print("______________________________________________________")
print("In string1 and not in string2 \n",str1.difference(str2))
print("______________________________________________________")
print("Unique words \n" ,str1.symmetric_difference(str2))
print("______________________________________________________")
print("append all words if they are not in string1 \n",str1.union(str2))