text = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""
text2 = text.split(" ")

for i in range(0,len(text2)):
	if text2[i].isupper() == True:
		text2[i] = text2[i].lower()
	else:
		text2[i] = text2[i].upper()

print (text2)

print (" ".join(text2))
