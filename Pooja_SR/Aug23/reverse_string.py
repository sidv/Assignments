string = """A computer is a machine that can be programmed to carry out sequences ofarithmetic or logical operations automatically.
 Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks.
 A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used
 for full operation. This term may also refer to a group of computers that are linked and function together"""

#Notes: alternate index means 0,2,4,6,8....



#Write a program to reverse all the words of above string?
print("reverse all the words")
print([x[::-1] for x in string.split(" ")])

print("_________________________________________________________________________________________________________________")
print("reverse the string")
print([x for x in string.split(" ")[::-1]])
