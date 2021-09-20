# 8.Write a python code to convert all upper case to lower case letters and vice versa in above string
string = """A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"""

s = ""
for i in string:
	if i.isupper():
		s += i.lower()
	elif i.islower():
		s += i.upper()
	else:
		s += i
print(s)
