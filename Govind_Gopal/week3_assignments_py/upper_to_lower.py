text = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""
text2 = []
for i in text:
	text2.append(i)
for i in text2:
	a = text2.index(i)
	if i.isupper() is True:
		text2[a] = text2[a].lower()

	else:
		text2[a] = text2[a].upper()

print (text2)
